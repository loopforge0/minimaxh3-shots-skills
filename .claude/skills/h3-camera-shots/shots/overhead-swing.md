# Overhead Swing

**Status:** verified on two renders, both on a beach, with a strong caveat about the location. Part 2.
**Effect:** the camera starts a few metres straight above the subject, looking down at them head to toe as
they look up, then swings down in front of them in a quarter-circle at the same distance, ending face-on at
eye level.
**Primitives:** none by name. A described arc that pairs a descent with a `Tilt Up` from pointing down to
pointing level.
**Credit:** a viewer, who found that the word "swing" works in H3.

## Shot line

> The camera swings down in front of {PRONOUN} in a smooth quarter-circle arc at slow speed, keeping the same
> distance from {PRONOUN} the whole way: it travels from straight above {POSSESSIVE} head down to
> {POSSESSIVE} eye level on the side {PRONOUN_SUBJ} is facing, tilting from pointing straight down to pointing
> level as it goes so {FACE} stays centred, and ends face-on to {PRONOUN} in a medium shot with the horizon
> level behind {PRONOUN}. It never passes behind {PRONOUN}, and it does not dive, fly forward or drop straight
> down.

## Be literal. Do not say "drone"

| Wording | What came back |
|---|---|
| Opening on a close-up | Worked, but started lower than intended |
| "High" and "like a drone" | A drone dive: an oblique aerial descending onto her, much like `fpv-drone.md` |
| A few metres straight above, lens pointing down, a quarter-circle at constant distance, and it "does not dive, fly forward or drop straight down" | The swing. Seed 7 starts top-down with her small on the sand looking up and comes down in front of her to face-on, a little higher at the start and wider at the end than asked. Seed 11 is the truest arc but starts on the top of her head and swings round her back before reaching the front |

"Arm's length directly above" was also tried and dropped: on the beach it read as a selfie, her arms reaching
up as if holding the camera.

## Location matters more than the wording

In a pine forest the swing went wrong repeatedly: from overhead the tall trees bent into a fisheye tunnel, and
the camera came round **behind** her and ended behind her head. Adding "down in front of her on the
side she faces, never passing behind her" did not fix it; seed 7 and seed 11 in the forest both still swung
behind her. The same prompt on a beach at sunset came down in front and ended face-on.

**Use an open place: a beach, a field, a plaza.** Tall trees or buildings around the subject are the risk.

## Gotchas

- ⚠️ **Resolution changes the composition.** The forest failure happened at 1344x768 on two different GPUs,
  so it was the output size, not the card, that moved the composition. A take that works at one size may not
  frame the same at another.
- **Start looking up into the lens and let the chin come down with the camera**, e.g. *"looks up into the
  lens with a small, curious smile and lowers her chin to follow the camera down"*.

## Machine-readable

```json
{
  "id": "P2-11",
  "slug": "overhead-swing",
  "name": "swing down from overhead",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "A top-down overhead shot, the camera a few metres directly above {SUBJECT} with its lens pointing straight down, a bird's-eye view of {SUBJECT} from head to toe with the ground around and looking up into the lens",
  "framing_summary": "a top-down overhead shot",
  "shot_intro": "comma",
  "shot_line": "The camera swings down in front of {PRONOUN} in a smooth quarter-circle arc at slow speed, keeping the same distance from {PRONOUN} the whole way: it travels from straight above {POSSESSIVE} head down to {POSSESSIVE} eye level on the side {PRONOUN_SUBJ} is facing, tilting from pointing straight down to pointing level as it goes so {FACE} stays centred, and ends face-on to {PRONOUN} in a medium shot with the horizon level behind {PRONOUN}. It never passes behind {PRONOUN}, and it does not dive, fly forward or drop straight down.",
  "extra_slots": {},
  "scene_warning": "Works best in an open place such as a beach, field or plaza. Tall trees or buildings around the subject can bend into a tunnel from overhead and send the swing round behind them.",
  "performance_note": "Start looking up into the lens and let the chin come down with the camera, e.g. \"looks up into the lens with a small, curious smile and lowers her chin to follow the camera down\"."
}
```

## Prompt as it ran

`prompts/P2-11_overhead-swing.txt`
