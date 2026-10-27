# The exact prompts

Thirty-three prompts, copied byte for byte from what was actually sent to the model rather than tidied up
afterwards: seventeen from Part 1 and sixteen from Part 2 (`P2-` prefix). These are the renders the shot
recipes were written from.

## ⚠️ These are not templates

**Every one of them is welded to one specific character set and one specific set of locations** — a
ginger-haired woman on an arctic coastline, a woman on a warm rooftop deck, a snowy pine forest. You
cannot usefully swap your own subject in by find-and-replace, because the framing, the foreground, the
soundscape and the performance arc were all written for that scene.

**To write a prompt for your own subject and location:**

```bash
cp scripts/scene.example.json my-scene.json     # then edit every value
python scripts/build_prompt.py snorricam --slots
python scripts/build_prompt.py snorricam --scene my-scene.json
```

That takes the shot's camera clause, framing requirement and subject action from
`.claude/skills/h3-camera-shots/shots/`, and everything else from your scene file.

**These files are here as evidence.** They are what the claims in the shot recipes rest on, so anyone can
check that a measurement came from the prompt it is attributed to. Read them to see how a finished one
reads; do not start from them.

## What is here

### Part 1

Every one ran at **1344x768, 20 steps, `res_multistep` / `simple`, turbo LoRA off, seed 552013742**, on
`MiniMaxH3ReferenceToVideo` with `ref_image_size: max` and **no background plate**.

| ID | Shot | Frames | Reference wiring |
|---|---|---|---|
| `C-01` | Crash Zoom In | 124 | `<Picture 1>` amber |
| `C-01b` | Crash Zoom In, rewritten as hold-then-snap | 124 | `<Picture 1>` amber |
| `C-02` | Whip Pan | 124 | `<Picture 1>` amber / `<Picture 2>` kate |
| `C-03` | Super Dolly In | 124 | `<Picture 1>` kate |
| `C-04` | 360 Orbit | 124 | `<Picture 1>` sofia |
| `C-05` | Crane Rise | 124 | `<Picture 1>` allie |
| `C-06` | Aerial Pullback | 124 | `<Picture 1>` kate |
| `C-07` | Handheld | 124 | `<Picture 1>` amber |
| `C-08` | Yo-Yo Zoom | **192** | `<Picture 1>` sofia |
| `C-09` | Dutch Angle | 124 | `<Picture 1>` kate |
| `C-10` | Eyes In | 124 | `<Picture 1>` amber |
| `D-01` | Snorricam | 124 | `<Picture 1>` allie |
| `D-03` | Rack Focus | 124 | `<Picture 1>` sofia / `<Picture 2>` allie / `<Picture 3>` amber |
| `D-04` | Multi-Panel Split Screen | **192** | `<Picture 1>` amber |
| `X-01` | Dolly Zoom, portability test | 124 | `<Picture 1>` sofia |
| `X-01b` | Dolly Zoom, every invariant clause stacked | 124 | `<Picture 1>` sofia |
| `K-06n` | Dolly Zoom, the base recipe on a concert stage | 124 | `<Picture 1>` amber |

### Part 2

Every one ran at **1344x768, 20 steps, turbo LoRA off**, on `MiniMaxH3ReferenceToVideo` with **one character
plate** wired as `<Picture 1>` and **no background plate**. Seed 7 unless stated. The `P2-` number is the order
the shots appear in the Part 2 video.

Part 2 prompts are written more plainly than Part 1's: no gear line, which Part 1 found cosmetic, and a short
subject definition, sometimes just *"the person in `<Picture 1>`"*. They use a wider cast of characters and
locations than Part 1.

| ID | Shot | Frames | Notes |
|---|---|---|---|
| `P2-01` | POV shot | **192** | The called name is a dialogue line spoken by the unseen viewer |
| `P2-02` | Slow pan reveal | 124 | |
| `P2-03` | Time-lapse crowd | 124 | |
| `P2-04` | Fisheye close-up | 124 | **seed 11** |
| `P2-05` | Cut-away montage | 124 | The seatbelt insert (`[Shot 3]`) was shortened by hand |
| `P2-06` | Crash zoom in, Part 2 wording | 124 | Shipped after `scripts/snap.py`: zoom at frames 42-104, ramped to 3 frames |
| `P2-07` | Crash zoom out | 124 | Shipped after `scripts/snap.py`: zoom at frames 71-112, ramped to 3 frames |
| `P2-08` | Hero spin | 124 | |
| `P2-09` | Rooftop swing | 124 | |
| `P2-10` | FPV drone dive | 124 | |
| `P2-11` | Overhead swing | 124 | |
| `P2-12` | Walk past camera | 124 | |
| `P2-13` | Crane down | 124 | |
| `P2-14` | Jib up | 124 | |
| `P2-15` | Low-angle hero shot | 124 | |
| `P2-16` | Tilt up reveal | 124 | |

The reference images themselves are not published. They are personal character plates, and none of the
findings depend on the specific faces.

## The one thing a prompt cannot tell you

**`<Picture 1>`, `<Picture 2>` and so on are positional.** The number comes from the order the reference
images are wired into the node, not from anything written in the prompt. Read a prompt without knowing the
wiring and `<Picture 2>` is unresolvable, which is why the table above exists.

## The format

All thirty-three use the six-section Ref2VA structure from MiniMax's own guide:

```
subject_definitions:     what each <Subject N> is, and which <Picture N> it comes from
summary:                 one line, with the task type in brackets
retention_analysis:      per subject, what is held identical
detailed_description:    gear and lighting, then the shot itself
overall_soundscape:      diegetic audio
non_diegetic_music:      score, or N/A
```

See `.claude/skills/h3-camera-shots/references/upstream.md` for where that guide lives.

## Reading them critically

A few of these prompts contain instructions that **did not work**, and they are kept exactly as they ran
rather than corrected:

| File | What is wrong with it |
|---|---|
| `D-04_multi-panel-split-screen.txt` | States absolute reveal times (2s, 4s). Those are precisely the instructions H3 ignored — it opened the last panel at 2.46s in two different runs |
| `C-01b_crash-zoom-in-hold-then-snap.txt` | States a 2s hold and a 200ms snap. H3 picks its own window |
| `K-06n_dolly-zoom-k06.txt` | Names a Cooke S4, a prime, on a shot that has to zoom. It was thought to matter and it turns out not to |
| `C-05_crane-drone-rise.txt` | Says "flown on a drone" in the style line. Naming equipment in an audio-adjacent slot is a rule this library now advises against |
| `P2-06_crash-zoom-in.txt`, `P2-07_crash-zoom-out.txt` | Ask for "two or three frames, as abrupt as a cut". H3 took 2.6 s and 1.7 s. The clips only snap because `scripts/snap.py` ramped them afterwards |
| `P2-15_low-angle-hero.txt` | The waist-up opening is why the angle is mild. See `shots/low-angle-hero.md` |

Line endings are LF.

Commands and paths in this file are written from the **repository root**.
