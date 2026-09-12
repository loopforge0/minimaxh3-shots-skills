# Dutch Angle

**Status:** verified. **The cleanest pass in the library, and it uses one primitive.**
**Effect:** the camera rolls into a canted frame and holds there. The horizon is tilted and the subject sits
off-axis.
**Primitives:** `Roll Counterclockwise` (or clockwise). That is all.
**Reference:** *The Third Man*, and every unsettled frame since.

## Shot line

> The camera rolls {ROLL_DIRECTION} into a canted dutch angle and holds there, the horizon tilted,
> {SUBJECT} off-axis.

## Why it is here

It is the counter-example to the instinct that a better shot needs more instruction. One primitive, no
amplitude, no speed, no framing override, and it passed first time with the note *"this is actually fine"*.
**Primitive count is not a quality lever.** `../references/camera-grammar.md`.

## Give it something to be tilted against

The roll is only visible against a horizon or a vertical. In a scene with no strong vertical structure a
dutch angle reads as a slightly crooked frame rather than a deliberate cant. Conifers, doorframes, a
skyline, a horizon line — anything with an axis.

## Gotchas

- ⚠️ **The measurement cannot see this shot.** Every background-tracking step was flagged weak (21/21),
  because a roll gives a feature tracker almost nothing to chain. Unmeasurable here does not mean it failed.
  Judge by eye. `../../h3-shot-iteration/references/judging.md`.
- `Roll` is around the lens axis. If you want the *world* to tilt while the camera stays level, that is not
  this shot and there is no primitive for it.
- This is a **hold**, not a move. Say *"and holds there"* or the frame keeps rotating.

## Machine-readable

```json
{
  "id": "C-09",
  "slug": "dutch-angle",
  "name": "dutch angle",
  "status": "verified",
  "motion": "stationary",
  "length": 124,
  "framing": "{MEDIUM_FRAMING}",
  "shot_line": "The camera rolls {ROLL_DIRECTION} into a canted dutch angle and holds there, the horizon tilted, {SUBJECT} off-axis.",
  "extra_slots": {},
  "direction_slot": "ROLL_DIRECTION (default counterclockwise; clockwise is documented but untested here)"
}
```

## Prompt as it ran

`prompts/C-09_dutch-angle.txt`
