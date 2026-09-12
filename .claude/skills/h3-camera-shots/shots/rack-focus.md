# Rack Focus

**Status:** verified, clean and monotonic first time
**Effect:** the camera does not move. Focus travels from a near subject to a far one; the near face falls into
blur exactly as the far pair resolves.
**Primitives:** `Static Shot`, and then **no primitive at all** — there is no focus primitive among the twelve.

## Shot line

> The camera holds a static shot. {SUBJECT} sits close to camera in sharp focus while {SUBJECT_2} and
> {SUBJECT_3} {FAR_ACTION} far behind {PRONOUN}, soft and unfocused. The focus then racks from {FACE} to
> the two of them, and {SUBJECT} falls into soft blur exactly as they resolve sharply.

## The result this shot exists to prove

**There is no focus primitive in H3's documented vocabulary, and the shot lands anyway.** Near-to-far
sharpness ratio through the clip:

```
2.88 2.81 2.70 2.62 2.50 2.37 2.03 1.65 1.22 0.88 0.56 0.46 0.41 0.40 0.40 0.40
```

2.88 → 0.40, crossing 1.0 smoothly and monotonically, ending about 2.5x softer than the pair behind.

⭐ With the split screen and the named-dolly-zoom result, that is three independent findings pointing the same
way: **the documented vocabulary is an interface, not the limit of the model.** Treat "not in the twelve" as
untested, never as impossible. `../references/camera-grammar.md`.

## Framing is mandatory here

The shot needs **two depth planes visible at once**, so the default waist-up physically cannot work — there is
no far plane in it. Override to a **medium-wide holding two distinct depth planes**, and say so in those terms.

## Three plates

Three character reference plates, one per subject. Extra character plates cost no camera motion. Wire them in
order; `<Picture N>` is positional.

## Gotchas

- **Give the far plane something to be doing.** Two people talking and laughing quietly together is a reason
  for focus to travel. Two people standing still is not, and an early version failed partly for having no real
  background subject.
- **Motivate the rack with a look.** The near subject turning her head is what makes the focus pull read as
  intentional rather than as a lens error.
- ⚠️ A generic focus metric reported *"crossover: NO"* on the verified take, because it samples a fixed centre
  band as the subject and this shot puts the subject right of frame. Pick the measurement region to match the
  shot, or judge by eye. `../../h3-shot-iteration/references/judging.md`.

## Machine-readable

```json
{
  "id": "D-03",
  "slug": "rack-focus",
  "name": "rack focus",
  "status": "verified",
  "motion": "stationary",
  "length": 124,
  "subjects": 3,
  "framing": "A medium-wide shot holds two distinct depth planes at once: {SUBJECT} close to camera and {ENVIRONMENT} opening out well behind {PRONOUN}",
  "framing_summary": "a medium-wide shot holding two depth planes",
  "shot_intro": "sentence",
  "shot_line": "The camera holds a static shot. {SUBJECT} sits close to camera in sharp focus while {SUBJECT_2} and {SUBJECT_3} {FAR_ACTION} far behind {PRONOUN}, soft and unfocused. The focus then racks from {FACE} to the two of them, and {SUBJECT} falls into soft blur exactly as they resolve sharply.",
  "extra_slots": {
    "SUBJECT_2_DEFINITION": "itemised description of the second subject, bound to <Picture 2>",
    "SUBJECT_3_DEFINITION": "itemised description of the third subject, bound to <Picture 3>"
  },
  "subject_warning": "The verified take motivated the rack with the near subject turning to look. An inanimate near subject has no such cue, so give the far plane the motivation instead: movement, a light coming on, something arriving."
}
```

## Prompt as it ran

`prompts/D-03_rack-focus.txt`
