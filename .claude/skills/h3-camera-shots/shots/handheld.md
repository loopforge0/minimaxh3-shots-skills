# Handheld

**Status:** verified
**Effect:** the operator runs alongside the subject and the frame lurches and corrects with every stride.
**Primitives:** `Shake Strongly` + `Tracking Shot`, `at fast speed`
**Reference:** *Children of Men*, *Saving Private Ryan* — the camera is a person, not a machine.

## Shot line

> The camera shakes strongly at fast speed while performing a tracking shot alongside {SUBJECT} as
> {PRONOUN_SUBJ} moves, the frame lurching and correcting {STRIDE}.

## Shake has to be earned

Measured frame-to-frame displacement **5.05 / 4.57 px**, against **0.11 px** for a locked dolly. That is a
genuine handheld rather than a suggestion of one.

The first version had the subject standing, and the verdict was that it *needed faster motion to earn the
shaky camera*. A shaking camera on a stationary subject reads as a defect. **Pair `Shake Strongly` with
something that justifies it** — running, a chase, a crowd.

## Gotchas

- `Shake Slightly` is a different shot. It is a nervous lock-off, not a handheld.
- **This shot settled the mouth question.** It kept *"breathing stays audible throughout"* in its soundscape
  and dropped only the two **visual** breathing cues, and came back mouth-closed — disproving the theory
  that the audio line was what held mouths open. The cause is visual cues written as a condition rather
  than a change. `../references/performance.md`.
- Subject scale drifted to 1.46x. A tracking shot is not a locked framing; if you need the subject held at
  constant size, that is `snorricam.md`.

## Machine-readable

```json
{
  "id": "C-07",
  "slug": "handheld",
  "name": "handheld tracking shot",
  "status": "verified",
  "motion": "run",
  "length": 124,
  "framing": "{MEDIUM_FRAMING}",
  "shot_line": "The camera shakes strongly at fast speed while performing a tracking shot alongside {SUBJECT} as {PRONOUN_SUBJ} moves, the frame lurching and correcting {STRIDE}.",
  "extra_slots": {},
  "performance_note": "e.g. \"runs with urgent purpose, lips pressed closed and jaw set, glancing back once over her shoulder without breaking stride\""
}
```

## Prompt as it ran

`prompts/C-07_handheld.txt`
