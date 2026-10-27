# Time-Lapse Crowd

**Status:** verified. Part 2. An effect more than a camera move.
**Effect:** the subject stands at normal speed in the middle of the frame while crowds, traffic, clouds and
light rush past in time-lapse around them.
**Primitives:** `Static Shot`, locked off. The time-lapse is described, not a primitive.
**Reference:** *Lucy*, in Times Square near the end.

## Shot line

> A static medium-wide shot, locked off on a tripod, frames {SUBJECT} standing still and centred {PLACE}, with
> {ENVIRONMENT_ELEMENTS} around {PRONOUN}. Everything around {PRONOUN} plays as a fast time-lapse: crowds of
> people stream past on both sides as soft blurred streaks, cars and lights race by, clouds rush across the sky
> and the light shifts and flickers as the hours pass. Only {SUBJECT} moves at normal speed, breathing slowly,
> blinking, and turning {POSSESSIVE} head a little, perfectly sharp in the middle of the rushing blur.

## Why it works

The camera never moves, which plays to what H3 does well. The work in the prompt is keeping the **two speeds
apart**: the subject is at normal speed, and only the crowd, the traffic, the sky and the light are in
time-lapse. The subject still breathes, blinks and turns their head, so they are still, not frozen (see
`../references/performance.md`).

## Audio

The shot adds to your soundscape rather than replacing it: whatever the place sounds like, "sped up into a
rushing, washing blur of footsteps, voices and traffic". `build_prompt.py` appends that for you.

## Gotchas

- Pick a place with a lot of things that can move: people, cars, signs, sky. The time-lapse has nothing to
  show in an empty room.

## Machine-readable

```json
{
  "id": "P2-03",
  "slug": "time-lapse",
  "name": "time-lapse crowd",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "A static medium-wide shot",
  "framing_summary": "a static medium-wide shot",
  "summary_action": "standing still at normal speed while the world around rushes past in time-lapse",
  "shot_intro": "custom",
  "shot_line": "A static medium-wide shot, locked off on a tripod, frames {SUBJECT} standing still and centred {PLACE}, with {ENVIRONMENT_ELEMENTS} around {PRONOUN}. Everything around {PRONOUN} plays as a fast time-lapse: crowds of people stream past on both sides as soft blurred streaks, cars and lights race by, clouds rush across the sky and the light shifts and flickers as the hours pass. Only {SUBJECT} moves at normal speed, breathing slowly, blinking, and turning {POSSESSIVE} head a little, perfectly sharp in the middle of the rushing blur.",
  "soundscape": "{SOUNDSCAPE}, sped up into a rushing, washing blur of footsteps, voices and traffic",
  "extra_slots": {},
  "scene_warning": "Needs a busy place: crowds, traffic, signs and sky give the time-lapse something to move."
}
```

## Prompt as it ran

`prompts/P2-03_time-lapse.txt`
