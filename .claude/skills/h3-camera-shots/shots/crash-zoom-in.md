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
  expect the proportions to be the model's. `../references/performance.md`.
- The audio is where this shot is won or lost. A single-frame impact at the landing beats a gradual
  swell, and the ambience should cut from open to tight in one frame rather than crossfading.

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
