# Eyes In

**Status:** verified
**Effect:** the camera travels toward the face and keeps going past it, until one eye fills the frame edge to
edge and the iris is the whole image.
**Primitives:** `Push In` + `with large amplitude` + `at slow speed`
⚠️ **No canonical film shot.** A preset label; judge against described behaviour.

## Shot line

> The camera pushes in with large amplitude at slow speed toward {FACE} and keeps going past it until
> {DETAIL} fills the entire frame edge to edge.

## "And keeps going past it" is the whole shot

The first version stopped at a face close-up. The destination has to be stated **beyond** the face, as an
anatomical detail rather than a degree of closeness. *"Until her right eye fills the entire frame edge to
edge"* is a place the camera can arrive at. *"A very tight close-up"* is not.

Naming which eye helps. It gives the move a target instead of a centre.

## The exception it created

This shot set **no framing override** and **opened wider than the default anyway**, which contradicts the
rule that you have to write the wide opening yourself. A sufficiently extreme destination may widen the
opening by itself.

⚠️ n=1, unresolved. Do not rely on it. `../references/framing.md`.

## Gotchas

- ⚠️ **The numbers are nonsense on this shot.** Reported subject 1.19x and background 17.78x — by the last
  frame there is no face in shot, only an iris, so face-scale tracking has nothing to measure. A 9x spread
  between metrics is the flag. Judge by eye.
- `at slow speed` is deliberate. This shot is a slow inexorable approach; `at fast speed` turns it into a
  crash zoom that overshoots.
- Pair it with a tightening expression that resolves *before* the eye fills frame — pupils contracting, one
  blink, then held. Once the eye is the frame there is no face left to act with.

## Machine-readable

```json
{
  "id": "C-10",
  "slug": "eyes-in",
  "name": "eyes in",
  "status": "verified",
  "motion": "stationary",
  "length": 124,
  "framing": "{MEDIUM_FRAMING}",
  "shot_line": "The camera pushes in with large amplitude at slow speed toward {FACE} and keeps going past it until {DETAIL} fills the entire frame edge to edge.",
  "extra_slots": {},
  "subject_warning": "For an inanimate subject there is no eye to land on. Set DETAIL to a structural feature that can fill the frame, e.g. \"the maker's mark stamped into its base\", \"a single rivet head\"."
}
```

## Prompt as it ran

`prompts/C-10_eyes-in.txt`
