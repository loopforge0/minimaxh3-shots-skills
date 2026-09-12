#!/usr/bin/env python3
"""Build the GitHub Pages gallery in docs/ from the prompts in this repository.

One card per shot: the clip, the exact prompt with its camera and lens phrase and its camera
clause marked, and download links for everything that produced it.

    python scripts/build_site.py

Nothing here is retyped. The prompt text is sliced out of prompts/*.txt with an anchor pair per
shot, and every anchor must resolve exactly once or the build fails. Clip durations and sizes are
read from the files with ffprobe and ffmpeg, never assumed.

Sources outside this repository (clips, character plates, the ComfyUI workflow) are copied into
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

GROUPS = [
    ("zoom", "the lens moves, not the camera"),
    ("specialty", "rig, focus and compound moves"),
    ("pan and roll", "the camera turns in place"),
    ("tracking", "the camera travels"),
]

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
    """Copy the source media into docs/assets once, and build the web-sized derivatives."""
    for sub in ("clips", "posters", "refs", "refs/thumbs", "workflow"):
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
        dst = OUT_ASSETS / "clips" / f"{sid}.mp4"
        if not dst.exists():
            src = SRC_CLIPS / f"{sid}_00001_.mp4"
            if not src.exists():
                sys.exit(f"error: {sid}: missing source clip {src}")
            shutil.copy2(src, dst)
        poster = OUT_ASSETS / "posters" / f"{sid}.jpg"
        if not poster.exists():
            dur, _, _ = probe(dst)
            run(["ffmpeg", "-y", "-v", "error", "-ss", f"{dur / 2:.3f}", "-i", str(dst),
                 "-frames:v", "1", "-q:v", "3", str(poster)])


def build_manifest() -> list[dict]:
    out = []
    for (sid, name, slug, group, pfile, frames, refs, start, end, lighting) in SHOTS:
        path = PROMPTS / pfile
        if not path.exists():
            sys.exit(f"error: {sid}: missing prompt {path}")
        text = path.read_text(encoding="utf-8")
        parts = slice_prompt(sid, text, start, end, lighting)

        clip = OUT_ASSETS / "clips" / f"{sid}.mp4"
        dur, w, h = probe(clip)
        entry = {
            "id": sid, "name": name, "slug": slug, "group": group,
            "promptFile": pfile, "frames": frames, "refs": refs,
            "duration": dur, "width": w, "height": h,
            "clipBytes": clip.stat().st_size,
            **parts,
        }
        out.append(entry)
        print(f"  {sid:<6} {name:<16} {group:<13} {dur:>6.3f}s  {w}x{h}  "
              f"clause {parts['clauseWords']:>3}/{parts['promptWords']:>3} words")
    return out


# ----------------------------------------------------------------------------- page

def esc(s: str) -> str:
    return html.escape(s, quote=False)


def prompt_html(e: dict) -> str:
    """The prompt, with the two camera sections marked the same way the video marks them."""
    return (f'<span>{esc(e["a"])}</span>'
            f'<mark class="gear">{esc(e["gear"])}</mark>'
            f'<span>{esc(e["b"])}</span>'
            f'<mark class="clause">{esc(e["clause"])}</mark>'
            f'<span>{esc(e["c"])}</span>')


def card(e: dict, wf_name: str) -> str:
    mb = e["clipBytes"] / 1e6
    refs = "".join(
        f'<a class="ref" href="assets/refs/{r}.png" download title="{r}.png">'
        f'<img src="assets/refs/thumbs/{r}.jpg" alt="{r}" loading="lazy"><span>{r}</span></a>'
        for r in e["refs"])
    return f'''
      <article class="card" id="{e["slug"]}" data-group="{e["group"]}">
        <header class="card-head">
          <div class="card-title">
            <h2>{esc(e["name"])}</h2>
            <span class="badge">{e["group"]}</span>
          </div>
          <dl class="specs">
            <div><dt>frames</dt><dd>{e["frames"]}</dd></div>
            <div><dt>length</dt><dd>{e["duration"]:.2f}s</dd></div>
            <div><dt>size</dt><dd>{e["width"]}&times;{e["height"]}</dd></div>
            <div><dt>clause</dt><dd>{e["clauseWords"]} of {e["promptWords"]} words</dd></div>
          </dl>
        </header>

        <div class="card-body">
          <div class="media">
            <video controls preload="none" playsinline
                   poster="assets/posters/{e["id"]}.jpg"
                   src="assets/clips/{e["id"]}.mp4"></video>
            <div class="dl">
              <a class="btn" href="assets/clips/{e["id"]}.mp4" download>Clip <span>mp4, {mb:.1f} MB</span></a>
              <a class="btn" href="prompts/{e["promptFile"]}" download>Prompt <span>txt</span></a>
              <a class="btn" href="assets/workflow/{wf_name}" download>Workflow <span>ComfyUI json</span></a>
            </div>
            <div class="refs">
              <h3>Reference plates</h3>
              <div class="ref-row">{refs}</div>
            </div>
          </div>

          <div class="prompt">
            <div class="prompt-head">
              <code>{esc(e["promptFile"])}</code>
              <button class="copy" data-target="p-{e["id"]}">Copy prompt</button>
            </div>
            <pre id="p-{e["id"]}" class="prompt-body">{prompt_html(e)}</pre>
          </div>
        </div>
      </article>'''


def page(entries: list[dict], wf_name: str) -> str:
    cards = "\n".join(card(e, wf_name) for e in entries)
    nav = "".join(
        f'<button class="chip" data-filter="{g}">{g}'
        f'<span class="n">{sum(1 for e in entries if e["group"] == g)}</span></button>'
        for g, _ in GROUPS)
    legend = "".join(
        f'<div><dt>{g}</dt><dd>{d}</dd></div>' for g, d in GROUPS)
    total_mb = sum(e["clipBytes"] for e in entries) / 1e6

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MiniMax H3 camera shots &middot; Loop Forge</title>
<meta name="description" content="Fourteen named camera shots in MiniMax H3, with the exact prompt, clip, reference plates and ComfyUI workflow behind each one.">
<link rel="icon" href="assets/loopforge-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Oswald:wght@400;500;700&family=JetBrains+Mono:wght@400;700&display=swap">
<style>
  :root {{
    --ink:#07090c; --slate:#121a20; --slate-2:#1b2730;
    --frost:#e8eff2; --frost-dim:#93a7b2; --line:#2a3a45;
    --works:#5fe3b1; --pink:#e85bbd; --blue:#5b8ff5;
    --r:14px;
  }}
  * {{ box-sizing:border-box; }}
  html {{ scroll-behavior:smooth; scroll-padding-top:104px; }}
  body {{
    margin:0; background:var(--ink); color:var(--frost);
    font-family:"Oswald",system-ui,sans-serif; font-weight:400;
    font-size:17px; line-height:1.6; -webkit-font-smoothing:antialiased;
  }}
  a {{ color:var(--works); }}

  /* ---------- top bar ---------- */
  .bar {{
    position:sticky; top:0; z-index:20;
    display:flex; align-items:center; gap:18px;
    padding:14px 28px; background:rgba(7,9,12,.86);
    backdrop-filter:blur(14px);
    border-bottom:1px solid var(--line);
  }}
  .bar::after {{
    content:""; position:absolute; left:0; right:0; bottom:-1px; height:2px;
    background:linear-gradient(90deg,var(--pink),var(--blue),var(--works));
    opacity:.85;
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

  /* ---------- hero ---------- */
  .wrap {{ max-width:1320px; margin:0 auto; padding:0 28px 96px; }}
  .hero {{ padding:64px 0 40px; border-bottom:1px solid var(--line); }}
  .hero h1 {{
    font-family:"Archivo Black",system-ui,sans-serif; font-weight:400;
    font-size:clamp(38px,6vw,76px); line-height:1.02; letter-spacing:-.03em; margin:0 0 20px;
  }}
  .hero p {{ max-width:68ch; color:var(--frost-dim); margin:0 0 14px; }}
  .hero strong {{ color:var(--frost); font-weight:500; }}
  .meta {{
    display:flex; flex-wrap:wrap; gap:10px 26px; margin-top:26px;
    font-family:"JetBrains Mono",monospace; font-size:13px; color:var(--frost-dim);
  }}
  .meta b {{ color:var(--frost); font-weight:400; }}

  .legend {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:18px; margin:34px 0 0; }}
  .legend div {{ border-top:2px solid var(--works); padding-top:12px; }}
  .legend dt {{ font-weight:700; letter-spacing:.1em; text-transform:uppercase; font-size:14px; }}
  .legend dd {{ margin:4px 0 0; color:var(--frost-dim); font-size:15px; }}

  /* ---------- filters ---------- */
  .filters {{
    position:sticky; top:70px; z-index:10;
    display:flex; flex-wrap:wrap; gap:10px; align-items:center;
    padding:18px 0; background:linear-gradient(var(--ink) 76%,rgba(7,9,12,0));
  }}
  .chip {{
    font-family:inherit; font-size:14px; letter-spacing:.05em; text-transform:uppercase;
    color:var(--frost-dim); background:transparent; cursor:pointer;
    border:1px solid var(--line); border-radius:999px; padding:8px 15px;
    display:inline-flex; align-items:center; gap:9px;
  }}
  .chip .n {{ font-family:"JetBrains Mono",monospace; font-size:12px; color:var(--works); }}
  .chip:hover {{ color:var(--frost); }}
  .chip[aria-pressed="true"] {{ color:var(--ink); background:var(--works); border-color:var(--works); }}
  .chip[aria-pressed="true"] .n {{ color:var(--ink); }}

  /* ---------- card ---------- */
  .card {{
    border:1px solid var(--line); border-radius:var(--r);
    background:var(--slate); margin:22px 0; overflow:hidden;
    scroll-margin-top:120px;
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
    color:var(--works); border:1px solid rgba(95,227,177,.4);
    background:rgba(95,227,177,.1); border-radius:999px; padding:4px 11px;
  }}
  .specs {{ display:flex; flex-wrap:wrap; gap:8px 26px; margin:0; font-family:"JetBrains Mono",monospace; font-size:13px; }}
  .specs dt {{ color:var(--frost-dim); font-size:11px; letter-spacing:.08em; text-transform:uppercase; }}
  .specs dd {{ margin:2px 0 0; color:var(--frost); }}

  .card-body {{ display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1.05fr); gap:0; }}
  .media {{ padding:22px 24px; border-right:1px solid var(--line); }}
  video {{ width:100%; aspect-ratio:16/9; background:#000; border:1px solid var(--line); border-radius:10px; display:block; }}

  .dl {{ display:flex; flex-wrap:wrap; gap:9px; margin-top:16px; }}
  .btn {{
    display:inline-flex; align-items:baseline; gap:8px; text-decoration:none;
    font-size:14px; letter-spacing:.03em;
    color:var(--frost); background:var(--slate-2);
    border:1px solid var(--line); border-radius:9px; padding:9px 14px;
  }}
  .btn span {{ font-family:"JetBrains Mono",monospace; font-size:11px; color:var(--frost-dim); }}
  .btn:hover {{ border-color:var(--works); color:var(--works); }}
  .btn:hover span {{ color:var(--works); }}

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
  .ref:hover img {{ border-color:var(--works); }}
  .ref:hover span {{ color:var(--works); }}

  .prompt {{ display:flex; flex-direction:column; min-width:0; }}
  .prompt-head {{
    display:flex; align-items:center; justify-content:space-between; gap:14px;
    padding:16px 24px; border-bottom:1px solid var(--line);
  }}
  .prompt-head code {{ font-family:"JetBrains Mono",monospace; font-size:13px; color:var(--frost-dim); }}
  .copy {{
    font-family:inherit; font-size:13px; letter-spacing:.04em; cursor:pointer;
    color:var(--frost-dim); background:transparent;
    border:1px solid var(--line); border-radius:8px; padding:6px 12px;
  }}
  .copy:hover {{ color:var(--works); border-color:var(--works); }}
  .prompt-body {{
    margin:0; padding:20px 24px; max-height:540px; overflow:auto;
    font-family:"JetBrains Mono",monospace; font-size:13.5px; line-height:1.72;
    white-space:pre-wrap; word-break:normal; overflow-wrap:break-word;
    color:var(--frost-dim);
  }}
  mark {{ background:rgba(95,227,177,.15); color:var(--frost); border-radius:3px; padding:2px 5px; }}
  mark.gear {{ box-shadow:inset 3px 0 0 var(--works); }}
  mark.clause {{ box-shadow:inset 3px 0 0 var(--works); }}

  footer {{ border-top:1px solid var(--line); padding:40px 0 0; margin-top:60px; color:var(--frost-dim); font-size:15px; }}
  footer a {{ color:var(--works); }}

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
    <a href="{REPO_URL}#readme">Skills</a>
    <a href="https://www.youtube.com/@LoopForge0">YouTube</a>
  </nav>
</div>

<div class="wrap">
  <section class="hero">
    <h1>Fourteen camera shots,<br>and the prompts behind them</h1>
    <p>MiniMax H3 documents <strong>twelve camera motions</strong> and no named shots. A crash zoom, a
       dolly zoom or a snorricam is something you compose out of those motions in a sentence. Every shot
       below rides the same six section Ref2VA scaffold, and the marked sentence is what turns it into a
       named shot.</p>
    <p>Everything is here: the clip, the exact prompt that produced it byte for byte, the character
       reference plates, and the ComfyUI workflow. Nothing has been tidied up for publication.</p>
    <div class="meta">
      <span>developed <b>864&times;480</b> on an <b>RTX 3060</b></span>
      <span>finished <b>1344&times;768</b> on a rented <b>RTX 5090</b></span>
      <span><b>20 steps</b>, turbo off</span>
      <span>seed <b>{SEED}</b></span>
      <span><b>{len(entries)}</b> clips, <b>{total_mb:.0f} MB</b></span>
    </div>
    <dl class="legend">{legend}</dl>
  </section>

  <div class="filters">
    <button class="chip" data-filter="all" aria-pressed="true">all<span class="n">{len(entries)}</span></button>
    {nav}
  </div>

  <main>
{cards}
  </main>

  <footer>
    <p>The two marked passages in each prompt are the <strong>camera and lens</strong> and the
       <strong>camera clause</strong>. They are sliced out of the prompt files in this repository by
       <code>scripts/build_site.py</code>, so what you read here is what actually ran.</p>
    <p>One caveat worth stating: the snorricam clip is <b>864&times;480</b> from the local pass rather than
       native resolution. It was kept because the shot is better.</p>
    <p><a href="{REPO_URL}">github.com/loopforge0/minimaxh3-shots-skills</a> &middot;
       <a href="https://www.youtube.com/@LoopForge0">youtube.com/@LoopForge0</a></p>
  </footer>
</div>

<script>
  // filters
  const chips = document.querySelectorAll('.chip');
  const cards = document.querySelectorAll('.card');
  chips.forEach(c => c.addEventListener('click', () => {{
    chips.forEach(o => o.setAttribute('aria-pressed', String(o === c)));
    const f = c.dataset.filter;
    cards.forEach(card => {{ card.hidden = !(f === 'all' || card.dataset.group === f); }});
  }}));

  // copy prompt
  document.querySelectorAll('.copy').forEach(b => b.addEventListener('click', async () => {{
    const el = document.getElementById(b.dataset.target);
    try {{
      await navigator.clipboard.writeText(el.innerText);
      const was = b.textContent; b.textContent = 'Copied';
      setTimeout(() => {{ b.textContent = was; }}, 1400);
    }} catch (e) {{ b.textContent = 'Press Ctrl C'; }}
  }}));

  // only one clip plays at a time
  document.querySelectorAll('video').forEach(v => v.addEventListener('play', () => {{
    document.querySelectorAll('video').forEach(o => {{ if (o !== v) o.pause(); }});
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

    # the page links prompts/ directly, so Pages needs a copy inside docs/
    dst = DOCS / "prompts"
    dst.mkdir(exist_ok=True)
    for e in entries:
        shutil.copy2(PROMPTS / e["promptFile"], dst / e["promptFile"])

    total = sum(e["clipBytes"] for e in entries) / 1e6
    print(f"\n{len(entries)} shots -> docs/index.html  ({total:.0f} MB of clips)")


if __name__ == "__main__":
    main()
