# Dolly Zoom, telephoto direction

**Status:** rendered and measured, **on weaker evidence than the wide direction.** Read the caveat below.
**Effect:** the subject stays exactly the same size and position in frame while the world behind them
**flattens and looms closer**, compressing into the frame.
**Primitives:** `Pull Out` + `Zoom In`, at exactly cancelling rates.
**Reference:** the *Vertigo* bell-tower stairwell. This is the direction most people picture.

The mirror of [`dolly-zoom`](dolly-zoom.md), which pushes in and zooms out so the background *spreads apart*
instead. Everything in that file about the shot needing **both** halves, the framing exception, the textured
scene and the unsolved subject lock applies here unchanged. Read it first.

## Shot line

> Throughout the entire shot {SUBJECT}'s size and position in frame stay exactly constant: {PRONOUN_SUBJ} is
> framed identically in the last frame as in the first, neither closer nor further away, and never drifts
> from the centre of frame. {FACE_CAMERA} {ROOTED} The camera pulls out while simultaneously zooming in at
> exactly the matching rate, so that the size of {SUBJECT} in frame is cancelled out entirely and does not
> change, while {ENVIRONMENT_ELEMENTS} behind {PRONOUN} flatten, grow, and compress closer together as the
> lens's focal length changes. Only the background transforms.

## ⚠️ Why this one is weaker

Both directions were rendered and measured in the same session, and the telephoto arm produced a background
transform of **1.39x** with correct compression. But that session ran with the reference image being
**silently discarded** by a nested ComfyUI key, so both arms were effectively text-only, with no identity
plate attached.

The wide direction has since been re-rendered many times with a plate connected. **This one has not.** The
recipe is sound on the physics and the measurement, and it has never been validated in the shipping
configuration.

## One thing this direction got right that is worth knowing

Its result clause accidentally described the **wide** behaviour while its verbs asked for telephoto, and the
**verbs won** — the background came back at 1.39x with correct compression. That is the evidence behind a
general rule: **the primitive verbs outrank the result clause.** Get the verb pair right first; the result
clause reinforces, it does not override. `../references/camera-grammar.md`.

## Machine-readable

```json
{
  "id": "v5gear",
  "slug": "dolly-zoom-telephoto",
  "name": "dolly zoom, telephoto direction",
  "status": "rendered-weak-evidence",
  "motion": "stationary",
  "length": 124,
  "framing": "{MEDIUM_FRAMING}",
  "shot_line": "Throughout the entire shot {SUBJECT}'s size and position in frame stay exactly constant: {PRONOUN_SUBJ} is framed identically in the last frame as in the first, neither closer nor further away, and never drifts from the centre of frame. {FACE_CAMERA} {ROOTED} The camera pulls out while simultaneously zooming in at exactly the matching rate, so that the size of {SUBJECT} in frame is cancelled out entirely and does not change, while {ENVIRONMENT_ELEMENTS} behind {PRONOUN} flatten, grow, and compress closer together as the lens's focal length changes. Only the background transforms.",
  "extra_slots": {},
  "framing_note": "Open where it ends. Do NOT open wide.",
  "scene_warning": "Use a scene with trackable structure. This direction has never been validated with an identity plate attached, so treat the first render as a test."
}
```
