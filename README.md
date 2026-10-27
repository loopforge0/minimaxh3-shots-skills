# MiniMax H3 camera shot skills

Agent skills for writing **named camera shots** in MiniMax H3 prompts. Part 1: dolly zoom, crash zoom, whip
pan, snorricam, 360 orbit, crane rise, aerial pullback, handheld, yo-yo zoom, dutch angle, eyes-in, rack focus,
split screen, super dolly in. Part 2: POV, slow pan reveal, time-lapse, fisheye, cut-away montage, crash zoom
out, hero spin, rooftop swing, FPV drone, overhead swing, walk past camera, crane down, jib up, low-angle hero,
tilt up reveal. Plus a post-render fix for crash zooms.

H3 has **twelve documented camera primitives and no named compound shots.** There is no "Dolly Zoom" button.
Every film shot has to be composed out of the twelve, in a sentence, and most of the ways of doing that do
not work. This repository is twenty-nine that do, and the reasons.

### 📺 [See the shots, with their prompts →](https://loopforge.cc/projects/h3-camera-shots/)

The gallery plays every clip next to the exact prompt that produced it, with the camera and lens phrase and
the camera clause marked, and download links for the clip, the prompt, the character reference plates and
the ComfyUI workflow.

**The videos**

- Part 1, fourteen shots: https://www.youtube.com/watch?v=GCdKh_KaQVs
- Part 2 video: (link added on publish)


## Install

```bash
git clone https://github.com/loopforge0/minimaxh3-shots-skills
cd minimaxh3-shots-skills
python scripts/fetch_upstream_guides.py      # pulls MiniMax's own guide, which these build on
```

`scripts/snap.py` also needs `ffmpeg` and `ffprobe` on your PATH. Nothing else does.

The skills live in `.claude/skills/`, so an agent working in this directory finds them automatically. To
have them everywhere, copy both directories into your user skills folder:

```bash
cp -r .claude/skills/h3-camera-shots  ~/.claude/skills/
cp -r .claude/skills/h3-shot-iteration ~/.claude/skills/
```

Then just ask for a shot: *"write me a snorricam prompt for this character on a city street"*.

## Write a prompt without an agent

```bash
python scripts/build_prompt.py --list                          # the shots
cp scripts/scene.example.json my-scene.json                    # then edit every value
python scripts/build_prompt.py snorricam --slots --scene my-scene.json   # what this shot needs
python scripts/build_prompt.py snorricam --scene my-scene.json
```

The shot supplies the camera clause, the opening framing it requires, and the subject action. You supply the
subject, the environment, the performance and the audio. Standard library Python, no dependencies.

**Your subject does not have to be a person.** Set `"SUBJECT_KIND"` to `person`, `animal`, `bird` or `object`
and the framing, pronouns, identity lock and the anti-frozen clause all change with it. For an inanimate
subject that last one inverts: a person must never be told to hold still, but an object genuinely is still, so
the motion moves to the world around it. `.claude/skills/h3-camera-shots/references/subjects.md`.

**Direction is a slot where it is a free axis.** `PAN_DIRECTION` for the whip pan, `ROLL_DIRECTION` for the
dutch angle, and the dolly zoom ships as two separate recipes because its two directions are different shots.
`.claude/skills/h3-camera-shots/references/direction.md`.

## The shots

Full index with what a viewer actually sees:
[`.claude/skills/h3-camera-shots/shots/INDEX.md`](.claude/skills/h3-camera-shots/shots/INDEX.md)

| | |
|---|---|
| **Passed first time** | dutch angle, rack focus, split screen (layout), aerial pullback |
| **Took two or three iterations** | super dolly in, 360 orbit, crane rise, handheld, eyes-in, snorricam |
| **Still imperfect, and the file says how** | yo-yo zoom (proportions), split screen (timing), dolly zoom (the subject lock) |
| **Cannot be done** | bullet time. [The file explains why, and what the attempt cost](.claude/skills/h3-camera-shots/shots/bullet-time.md) |

**Part 2** added fifteen, several from viewer requests:

| | |
|---|---|
| **Camera moves** | slow pan reveal, crash zoom out, hero spin, FPV drone, overhead swing, walk past camera, crane down, jib up, low-angle hero, tilt up reveal |
| **Effects and edits** | POV, time-lapse, fisheye, cut-away montage, rooftop swing |
| **Took several rounds, and the file says what failed** | POV, cut-away montage, overhead swing, rooftop swing, fisheye |
| **Verified on one render only** | crane down, jib up |
| **Still imperfect** | fisheye (no true circular bulge), low-angle hero (the angle comes out mild) |
| **Need `snap.py` after the render** | crash zoom in, crash zoom out |

## Crash zoom fix

H3 picks its own pace for a zoom. The crash zoom prompts ask for the change to take about 200 ms, or "two or
three frames, as abrupt as a cut", and at 1344x768 the render takes **about 2.6 s** for the zoom in and **about
1.7 s** for the zoom out. No wording tried fixed that, so the fix runs after the render:

```bash
python scripts/snap.py crash-zoom-in_raw.mp4 crash-zoom-in.mp4
# zoom found at frames 42-104 (1.75-4.33 s, 62 frames), sped up 20.7x to 3 frames
```

`snap.py` compares every frame with the first and the last to find where the zoom starts and lands, then
speeds that stretch up to three frames. The audio over the same stretch is sped up by the same factor with its
pitch kept, so sound stays in sync and the clip just gets shorter. Standard library Python plus ffmpeg; it does
not touch your prompt. It expects one hold, one zoom, one hold: a clip with two zooms, a cut, or a camera that
keeps moving after the zoom will get the wrong window, so check the frames it reports.
[`crash-zoom-in.md`](.claude/skills/h3-camera-shots/shots/crash-zoom-in.md) and
[`crash-zoom-out.md`](.claude/skills/h3-camera-shots/shots/crash-zoom-out.md) have the details.

**"Verified" means a person watched it and said it reads as the intended shot.** Not that a metric agreed.

## The findings, in short

The things that would have saved the most time, if someone had written them down first.

**Settings that decide whether the move happens at all.** 20 steps — a 4-step turbo render suppresses camera
motion almost entirely regardless of the prompt. 124 frames minimum, because H3's trained range starts there.
192 for anything with three phases.

**A background reference plate halves the camera move.** Controlled A/B, identical prompt and seed: one
character plate gives a 0.47x background transform, adding a background plate gives 0.81x. It buys a locked
environment and costs you half the shot. Extra *character* plates are free.

**Camera motion is TYPE + AMPLITUDE + SPEED**, and the modifiers do not stack. `with large amplitude at fast
speed` took a 360 orbit from a small curve to a genuine circle. `with small amplitude` is inert on a single
primitive — 1.47x against a 1.53x control. Combining large and fast saturates rather than adding.

**Open at whichever end of the range the subject is largest.** A shot that must end tight has to open wide, or
it has nowhere to travel. One waist-up default was correct for an aerial pullback and fatal for a super dolly
in, in the same scene on the same day.

**Lenses and camera bodies do almost nothing.** Tested properly: Cooke S4 50mm, Petzval 8mm and Zeiss 75mm
against no gear at all, one variable, same seed. An 8mm rendered pixel-for-pixel identical framing to a 50mm.
Gear only matters when it names something that would be **in the scene** — naming a "Snorricam body rig"
rendered the rig in frame.

**You cannot place events in time.** Two prompts asking for reveals at 3.0s and 4.0s both delivered 2.46s. H3
picks a window, packs the described action into it, and pads the rest. State the sequence; cut the timing in an
editor.

**An impossible instruction costs you the rest of the shot.** Same camera clause, same subject, same rooftop:
natural motion gave 98-108% of frame width in camera travel, and *"holds one single pose completely rigid"*
gave 22%.

**The twelve primitives are an interface, not a limit.** A rack focus landed with no focus primitive in the
vocabulary. A three-panel split screen landed with no layout primitive and no timed-event primitive. Treat
"not in the twelve" as untested, never as impossible.

**Some of the vocabulary is untested, and the file says which.** After Part 2, one of the twelve primitives
has no render behind it at all here: `Truck`, in either direction. Part 2 filled in `POV`, `Tilt Up` and
`Pedestal Down`. Absence means nobody tried it, never that it does not work.

**And a measurement will mis-describe a shot.** Four of this project's most confident written conclusions were
overturned by watching the clips, including one recorded as the headline finding. A metric called a crane rise
a pull-out, called a perfect orbit weak because pan cancels over a circle, and called a rack focus absent
because the subject was not centred. Run metrics privately as a sanity check and never let one outrank your
eyes. [`judging.md`](.claude/skills/h3-shot-iteration/references/judging.md)

## Layout

```
.claude/skills/
  h3-camera-shots/           writing the prompt
    SKILL.md
    shots/                   30 recipes + the one that cannot be done
    references/              scaffold, camera grammar, framing, performance, gear,
                             subjects, direction, settings, upstream
  h3-shot-iteration/         diagnosing a generation that came back wrong
    SKILL.md
    references/              failure modes, conditioning A/B, judging
prompts/                     the exact 33 prompts that ran, byte for byte (P2- for Part 2)
scripts/
  build_prompt.py            your scene + a shot -> a complete prompt
  snap.py                    ramps a rendered crash zoom down to three frames (needs ffmpeg)
  fetch_upstream_guides.py   pulls MiniMax's own guide into upstream/
  verify_refs.mjs            catches a ComfyUI trap that silently discards reference images
  scene.example.json         a worked scene to copy
```

## This builds on MiniMax's own documentation

It does not replace it, and it will go wrong if you skip it. Section names, section order, reference-label
rules and the camera vocabulary all belong upstream:

- [`h3-prompt-writing`](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/.claude/skills/h3-prompt-writing/SKILL.md)
  — MiniMax's own skill, covering all five input modes
- Its `references/base-en.txt` (§4.3 is the camera vocabulary) and `references/ref-en.txt` (the six-section
  Ref2VA format every shot here uses)

`scripts/fetch_upstream_guides.py` pulls both. **If the upstream vocabulary ever disagrees with this
library's copy, upstream wins** and the copy here is stale.

This repository's scope is narrow on purpose: which primitives to compose for a named shot, what framing that
shot needs, how it fails, and which of the available knobs turn out to do nothing.

## Caveats

- **All human subjects.** Part 1 was developed on four *human* character plates across five locations; Part 2
  used a wider cast and more locations, still all human. The `animal`, `bird` and `object` vocabularies are
  reasoned from the same findings, not measured. In Part 1, portability to a different *person* was tested for
  exactly one shot (the dolly zoom), and that test found the recipe ports its background and loses its subject
  lock. In Part 2, seven shots were rendered on two different people; the rest on one.
- **One direction per shot.** Each recipe writes the direction that was rendered. The mirrors are documented
  primitives with no render behind them here.
- **Sample sizes are small and are stated.** Several findings are n=1 or n=2 and say so.
- **Quantisation is uncontrolled.** Development ran on a pruned int8 UNET with an NVFP4 text encoder;
  publication renders used higher precision. How far a shot moves between quants is not characterised.
- **Some findings here replaced an earlier finding that was wrong.** The retractions are written down rather
  than deleted, because the wrong version is usually the more useful half to read.

## Licence

MIT, for the files in this repository. `upstream/` holds MiniMax's files under MiniMax's terms and is not
covered by it.
