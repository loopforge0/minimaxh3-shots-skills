# Aerial Pullback

**Status:** verified
**Effect:** the camera retreats and climbs at once until the subject is a small lone figure far below and
the whole location opens out around them.
**Primitives:** `Pull Out` + `Pedestal Up`, with `large amplitude at fast speed`
**Reference:** the closing pull-back-and-reveal, from *The Shawshank Redemption* onward.

## Shot line

> The camera pulls out with large amplitude at fast speed while pedestalling up, rising and retreating
> until {SUBJECT} is a small lone {SMALL_NOUN} far below and the whole {LOCATION} opens out around
> {PRONOUN}.

## Framing, and why this one is easy

It must **end wide**, so it **opens tight** — which is the default most templates already give you. This
is the shot that passes without any framing work, and its twin (`super-dolly-in.md`) is the one that fails
on the same default. `../references/framing.md`.

Measured: rise **71% of frame height**, subject **0.30x**. The background shrank *with* the subject, which
is what separates a camera retreating from a lens widening.

## Pull Out, not Zoom Out

`Pull Out` moves the camera. `Zoom Out` changes focal length and leaves you with a flat widening in which
the ground never passes underneath. For an aerial the travel is the point.

## Gotchas

- **Give the subject a reaction to the scale**, not just stillness — *"head tipping slowly back to take in
  the scale of the place as it opens around her"*. A figure standing inert at the bottom of a reveal reads
  as a stock shot.
- ⚠️ Its audio was deliberately left untouched when the gear lines were stripped from the library, because
  changing an audio slot can move the picture. If you edit a passing shot's soundscape, treat it as a new
  generation and re-judge it.

## Machine-readable

```json
{
  "id": "C-06",
  "slug": "aerial-pullback",
  "name": "aerial pullback",
  "status": "verified",
  "motion": "stationary",
  "length": 124,
  "framing": "{MEDIUM_FRAMING}",
  "shot_line": "The camera pulls out with large amplitude at fast speed while pedestalling up, rising and retreating until {SUBJECT} is a small lone {SMALL_NOUN} far below and the whole {LOCATION} opens out around {PRONOUN}.",
  "extra_slots": {
    "LOCATION": "the wider place that the reveal opens onto, e.g. \"forest\", \"rooftop\", \"valley\""
  }
}
```

## Prompt as it ran

`prompts/C-06_aerial-pullback.txt`
