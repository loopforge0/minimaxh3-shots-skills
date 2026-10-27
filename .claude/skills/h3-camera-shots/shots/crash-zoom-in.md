# Crash Zoom In

**Status:** verified
**Effect:** the frame snaps from a wide view to a tight close-up in one violent magnification. The
world does not move, only the focal length does.
**Primitives:** `Zoom In` + `with large amplitude` + `at fast speed`
**Reference:** the 1970s snap zoom; Edgar Wright uses it as punctuation.

## Shot line

> The camera zooms in with large amplitude at fast speed on {FACE}, a sudden violent crash zoom.

## Framing

Open **wide**. The shot ends tight, so the opening is where the range comes from. The verified version
opened on a waist-up medium close-up and still read, which suggests `large amplitude at fast speed` on
a zoom carries itself further than most, but a wider opening gives it more to spend.

## Why it is a zoom and not a push

A crash zoom is flat magnification. Nothing streams past the lens, there is no parallax, the world
just gets bigger. Write `Push In` here and you get a **super dolly in** instead, which is a different
shot. See `super-dolly-in.md`.

## Gotchas

- **The reaction lands with the zoom, not across the shot.** The first version arced the expression
  through the whole clip, which reads as a slow build with a fast camera bolted on. The revised prompt
  moves the reaction to after the landing.
- ⚠️ **You cannot place the snap in time.** The revised prompt asks for two seconds of locked-off
  hold, a 200ms snap, then a hold, and H3 picks its own window regardless. Write the *sequence* and
  expect the proportions to be the model's. `../references/performance.md`. For the length of the
  zoom itself, see the Part 2 section below: ramp it after the render.
- The audio is where this shot is won or lost. A single-frame impact at the landing beats a gradual
  swell, and the ambience should cut from open to tight in one frame rather than crossfading.

## The zoom is never a crash. Ramp it afterwards (Part 2)

Watching the Part 1 take back, the "crash" is not one. The hold-then-snap prompt asks for the zoom to take
about 200 ms, and H3 takes its own time regardless. Part 2 re-ran the shot with the wording that worked best
on `crash-zoom-out.md`, which describes the change as two or three frames, as abrupt as a cut, with the lens
alone moving:

> The camera is locked off on a tripod and holds the wide shot completely still for the first two seconds;
> only the zoom lens changes and the camera body never moves. Between one frame and the next the lens crash
> zooms in to a tight close-up of {FACE}: the whole change takes only two or three frames, as abrupt as a
> cut, with a streak of zoom blur on those few frames only, and nothing shifts against anything else, the
> background simply magnifies flat together with {PRONOUN}. After it lands the close-up is locked and does
> not change.

At 1344x768 the zoom in that render runs from frame 42 to frame 104 at 24 fps: **about 2.6 seconds**. Every
render in either direction took far longer than asked: about 0.9 s at a lower test resolution, and 1.7 to
2.6 s at 1344x768. So the fix moved out of the prompt and into the edit. `scripts/snap.py` finds the zoom in the rendered clip by comparing every frame with the first and last,
and speeds that stretch up to three frames, audio included:

```bash
python scripts/snap.py crash-zoom-in_raw.mp4 crash-zoom-in.mp4
```

```
zoom found at frames 42-104 (1.75-4.33 s, 62 frames), sped up 20.7x to 3 frames
```

The clip goes from 124 frames to 65, about 2.75 s. Needs only Python and ffmpeg, and runs after the render, so
the prompt does not change. The script's docstring lists what it cannot handle (more than one zoom, a cut, a
camera that keeps moving).

The machine-readable block below is still the Part 1 recipe. To build the Part 2 version, override
`SHOT_LINE` in your scene file with the line above, then run `snap.py` on the result.

## Machine-readable

```json
{
  "id": "C-01",
  "slug": "crash-zoom-in",
  "name": "crash zoom in",
  "status": "verified",
  "motion": "stationary",
  "length": 124,
  "framing": "{WIDE_FRAMING} places {SUBJECT} small and complete in frame {PLACE}",
  "framing_summary": "a wide shot",
  "shot_intro": "comma",
  "shot_line": "The camera zooms in with large amplitude at fast speed on {FACE}, a sudden violent crash zoom.",
  "extra_slots": {}
}
```

## Prompts as they ran

| File | What it is |
|---|---|
| `prompts/C-01_crash-zoom-in.txt` | The verified take. Expression arcs across the shot |
| `prompts/C-01b_crash-zoom-in-hold-then-snap.txt` | Rewritten as locked-off hold, snap, locked-off hold, reaction after the landing, single-frame audio impact |
| `prompts/P2-06_crash-zoom-in.txt` | Part 2: "two or three frames, as abrupt as a cut" wording at 1344x768. H3 still took 2.6 s; shipped after `snap.py` |
