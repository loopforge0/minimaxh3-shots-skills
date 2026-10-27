# Jib Up

**Status:** verified on one render. Part 2.
**Effect:** the camera sweeps up and over the subject on a jib, tilting down as it rises, and ends looking down
on them with the place spread out around them.
**Primitives:** a rise with `Tilt Down`, described as one arc at slow speed. "Jib" itself is not one of the
twelve.

## Shot line

> The camera jibs up at slow speed in one sweeping arc, rising from {POSSESSIVE} chest height up and over
> {PRONOUN} while tilting down to keep {PRONOUN} in frame, and ends in a high angle looking down on {PRONOUN}
> with {ENVIRONMENT} spread out around {PRONOUN}.

## Framing

Open on the default **waist-up medium close-up** at chest height. The shot ends high and wide on the place,
so it starts close.

## Gotchas

- `{ENVIRONMENT}` appears in the shot line as well as the summary, so it has to read as a place that can be
  "spread out around" the subject, e.g. *ancient temple ruins in the jungle*.
- Give the face somewhere to go as the camera rises, e.g. *"turns her face up toward the rising camera, her
  expression opening from wariness into awe"*.
- One render only (seed 7). Treat a second scene as untested.
- Compare `crane-rise.md`, which climbs and tips over while tracking a runner, and `aerial-pullback.md`, which
  rises and retreats. The jib stays over a still subject.

## Machine-readable

```json
{
  "id": "P2-14",
  "slug": "jib-up",
  "name": "jib up",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "{MEDIUM_FRAMING}",
  "shot_line": "The camera jibs up at slow speed in one sweeping arc, rising from {POSSESSIVE} chest height up and over {PRONOUN} while tilting down to keep {PRONOUN} in frame, and ends in a high angle looking down on {PRONOUN} with {ENVIRONMENT} spread out around {PRONOUN}.",
  "extra_slots": {},
  "performance_note": "Give the face somewhere to go as the camera rises, e.g. \"turns her face up toward the rising camera, her expression opening from wariness into awe\"."
}
```

## Prompt as it ran

`prompts/P2-14_jib-up.txt`
