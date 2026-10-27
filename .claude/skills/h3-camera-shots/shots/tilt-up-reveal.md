# Tilt Up Reveal

**Status:** verified on two renders (two seeds, two scenes). Part 2.
**Effect:** the shot opens on the feet; the camera tilts up the body and lands on the face, so the subject is
only revealed at the end.
**Primitives:** `Tilt Up` + `at slow speed`, with the camera held in place.

## Shot line

> The camera stays in one place and tilts up at slow speed, travelling up {POSSESSIVE} legs, body and
> shoulders, and comes to rest on {FACE} in a medium close-up, so {PRONOUN_SUBJ} is only revealed at the end.

## Framing

> A chest-height camera angled down frames only {SUBJECT}'s feet and lower legs, {POSSESSIVE} face out of frame

The camera is at chest height and **angled down**, so the tilt up has a range to travel through. The face must
be out of frame at the start or there is nothing to reveal.

## Gotchas

- "Stays in one place" asks for a tilt with the camera body fixed, the same phrasing `slow-pan-reveal.md` uses
  for its pan.
- A short, plain prompt, and it held on both seeds (7 and 11).

## Machine-readable

```json
{
  "id": "P2-16",
  "slug": "tilt-up-reveal",
  "name": "tilt up reveal",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "A chest-height camera angled down frames only {SUBJECT}'s feet and lower legs, {POSSESSIVE} face out of frame",
  "framing_summary": "a close shot of {POSSESSIVE} feet",
  "shot_intro": "comma",
  "shot_line": "The camera stays in one place and tilts up at slow speed, travelling up {POSSESSIVE} legs, body and shoulders, and comes to rest on {FACE} in a medium close-up, so {PRONOUN_SUBJ} is only revealed at the end.",
  "extra_slots": {}
}
```

## Prompt as it ran

`prompts/P2-16_tilt-up-reveal.txt`
