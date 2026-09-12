# Crane Rise (over the head)

**Status:** verified
**Effect:** the camera starts at the subject's feet as they run, then climbs and tips over to look
straight down at them from overhead, holding them centred the whole way.
**Primitives:** `Tracking Shot` + `Pedestal Up` + `Tilt Down`, with `large amplitude at fast speed`

## Shot line

> The camera starts low at ground level beside {SUBJECT} as {PRONOUN_SUBJ} moves, then performs a tracking
> shot with large amplitude at fast speed, pedestalling up and tilting down to follow {PRONOUN} from high
> overhead while {PRONOUN_SUBJ} stays centred and sharp in frame.

## Three primitives, and it is the most complete shot in the library

This is the shot that killed the theory that reliability falls as primitives stack. It composes **three**
and produced the cleanest full move in the set. The rule that replaced it: **complementary primitives
compose well, contradictory primitives fight.** These three describe one coherent move, so they cooperate.
`../references/camera-grammar.md`.

## The subject must actually run

A crane rise over a stationary subject has nothing to track. State **running**, not stillness, and give
the run a rhythm.

## Gotchas

- ⚠️ **This is the shot that taught the frozen-expression lesson.** The first version asked for *"runs
  hard and open-faced, breath clouding"* — a condition, not an arc — and H3 held one rigid open-mouthed
  frame for the entire clip. The reference plate was a closed-mouth smile, so the plate was innocent.
  Rewritten as a transition (*"easing out of hard concentration into open delight"*) it came back correct.
  `../references/performance.md`.
- **State lips closed and jaw relaxed explicitly** on any running shot. Hard exertion plus an unstated
  mouth is how you get the held "O".
- ⚠️ Its soundscape said *"flown on a drone"* and the result carried twice the low-frequency energy of a
  comparable handheld take — plausibly wind rumble rather than rotor, but worth a listen. **Never name the
  rig in an audio slot.** `../references/performance.md`.

## Machine-readable

```json
{
  "id": "C-05",
  "slug": "crane-rise",
  "name": "crane rise over the head",
  "status": "verified",
  "motion": "run",
  "length": 124,
  "framing": "{MEDIUM_FRAMING}",
  "shot_line": "The camera starts low at ground level beside {SUBJECT} as {PRONOUN_SUBJ} moves, then performs a tracking shot with large amplitude at fast speed, pedestalling up and tilting down to follow {PRONOUN} from high overhead while {PRONOUN_SUBJ} stays centred and sharp in frame.",
  "extra_slots": {},
  "performance_note": "Must be an arc, and must state the mouth. e.g. \"runs at a steady rhythm with lips closed and jaw relaxed, chin level, expression easing out of hard concentration into open delight as the camera lifts away\""
}
```

## Prompt as it ran

`prompts/C-05_crane-drone-rise.txt`
