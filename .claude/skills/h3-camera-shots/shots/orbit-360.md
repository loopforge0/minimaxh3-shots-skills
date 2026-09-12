# 360 Orbit

**Status:** verified
**Effect:** the camera sweeps a complete circle around the subject and returns to the front. The subject
stays put; the world rotates behind them.
**Primitives:** `Arc Shot` + `with large amplitude` + `at fast speed`
**Reference:** the hero orbit, from *The Matrix* lobby through every superhero landing since.

## Shot line

> The camera performs an arc shot around {SUBJECT} with large amplitude at fast speed, sweeping a complete
> circle around {PRONOUN} and coming back to the front. {SUBJECT} stays where {PRONOUN_SUBJ} is through
> the sweep. {ORBIT_ACKNOWLEDGE}

## Both modifiers are mandatory here

This is the shot that established rule 1. Without `with large amplitude at fast speed` an arc shot
produces **a small curve, not a circle** — peak travel 72 px/step. With them: **203 px/step**, and a
genuine circle. The shot's identity *is* the completeness of the sweep, which is exactly the case the
modifiers exist for.

Absolute travel measured **98% of frame width** on the verified take.

## Reading the result

⚠️ **Do not judge this shot on cumulative pan.** Pan cancels over a circle, so a perfect orbit can
measure near zero, and one metric called the verified take weak for exactly that reason. Judge it on
the stills: faces camera → **back to camera with the skyline behind** → faces camera again.

## Gotchas

- **Give the subject natural motion.** The identical camera clause on a subject told to hold *"one
  single pose completely rigid"* collapsed camera travel from 108% to **22%**. An impossible
  instruction costs you the camera move. `../references/performance.md`.
- Letting the subject turn their head slightly to keep the camera in view reads as intentional and costs
  nothing — the life clause did not reduce the travel.
- ⚠️ The end background does not exactly match the start, so the return is approximate rather than a
  true loop. Do not build a seamless loop on it without checking.

## Machine-readable

```json
{
  "id": "C-04",
  "slug": "orbit-360",
  "name": "360 orbit",
  "status": "verified",
  "motion": "stationary",
  "length": 124,
  "framing": "{MEDIUM_FRAMING}",
  "shot_line": "The camera performs an arc shot around {SUBJECT} with large amplitude at fast speed, sweeping a complete circle around {PRONOUN} and coming back to the front. {SUBJECT} stays where {PRONOUN_SUBJ} is through the sweep. {ORBIT_ACKNOWLEDGE}",
  "extra_slots": {}
}
```

## Prompt as it ran

`prompts/C-04_360-orbit.txt`
