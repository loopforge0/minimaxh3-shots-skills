#!/usr/bin/env python3
"""Speed-ramp a crash zoom so the zoom itself lasts a few frames, the way an editor would.

H3 picks its own pace for a zoom. A prompt can ask for a 200 ms snap, and the render still takes far
longer: 2.6 s for the Part 2 crash zoom in and 1.7 s for the crash zoom out at 1344x768. No wording
tried so far fixes that, so this fixes it after the render instead.

How it works: every frame is compared (SSIM, at 32 px wide) against the first frame and against the
last. The zoom is the stretch where the picture stops looking like the opening framing and starts
looking like the closing one. That stretch is played fast enough to last TARGET_FRAMES frames, and the
audio over the same stretch is sped up by the same factor with its pitch kept, so picture and sound
stay in sync. Everything before and after the zoom is untouched; the clip just gets shorter.

    python scripts/snap.py input.mp4 output.mp4

Limits:
- Built for a clip that holds one framing, zooms once, and holds the other framing. A clip with two
  zooms, a cut, or a camera that keeps moving after the zoom will get the wrong window.
- If the framing never changes much, or the zoom is already TARGET_FRAMES frames or shorter, the input
  is copied unchanged and the report says "ramped: False".
- The video is re-encoded (libx264, CRF 16) and the audio becomes AAC 192k.
- Tested on two 1344x768, 24 fps, 124-frame H3 renders. Check the reported window against your clip.

Needs Python 3.9+ and ffmpeg / ffprobe on PATH. Standard library only.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"
TARGET_FRAMES = 3   # how long the zoom should last after the ramp: 0.125 s at 24 fps, under a crash zoom's 0.2 s


def _similarity(video: Path, ref: Path) -> list[float]:
    """SSIM of every frame of `video` against one still, at a small size."""
    out = subprocess.run([FFMPEG, "-v", "error", "-i", str(video), "-loop", "1", "-i", str(ref), "-filter_complex",
                          "[0:v]scale=32:-2[a];[a][1:v]ssim=stats_file=-", "-shortest", "-f", "null", "-"],
                         capture_output=True, text=True, check=True).stdout
    return [float(x) for x in re.findall(r"All:([0-9.]+)", out)]


def zoom_window(video: Path) -> tuple[int, int] | None:
    """The zoom, as [start, end) frames: where the picture stops looking like the opening framing,
    to where it starts looking like the closing one. Comparing against both ends ignores what moves
    inside a framing (a face reacting), which a frame-to-frame difference would count as zoom."""
    with tempfile.TemporaryDirectory() as tmp:
        first, last = Path(tmp) / "first.png", Path(tmp) / "last.png"
        subprocess.run([FFMPEG, "-v", "error", "-y", "-i", str(video), "-vf", "scale=32:-2",
                        "-frames:v", "1", str(first)], check=True)
        subprocess.run([FFMPEG, "-v", "error", "-y", "-sseof", "-0.1", "-i", str(video), "-vf", "scale=32:-2",
                        "-update", "1", str(last)], check=True)
        to_first, to_last = _similarity(video, first), _similarity(video, last)
    n = min(len(to_first), len(to_last))
    if n < 20 or max(to_first) - min(to_first) < 0.15:
        return None  # the framing never changes much: no zoom
    # The zoom starts once the picture has gone 15% of the way from the opening framing's likeness
    # down to the least alike it gets, and ends once it has come 92% of the way up to the closing
    # framing. Levels rather than rates: a face drifting inside the held opening framing changes the
    # picture slowly but for a long time, and a rate threshold low enough to catch a soft zoom also
    # caught that drift and ramped the whole hold away on a crash zoom out.
    head = max(to_first[:8])
    low = min(to_first)
    start = next(i for i in range(n) if to_first[i] < head - 0.15 * (head - low)) - 2
    start = max(0, start)
    floor = min(to_last[:start + 1])
    end = next((i for i in range(start, n) if to_last[i] >= floor + 0.92 * (1 - floor)), n - 1)
    if end <= start:
        return None
    return start, end + 1


def _atempo(factor: float) -> str:
    """atempo takes 0.5..2.0 per stage, so a bigger factor is a chain."""
    stages = []
    while factor > 2.0:
        stages.append("atempo=2.0")
        factor /= 2.0
    stages.append(f"atempo={factor:.4f}")
    return ",".join(stages)


def snap(src: Path, dst: Path) -> dict:
    """Write `dst` with the zoom ramped to about TARGET_FRAMES frames. Copies `src` if no zoom is found."""
    fps_text = subprocess.run([FFPROBE, "-v", "error", "-select_streams", "v:0", "-show_entries",
                               "stream=r_frame_rate", "-of", "csv=p=0", str(src)],
                              capture_output=True, text=True, check=True).stdout.strip()
    num, _, den = fps_text.partition("/")
    fps = float(num) / float(den or 1)
    window = zoom_window(src)
    if not window or window[1] - window[0] <= TARGET_FRAMES:
        shutil.copyfile(src, dst)
        return {"ramped": False, "window": window}
    a, b = window
    factor = (b - a) / TARGET_FRAMES
    t0, t1 = a / fps, b / fps
    has_audio = bool(subprocess.run([FFPROBE, "-v", "error", "-select_streams", "a", "-show_entries",
                                     "stream=index", "-of", "csv=p=0", str(src)],
                                    capture_output=True, text=True).stdout.strip())
    graph = (f"[0:v]trim=end={t0},setpts=PTS-STARTPTS[v0];"
             f"[0:v]trim=start={t0}:end={t1},setpts=(PTS-STARTPTS)/{factor:.4f}[v1];"
             f"[0:v]trim=start={t1},setpts=PTS-STARTPTS[v2];"
             "[v0][v1][v2]concat=n=3:v=1:a=0,fps=" + f"{fps:g}" + "[v]")
    maps = ["-map", "[v]"]
    if has_audio:
        graph += (f";[0:a]atrim=end={t0},asetpts=PTS-STARTPTS[a0];"
                  f"[0:a]atrim=start={t0}:end={t1},asetpts=PTS-STARTPTS,{_atempo(factor)}[a1];"
                  f"[0:a]atrim=start={t1},asetpts=PTS-STARTPTS[a2];"
                  "[a0][a1][a2]concat=n=3:v=0:a=1[a]")
        maps += ["-map", "[a]", "-c:a", "aac", "-b:a", "192k"]
    subprocess.run([FFMPEG, "-v", "error", "-y", "-i", str(src), "-filter_complex", graph, *maps,
                    "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(dst)],
                   check=True)
    return {"ramped": True, "window": window, "seconds": [round(t0, 2), round(t1, 2)], "factor": round(factor, 1)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", type=Path, help="the clip as H3 rendered it")
    ap.add_argument("output", type=Path, help="where to write the ramped clip")
    args = ap.parse_args()

    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        sys.exit("error: ffmpeg and ffprobe must be on PATH")
    if not args.input.is_file():
        sys.exit(f"error: no such file: {args.input}")
    if args.input.resolve() == args.output.resolve():
        sys.exit("error: write to a different file; the input is read while the output is written")
    args.output.parent.mkdir(parents=True, exist_ok=True)

    result = snap(args.input, args.output)
    if result["ramped"]:
        a, b = result["window"]
        t0, t1 = result["seconds"]
        print(f"zoom found at frames {a}-{b} ({t0}-{t1} s, {b - a} frames), "
              f"sped up {result['factor']}x to {TARGET_FRAMES} frames")
    elif result["window"]:
        print(f"zoom at frames {result['window'][0]}-{result['window'][1]} is already short; copied unchanged")
    else:
        print("no zoom found; copied unchanged")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
