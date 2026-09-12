# Whip Pan

**Status:** verified. The fastest camera move in the library.
**Effect:** the camera tears horizontally off one subject and lands on another, everything between
smearing into streaked motion blur.
**Primitives:** `Pan Right` / `Pan Left`, driven by a stated destination rather than by modifiers.

## Shot line

> The camera starts framed on {SUBJECT}, then whip pans {PAN_DIRECTION} away from {PRONOUN} and lands on
> {SUBJECT_2} {PLACE_2}, {ENVIRONMENT_ELEMENTS} between them smearing into streaked horizontal motion blur
> through the middle of the move, the frame settling and resolving sharply on {SUBJECT_2}. The shot ends
> held on {SUBJECT_2}, not on {SUBJECT}.

## The rule this shot exists to demonstrate

**A transition needs a FROM and a TO.** Naming the destination took this shot from 23 px/step to
**218 px/step**, a factor of nine, from the same primitive.

⚠️ **Asking for motion blur does not produce motion blur.** The destination produces the speed and the
speed produces the blur. Request the blur on its own and you get nothing. The blur clause above is
describing what the speed will do; it is not asking for an effect.

## Two subjects, two plates

This shot runs **two character reference plates** and it produced the fastest move in the set, which is
the clearest evidence that extra *character* plates cost nothing. Only a *background* plate costs
motion. Wire them in order, and remember `<Picture N>` is positional.

## Gotchas

- **End on the destination.** State it: *"the shot ends held on `<Subject 2>`, not on `<Subject 1>`"*.
  Without that the frame drifts back.
- Give the first subject something to be caught mid-way through, and the second something to be
  already doing. A whip pan onto a waiting mannequin reads as a mistake.
- Measured peak single-step travel 268 px, cumulative pan 60% of frame width. A whip pan has to
  **spike**, not glide. If the peak step is low the shot has failed even when the total looks right.

## Machine-readable

```json
{
  "id": "C-02",
  "slug": "whip-pan",
  "name": "whip pan",
  "status": "verified",
  "motion": "stationary",
  "length": 124,
  "subjects": 2,
  "framing": "{MEDIUM_FRAMING}",
  "shot_line": "The camera starts framed on {SUBJECT}, then whip pans {PAN_DIRECTION} away from {PRONOUN} and lands on {SUBJECT_2} {PLACE_2}, {ENVIRONMENT_ELEMENTS} between them smearing into streaked horizontal motion blur through the middle of the move, the frame settling and resolving sharply on {SUBJECT_2}. The shot ends held on {SUBJECT_2}, not on {SUBJECT}.",
  "extra_slots": {
    "PLACE_2": "where the second subject is, with its verb, e.g. \"standing further along the shore\", \"perched on the far railing\", \"parked at the end of the row\"",
    "SUBJECT_2_DEFINITION": "itemised description of the second subject, bound to <Picture 2>"
  },
  "direction_slot": "PAN_DIRECTION (default right; left is documented but untested here)"
}
```

## Prompt as it ran

`prompts/C-02_whip-pan.txt`
