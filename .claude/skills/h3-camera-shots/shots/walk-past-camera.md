# Walk Past Camera

**Status:** verified on two renders (two seeds, two scenes). Part 2.
**Effect:** the subject walks straight at the lens, passes right beside it, and the camera pans to follow them
walking away.
**Primitives:** `Pan Right` + `at fast speed`. The subject's walk does most of the work.

## Shot line

> {PRONOUN_SUBJ_CAP} walks straight toward the lens, growing from a full figure to a close-up, and passes right
> beside the camera; the camera pans right at fast speed as {PRONOUN_SUBJ} goes by, and follows {PRONOUN} from
> behind as {PRONOUN_SUBJ} walks on into the distance, {POSSESSIVE} back to the camera.

## Framing

Open **wide**, with the subject a full figure. They grow to a close-up as they reach the lens, so the shot
needs the distance.

## Gotchas

- **Keep the walk steady and give the face one change**, e.g. *"walks with a calm, set expression that breaks
  into a small smile as she passes the lens"*.
- Right is the only pan direction rendered.

## Machine-readable

```json
{
  "id": "P2-12",
  "slug": "walk-past-camera",
  "name": "walk-past shot",
  "status": "verified",
  "part": 2,
  "motion": "walk",
  "length": 124,
  "framing": "{WIDE_FRAMING}",
  "shot_line": "{PRONOUN_SUBJ_CAP} walks straight toward the lens, growing from a full figure to a close-up, and passes right beside the camera; the camera pans right at fast speed as {PRONOUN_SUBJ} goes by, and follows {PRONOUN} from behind as {PRONOUN_SUBJ} walks on into the distance, {POSSESSIVE} back to the camera.",
  "extra_slots": {},
  "performance_note": "Keep the walk steady and give the face one change, e.g. \"walks with a calm, set expression that breaks into a small smile as she passes the lens\"."
}
```

## Prompt as it ran

`prompts/P2-12_walk-past-camera.txt`
