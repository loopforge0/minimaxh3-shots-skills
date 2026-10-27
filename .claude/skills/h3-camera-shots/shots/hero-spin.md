# Hero Spin

**Status:** verified. Part 2.
**Effect:** a low camera circles the subject while looking up as they rise from a crouch, the sky wheeling
behind them.
**Primitives:** `Arc Shot` + `with large amplitude` + `at fast speed`, from a low angle.
**Reference:** Michael Bay's hero shot, from *Bad Boys* and *The Rock* on.

## Shot line

> The camera sits low near the ground and performs an arc shot around {PRONOUN} with large amplitude at fast
> speed, circling {PRONOUN} while looking up, as {PRONOUN_SUBJ} slowly rises from the crouch to full height,
> the sky wheeling behind {PRONOUN}.

## Two Part 1 shots combined

This is `orbit-360.md` with the camera dropped to the ground and tipped up. The orbit's modifiers come with
it: `with large amplitude at fast speed` is what turned Part 1's arc from a small curve into a full circle.

The rise from the crouch gives the subject something to do through the orbit. Part 1's orbit lost most of its
travel when the subject was told to hold a pose rigid (`orbit-360.md`).

## Framing

Open on a **low-angle medium shot with the subject crouched**. The crouch is in the framing so the rise has
somewhere to start.

## Gotchas

- Give the face an arc that matches the rise, e.g. *"moves from strain to fierce resolve as she rises"*.

## Machine-readable

```json
{
  "id": "P2-08",
  "slug": "hero-spin",
  "name": "hero spin",
  "status": "verified",
  "part": 2,
  "motion": "stationary",
  "length": 124,
  "framing": "A low-angle medium shot looks up at {SUBJECT}, crouched low",
  "framing_summary": "a low-angle medium shot",
  "shot_intro": "comma",
  "shot_line": "The camera sits low near the ground and performs an arc shot around {PRONOUN} with large amplitude at fast speed, circling {PRONOUN} while looking up, as {PRONOUN_SUBJ} slowly rises from the crouch to full height, the sky wheeling behind {PRONOUN}.",
  "extra_slots": {},
  "performance_note": "Give the face an arc that matches the rise, e.g. \"moves from strain to fierce resolve as she rises\"."
}
```

## Prompt as it ran

`prompts/P2-08_hero-spin.txt`
