# Slow Pan Reveal

**Status:** verified. Part 2.
**Effect:** the camera stays in one place and turns slowly across the location, and finds the person at the
end of the turn.
**Primitives:** `Pan Right` + `at slow speed`, with the camera body held in place.

## Shot line

> A wide shot looks across {ENVIRONMENT_ELEMENTS} {PLACE}, with no one in view. The camera stays in one place
> and pans right at slow speed across the place, and comes to rest on {SUBJECT} {REVEAL_ACTION}, framing
> {PRONOUN} in a medium shot.

## Framing

Open on the place with **no one in view**. The subject is out of frame to the right, so the pan has something
to find. The shot owns its whole `[Shot 1]` line for that reason: the usual "frames `<Subject 1>`" opening
would put them on screen from the first frame.

## Gotchas

- **Give the subject something to be doing.** A version that ended on her just standing there felt flat. The
  shipped take has her lying sideways across an armchair, scrolling on her phone.
- "Stays in one place" is what keeps this a pan. Part 1 only had `Pan Right` as a whip pan, driven by a
  destination; here the same primitive at slow speed with a stationary camera behaves well.
- Right is the only direction rendered. The subject is placed "at the right" in `{REVEAL_ACTION}` to match.

## Machine-readable

```json
{
  "id": "P2-02",
  "slug": "slow-pan-reveal",
  "name": "slow pan reveal",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "A wide shot looks across {ENVIRONMENT_ELEMENTS} {PLACE}, with {SUBJECT} out of frame to the right",
  "framing_summary": "a wide shot of the place",
  "shot_intro": "custom",
  "shot_line": "A wide shot looks across {ENVIRONMENT_ELEMENTS} {PLACE}, with no one in view. The camera stays in one place and pans right at slow speed across the place, and comes to rest on {SUBJECT} {REVEAL_ACTION}, framing {PRONOUN} in a medium shot.",
  "extra_slots": {
    "REVEAL_ACTION": "where the subject is and what they are doing when the pan finds them, e.g. \"lying sideways across a wide velvet armchair at the right, scrolling on her phone\""
  }
}
```

## Prompt as it ran

`prompts/P2-02_slow-pan-reveal.txt`
