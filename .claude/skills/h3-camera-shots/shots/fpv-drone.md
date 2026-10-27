# FPV Drone Dive

**Status:** verified on two renders (two seeds, two scenes). Part 2.
**Effect:** a racing drone dives from high above, rolls and banks, skims low over the ground, and pulls up to
a stop in a medium shot of the subject.
**Primitives:** none by name. A described flight path, with `at fast speed` on the dive.
**Reference:** the drone work in *Ambulance*.

## Shot line

> The camera flies like a racing FPV drone: it dives steeply at fast speed, rolls and banks through the air,
> skims low and fast over the ground toward {PRONOUN}, then pulls up and slows to a stop in a medium shot of
> {SUBJECT}, {FACE} sharp in frame.

## Framing

Open **high and wide**, with the subject a tiny figure far below. The dive needs the height to fall through,
and the stop in a medium shot needs the distance to close.

## Notes

- For a move with this many phases (dive, roll, skim, pull-up, stop) it held up across two different seeds
  and scenes.
- "Like a racing FPV drone" is doing real work here. The same idea leaks into other shots: see
  `overhead-swing.md`, where the word "drone" turned a swing into this dive.

## Machine-readable

```json
{
  "id": "P2-10",
  "slug": "fpv-drone",
  "name": "racing-drone dive",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "An aerial wide shot from high above {ENVIRONMENT} looks down on {SUBJECT}, a tiny figure far below",
  "framing_summary": "a high aerial wide shot",
  "shot_intro": "comma",
  "shot_line": "The camera flies like a racing FPV drone: it dives steeply at fast speed, rolls and banks through the air, skims low and fast over the ground toward {PRONOUN}, then pulls up and slows to a stop in a medium shot of {SUBJECT}, {FACE} sharp in frame.",
  "extra_slots": {}
}
```

## Prompt as it ran

`prompts/P2-10_fpv-drone.txt`
