#!/usr/bin/env python3
"""Build the GitHub Pages gallery in docs/ from the prompts in this repository.

One card per shot: a still from the shot, the exact prompt that produced it, and the files
behind it. The clips are not published here on purpose, so the shots are watched on YouTube.

    python scripts/build_site.py

Nothing here is retyped. The prompt text is sliced out of prompts/*.txt with an anchor pair per
shot, and every anchor must resolve exactly once or the build fails. Clip durations and sizes are
read from the files with ffprobe and ffmpeg, never assumed.

Sources outside this repository (character plates, the ComfyUI workflow) are copied into
docs/assets/ on the first run and then live here, so the published site is self-contained.
"""

from __future__ import annotations

import html
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROMPTS = REPO / "prompts"
DOCS = REPO / "docs"
OUT_ASSETS = DOCS / "assets"

# Where the source material lives on the machine that produced it. Only needed to populate
# docs/assets the first time; afterwards the copies in docs/ are the source of truth.
SRC_CLIPS = Path("E:/repos/ytideas/shots-video/assets/clips")
SRC_REFS = {
    "amber-main": Path("E:/repos/h3-walking/assets/characters/amber-main.png"),
    "sofia": Path("E:/repos/h3-walking/assets/characters/sofia.png"),
    "allie": Path("E:/repos/h3-walking/assets/characters/allie.png"),
    "kate": Path("E:/repos/h3-walking/assets/characters/kate.png"),
}
SRC_WORKFLOW = Path(
    "E:/repos/ytideas/h3-shot-library/tests/templates/h3_dollyzoom_test_v6flip.json")
SRC_LOGO = Path("E:/repos/h3-walking/showcase-video/assets/refs/loopforge-logo.png")

REPO_URL = "https://github.com/loopforge0/minimaxh3-shots-skills"
SEED = "552013742"

# Each group gets its own tone, stepping through the pink to blue of the Loop Forge mark.
# The video's green is the video's; this is a Loop Forge page, so it wears the logo's palette.
GROUPS = [
    ("zoom",         "zoom",         "#f06bb8"),
    ("specialty",    "specialty",    "#b57cf0"),
    ("pan and roll", "pan-and-roll", "#6f95f7"),
    ("tracking",     "tracking",     "#4fc9dd"),
]
GROUP_SLUG = {g: s for g, s, _ in GROUPS}
GROUP_TONE = {g: c for g, _, c in GROUPS}

# id -> name, slug, group, prompt file, frames, reference plates,
#       clause start anchor, clause end anchor, lighting anchor (where the gear phrase stops)
#
# ⚠️ The reference plates for C-01b and K-06n are not recorded in a run manifest: both were run
# on the rented card rather than locally, so there is no cached workflow for them. Both prompts
# describe the ginger-red-haired subject, which is amber-main, and that is what is listed.
SHOTS = [
    ("C-01b", "Crash zoom in", "crash-zoom-in", "zoom",
     "C-01b_crash-zoom-in-hold-then-snap.txt", 124, ["amber-main"],
     "The camera is locked off and completely motionless",
     "the framing does not change for the remainder of the shot.",
     "cold blue-green arctic lighting"),
    ("C-08", "Yo-yo zoom", "yoyo-zoom", "zoom",
     "C-08_yoyo-zoom.txt", 192, ["sofia"],
     "The camera begins in a tight close-up", "exactly as it began.",
     "warm golden-hour sunlight"),
    ("K-06n", "Dolly zoom", "dolly-zoom", "specialty",
     "K-06n_dolly-zoom-k06.txt", 124, ["amber-main"],
     "The camera pushes in while simultaneously zooming out", "focal length changes.",
     "warm amber stage lighting"),
    ("D-05", "Snorricam", "snorricam", "specialty",
     "D-05_snorricam-corridor.txt", 192, ["allie"],
     "Her shoulders and chest stay frozen in the frame throughout",
     "before the next room opens up ahead of her.",
     "harsh mixed party lighting"),
    ("D-03", "Rack focus", "rack-focus", "specialty",
     "D-03_rack-focus.txt", 124, ["sofia", "allie", "amber-main"],
     "The camera holds a static shot.", "as they resolve sharply.",
     "warm golden-hour sunlight"),
    ("D-04", "Split screen", "split-screen", "specialty",
     "D-04_multi-panel-split-screen.txt", 192, ["amber-main"],
     "The frame is divided into three equal vertical panels", "three different angles.",
     "cool monitor light"),
    ("C-02", "Whip pan", "whip-pan", "pan and roll",
     "C-02_whip-pan.txt", 124, ["amber-main", "kate"],
     "The camera starts framed on", "resolving sharply on <Subject 2>'s face.",
     "cold blue-green arctic lighting"),
    ("C-09", "Dutch angle", "dutch-angle", "pan and roll",
     "C-09_dutch-angle.txt", 124, ["kate"],
     "The camera rolls counterclockwise", "off-axis.",
     "cold blue dusk light"),
    ("C-03", "Super dolly in", "super-dolly-in", "tracking",
     "C-03_super-dolly-in.txt", 124, ["kate"],
     "The camera pushes in with large amplitude at fast speed, charging",
     "her face filling the frame.", "cold blue dusk light"),
    ("C-10", "Eyes in", "eyes-in", "tracking",
     "C-10_eyes-in.txt", 124, ["amber-main"],
     "The camera pushes in with large amplitude at slow speed", "filling the view.",
     "cold blue-green arctic lighting"),
    ("C-06", "Aerial pullback", "aerial-pullback", "tracking",
     "C-06_aerial-pullback.txt", 124, ["kate"],
     "The camera pulls out with large amplitude", "opens out around her.",
     "cold blue dusk light"),
    ("C-07", "Handheld", "handheld", "tracking",
     "C-07_handheld.txt", 124, ["amber-main"],
     "The camera shakes strongly", "with every stride.",
     "cold blue-green arctic lighting"),
    ("C-04", "360 orbit", "orbit-360", "tracking",
     "C-04_360-orbit.txt", 124, ["sofia"],
     "The camera performs an arc shot", "coming back to the front.",
     "warm golden-hour sunlight"),
    ("C-05", "Crane rise", "crane-rise", "tracking",
     "C-05_crane-drone-rise.txt", 124, ["allie"],
     "The camera starts low at", "sharp in frame.",
     "warm soft afternoon sunlight"),
]


def run(cmd: list[str]) -> str:
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout


def need(tool: str) -> None:
    if not shutil.which(tool):
        sys.exit(f"error: {tool} is not on PATH; it is needed to measure and stage the media")


def probe(path: Path) -> tuple[float, int, int]:
    out = run(["ffprobe", "-v", "error", "-select_streams", "v:0",
               "-show_entries", "stream=width,height", "-show_entries", "format=duration",
               "-of", "csv=p=0", str(path)]).split()
    w, h = (int(v) for v in out[0].strip().rstrip(",").split(",")[:2])
    return round(float(out[1]), 3), w, h


def slice_prompt(shot: str, text: str, start: str, end: str, lighting: str) -> dict:
    """before / gear / between / clause / after, from the real file. Fails loudly."""
    if text.count(start) != 1:
        sys.exit(f"error: {shot}: clause start anchor occurs {text.count(start)} times, need 1")
    i = text.index(start)
    tail = text[i:]
    if end not in tail:
        sys.exit(f"error: {shot}: clause end anchor not found after the start anchor")
    j = i + tail.index(end) + len(end)

    g0 = text.find("shot on ")
    if g0 < 0:
        sys.exit(f'error: {shot}: no gear phrase ("shot on ") in the prompt')
    rel = text[g0:].find(lighting)
    if rel < 0:
        sys.exit(f"error: {shot}: lighting anchor not found after the gear phrase: {lighting!r}")
    gear = text[g0:g0 + rel].rstrip().rstrip(",")
    if not (8 < len(gear) < 200):
        sys.exit(f"error: {shot}: gear phrase is {len(gear)} chars, anchors look wrong")
    if g0 + rel > i:
        sys.exit(f"error: {shot}: gear phrase overlaps the clause")

    return {
        "a": text[:g0], "gear": gear, "b": text[g0 + len(gear):i],
        "clause": text[i:j], "c": text[j:],
        "clauseWords": len(text[i:j].split()), "promptWords": len(text.split()),
    }


def stage() -> None:
    """Copy the character plates and the workflow into docs/, and cut one still per shot.

    The clips themselves are deliberately NOT published here. The video lives on YouTube and that
    is where the shots should be watched; the page carries one frame per shot so a reader can tie
    a prompt back to something they have already seen.
    """
    for sub in ("stills", "refs", "refs/thumbs", "workflow"):
        (OUT_ASSETS / sub).mkdir(parents=True, exist_ok=True)

    if SRC_LOGO.exists() and not (OUT_ASSETS / "loopforge-logo.png").exists():
        shutil.copy2(SRC_LOGO, OUT_ASSETS / "loopforge-logo.png")

    wf = OUT_ASSETS / "workflow" / SRC_WORKFLOW.name
    if SRC_WORKFLOW.exists() and not wf.exists():
        shutil.copy2(SRC_WORKFLOW, wf)

    for name, src in SRC_REFS.items():
        dst = OUT_ASSETS / "refs" / f"{name}.png"
        if src.exists() and not dst.exists():
            shutil.copy2(src, dst)
        thumb = OUT_ASSETS / "refs" / "thumbs" / f"{name}.jpg"
        if dst.exists() and not thumb.exists():
            # kate.png alone is 7 MB; the page shows thumbnails and links the originals
            run(["ffmpeg", "-y", "-v", "error", "-i", str(dst),
                 "-vf", "scale=420:-1", "-q:v", "4", str(thumb)])

    for shot in SHOTS:
        sid = shot[0]
        still = OUT_ASSETS / "stills" / f"{sid}.jpg"
        if still.exists():
            continue
        clip = SRC_CLIPS / f"{sid}_00001_.mp4"
        if not clip.exists():
            sys.exit(f"error: {sid}: no still yet and the source clip is missing ({clip})")
        dur, _, _ = probe(clip)
        run(["ffmpeg", "-y", "-v", "error", "-ss", f"{dur / 2:.3f}", "-i", str(clip),
             "-frames:v", "1", "-q:v", "3", str(still)])


def build_manifest() -> list[dict]:
    """Per shot: the prompt slices, and the clip facts.

    Clip facts are measured from the source clips when they are present. When they are not, the
    values already in docs/data/shots.json are reused, so the site still rebuilds on a machine
    that only has this repository.
    """
    cached = {}
    prev = DOCS / "data" / "shots.json"
    if prev.exists():
        cached = {e["id"]: e for e in json.loads(prev.read_text(encoding="utf-8"))}

    out = []
    for (sid, name, slug, group, pfile, frames, refs, start, end, lighting) in SHOTS:
        path = PROMPTS / pfile
        if not path.exists():
            sys.exit(f"error: {sid}: missing prompt {path}")
        parts = slice_prompt(sid, path.read_text(encoding="utf-8"), start, end, lighting)

        clip = SRC_CLIPS / f"{sid}_00001_.mp4"
        if clip.exists():
            dur, w, h = probe(clip)
        elif sid in cached:
            dur, w, h = cached[sid]["duration"], cached[sid]["width"], cached[sid]["height"]
        else:
            sys.exit(f"error: {sid}: no source clip and nothing cached to fall back on")

        out.append({
            "id": sid, "name": name, "slug": slug, "group": group,
            "promptFile": pfile, "frames": frames, "refs": refs,
            "duration": dur, "width": w, "height": h, **parts,
        })
        print(f"  {sid:<6} {name:<16} {group:<13} {dur:>6.3f}s  {w}x{h}  "
              f"{parts['promptWords']:>3} words")
    return out


# ----------------------------------------------------------------------------- page

def esc(s: str) -> str:
    return html.escape(s, quote=False)


def card(e: dict, wf_name: str) -> str:
    """One shot: a still, the plain prompt, and the files behind it.

    The prompt is shown unmarked. On the page the whole thing is there to be read and copied;
    colouring two passages of it is the video's job, not this one's.
    """
    gslug = GROUP_SLUG[e["group"]]
    refs = "".join(
        f'<a class="ref" href="assets/refs/{r}.png" download title="{r}.png">'
        f'<img src="assets/refs/thumbs/{r}.jpg" alt="{r}" loading="lazy"><span>{r}</span></a>'
        for r in e["refs"])
    body = esc(e["a"] + e["gear"] + e["b"] + e["clause"] + e["c"])
    return f'''
      <article class="card g-{gslug}" id="{e["slug"]}" data-group="{e["group"]}">
        <header class="card-head">
          <div class="card-title">
            <h2>{esc(e["name"])}</h2>
            <span class="badge">{e["group"]}</span>
          </div>
          <dl class="specs">
            <div><dt>frames</dt><dd>{e["frames"]}</dd></div>
            <div><dt>length</dt><dd>{e["duration"]:.2f}s</dd></div>
            <div><dt>size</dt><dd>{e["width"]}&times;{e["height"]}</dd></div>
          </dl>
        </header>

        <div class="card-body">
          <div class="media">
            <img class="still" src="assets/stills/{e["id"]}.jpg"
                 alt="Frame from the {esc(e["name"].lower())} shot" loading="lazy">
            <div class="dl">
              <a class="btn" href="assets/workflow/{wf_name}" download>Workflow <span>ComfyUI json</span></a>
            </div>
            <div class="refs">
              <h3>Reference plates</h3>
              <div class="ref-row">{refs}</div>
            </div>
          </div>

          <div class="prompt">
            <div class="prompt-head">
              <span class="prompt-label">Prompt</span>
              <button class="copy" data-target="p-{e["id"]}">Copy</button>
            </div>
            <pre id="p-{e["id"]}" class="prompt-body">{body}</pre>
          </div>
        </div>
      </article>'''


def page(entries: list[dict], wf_name: str) -> str:
    cards = "\n".join(card(e, wf_name) for e in entries)
    chips = "".join(
        f'<button class="chip g-{s}" data-filter="{g}">{g}'
        f'<span class="n">{sum(1 for e in entries if e["group"] == g)}</span></button>'
        for g, s, _ in GROUPS)
    # this f-string is not the page f-string, so a literal brace is {{ here, not {{{{
    tones = "\n".join(f"  .g-{s} {{ --tone:{c}; }}" for _, s, c in GROUPS)
    ramp = ",".join(c for _, _, c in GROUPS)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MiniMax H3 camera shots &middot; Loop Forge</title>
<meta name="description" content="The exact prompts behind fourteen named camera shots in MiniMax H3, with the reference plates and the ComfyUI workflow.">
<link rel="icon" href="assets/loopforge-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Oswald:wght@400;500;700&family=JetBrains+Mono:wght@400;700&display=swap">
<style>
  :root {{
    --ink:#07090c; --slate:#121a20; --slate-2:#1b2730;
    --frost:#e8eff2; --frost-dim:#93a7b2; --line:#2a3a45;
    --tone:#b57cf0;
    --r:14px;
  }}
{tones}
  * {{ box-sizing:border-box; }}
  html {{ scroll-behavior:smooth; scroll-padding-top:150px; }}
  body {{
    margin:0; background:var(--ink); color:var(--frost);
    font-family:"Oswald",system-ui,sans-serif; font-weight:400;
    font-size:17px; line-height:1.6; -webkit-font-smoothing:antialiased;
  }}
  a {{ color:var(--tone); }}

  .bar {{
    position:sticky; top:0; z-index:20;
    display:flex; align-items:center; gap:18px;
    padding:14px 28px; background:rgba(7,9,12,.9);
    backdrop-filter:blur(14px);
    border-bottom:1px solid var(--line);
  }}
  .bar::after {{
    content:""; position:absolute; left:0; right:0; bottom:-1px; height:2px;
    background:linear-gradient(90deg,{ramp});
  }}
  .bar img {{ width:40px; height:40px; flex:none; }}
  .brand {{ display:flex; flex-direction:column; line-height:1.15; }}
  .brand b {{ font-family:"Archivo Black",system-ui,sans-serif; font-size:18px; letter-spacing:-.01em; }}
  .brand span {{ font-size:12px; letter-spacing:.16em; text-transform:uppercase; color:var(--frost-dim); }}
  .bar nav {{ margin-left:auto; display:flex; gap:10px; flex-wrap:wrap; }}
  .bar nav a {{
    font-size:14px; letter-spacing:.04em; text-transform:uppercase;
    color:var(--frost-dim); text-decoration:none; padding:7px 13px;
    border:1px solid var(--line); border-radius:999px;
  }}
  .bar nav a:hover {{ color:var(--frost); border-color:var(--frost-dim); }}

  .wrap {{ max-width:1320px; margin:0 auto; padding:0 28px 96px; }}

  .filters {{
    position:sticky; top:70px; z-index:10;
    display:flex; flex-wrap:wrap; gap:10px; align-items:center;
    padding:20px 0 22px; background:linear-gradient(var(--ink) 74%,rgba(7,9,12,0));
  }}
  .chip {{
    font-family:inherit; font-size:14px; letter-spacing:.05em; text-transform:uppercase;
    color:var(--frost-dim); background:transparent; cursor:pointer;
    border:1px solid var(--line); border-radius:999px; padding:8px 15px;
    display:inline-flex; align-items:center; gap:9px;
  }}
  .chip .n {{ font-family:"JetBrains Mono",monospace; font-size:12px; color:var(--tone); }}
  .chip:hover {{ color:var(--frost); border-color:var(--tone); }}
  .chip[aria-pressed="true"] {{ color:var(--ink); background:var(--tone); border-color:var(--tone); }}
  .chip[aria-pressed="true"] .n {{ color:var(--ink); opacity:.72; }}

  .card {{
    border:1px solid var(--line); border-left:3px solid var(--tone); border-radius:var(--r);
    background:var(--slate); margin:22px 0; overflow:hidden; scroll-margin-top:160px;
  }}
  .card[hidden] {{ display:none; }}
  .card-head {{
    display:flex; flex-wrap:wrap; gap:16px 30px; align-items:center; justify-content:space-between;
    padding:20px 24px; border-bottom:1px solid var(--line);
  }}
  .card-title {{ display:flex; align-items:center; gap:14px; }}
  .card-title h2 {{
    font-family:"Archivo Black",system-ui,sans-serif; font-weight:400;
    font-size:27px; letter-spacing:-.02em; margin:0;
  }}
  .badge {{
    font-size:12px; letter-spacing:.12em; text-transform:uppercase;
    color:var(--tone); border:1px solid color-mix(in srgb, var(--tone) 42%, transparent);
    background:color-mix(in srgb, var(--tone) 12%, transparent);
    border-radius:999px; padding:4px 11px;
  }}
  .specs {{ display:flex; flex-wrap:wrap; gap:8px 26px; margin:0; font-family:"JetBrains Mono",monospace; font-size:13px; }}
  .specs dt {{ color:var(--frost-dim); font-size:11px; letter-spacing:.08em; text-transform:uppercase; }}
  .specs dd {{ margin:2px 0 0; color:var(--frost); }}

  .card-body {{ display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1.05fr); }}
  .media {{ padding:22px 24px; border-right:1px solid var(--line); }}
  .still {{
    width:100%; aspect-ratio:16/9; object-fit:cover; display:block;
    background:#000; border:1px solid var(--line); border-radius:10px;
  }}

  .dl {{ display:flex; flex-wrap:wrap; gap:9px; margin-top:16px; }}
  .btn {{
    display:inline-flex; align-items:baseline; gap:8px; text-decoration:none;
    font-size:14px; letter-spacing:.03em;
    color:var(--frost); background:var(--slate-2);
    border:1px solid var(--line); border-radius:9px; padding:9px 14px;
  }}
  .btn span {{ font-family:"JetBrains Mono",monospace; font-size:11px; color:var(--frost-dim); }}
  .btn:hover {{ border-color:var(--tone); color:var(--tone); }}
  .btn:hover span {{ color:var(--tone); }}

  .refs h3 {{
    font-size:11px; letter-spacing:.14em; text-transform:uppercase;
    color:var(--frost-dim); margin:22px 0 10px; font-weight:500;
  }}
  .ref-row {{ display:flex; flex-wrap:wrap; gap:12px; }}
  .ref {{ text-decoration:none; color:var(--frost-dim); font-size:12px; text-align:center; }}
  .ref img {{
    display:block; width:84px; height:84px; object-fit:cover;
    border:1px solid var(--line); border-radius:9px; background:var(--slate-2);
  }}
  .ref span {{ display:block; margin-top:5px; font-family:"JetBrains Mono",monospace; }}
  .ref:hover img {{ border-color:var(--tone); }}
  .ref:hover span {{ color:var(--tone); }}

  .prompt {{ display:flex; flex-direction:column; min-width:0; }}
  .prompt-head {{
    display:flex; align-items:center; justify-content:space-between; gap:14px;
    padding:16px 24px; border-bottom:1px solid var(--line);
  }}
  .prompt-label {{
    font-size:11px; letter-spacing:.14em; text-transform:uppercase; color:var(--frost-dim);
  }}
  .copy {{
    font-family:inherit; font-size:13px; letter-spacing:.04em; cursor:pointer;
    color:var(--frost-dim); background:transparent;
    border:1px solid var(--line); border-radius:8px; padding:6px 12px;
  }}
  .copy:hover {{ color:var(--tone); border-color:var(--tone); }}
  .prompt-body {{
    margin:0; padding:20px 24px; max-height:560px; overflow:auto;
    font-family:"JetBrains Mono",monospace; font-size:13.5px; line-height:1.72;
    white-space:pre-wrap; word-break:normal; overflow-wrap:break-word;
    color:var(--frost-dim);
  }}

  @media (max-width:980px) {{
    .card-body {{ grid-template-columns:1fr; }}
    .media {{ border-right:0; border-bottom:1px solid var(--line); }}
    .prompt-body {{ max-height:420px; }}
    .filters {{ top:66px; }}
  }}
  @media (prefers-reduced-motion:reduce) {{ html {{ scroll-behavior:auto; }} }}
</style>
</head>
<body>

<div class="bar">
  <img src="assets/loopforge-logo.png" alt="Loop Forge">
  <div class="brand"><b>Loop Forge</b><span>MiniMax H3 camera shots</span></div>
  <nav>
    <a href="{REPO_URL}">Repository</a>
    <a href="https://www.youtube.com/@LoopForge0">YouTube</a>
  </nav>
</div>

<div class="wrap">
  <div class="filters">
    <button class="chip" data-filter="all" aria-pressed="true">all<span class="n">{len(entries)}</span></button>
    {chips}
  </div>

  <main>
{cards}
  </main>
</div>

<script>
  const chips = document.querySelectorAll('.chip');
  const cards = document.querySelectorAll('.card');
  chips.forEach(c => c.addEventListener('click', () => {{
    chips.forEach(o => o.setAttribute('aria-pressed', String(o === c)));
    const f = c.dataset.filter;
    cards.forEach(card => {{ card.hidden = !(f === 'all' || card.dataset.group === f); }});
  }}));

  document.querySelectorAll('.copy').forEach(b => b.addEventListener('click', async () => {{
    const el = document.getElementById(b.dataset.target);
    try {{
      await navigator.clipboard.writeText(el.innerText);
      const was = b.textContent; b.textContent = 'Copied';
      setTimeout(() => {{ b.textContent = was; }}, 1400);
    }} catch (e) {{ b.textContent = 'Press Ctrl C'; }}
  }}));
</script>
</body>
</html>
'''


def main() -> None:
    need("ffprobe")
    need("ffmpeg")
    DOCS.mkdir(exist_ok=True)
    stage()
    entries = build_manifest()

    wf_name = SRC_WORKFLOW.name
    (DOCS / "data").mkdir(exist_ok=True)
    (DOCS / "data" / "shots.json").write_text(
        json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    (DOCS / "index.html").write_text(page(entries, wf_name), encoding="utf-8", newline="\n")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    print(f"\n{len(entries)} shots -> docs/index.html")


if __name__ == "__main__":
    main()
