# Crane Down

**Status:** verified on one render. Part 2.
**Effect:** the camera starts high above, looking down, then descends and levels out to end at eye level on
the face.
**Primitives:** `Pedestal Down` + `Tilt Up` + `at slow speed`. The reverse of `crane-rise.md`, which is
`Pedestal Up` + `Tilt Down`.

## Shot line

> The camera cranes down at slow speed, pedestalling down and tilting up as it descends, and comes to rest at
> eye level in a medium close-up of {FACE}.

## Framing

Open **high and wide**, looking down on the subject. The shot ends on a medium close-up at eye level, so it
needs both the height and the distance to come down through.

## Gotchas

- The shot line asks for both halves of the move at once, the pedestal down and the tilt up, and names the
  move as a crane.
- One render only (seed 7). Treat a second scene as untested.

## Machine-readable

```json
{
  "id": "P2-13",
  "slug": "crane-down",
  "name": "crane down",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "A high wide shot from well above looks down on {SUBJECT}",
  "framing_summary": "a high wide shot from above",
  "shot_intro": "comma",
  "shot_line": "The camera cranes down at slow speed, pedestalling down and tilting up as it descends, and comes to rest at eye level in a medium close-up of {FACE}.",
  "extra_slots": {}
}
```

## Prompt as it ran

`prompts/P2-13_crane-down.txt`
