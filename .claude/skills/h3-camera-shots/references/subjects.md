# Subjects that are not people

**Everything in this library was developed and judged on human subjects** — four character plates across
five locations. A camera move does not care what it is pointed at, but almost every *sentence* in a prompt
does, and a shot line written for a person is full of hair, clothing, faces, weight and breathing.

So the subject-specific wording is a **vocabulary selected by kind**, not hardcoded. Set it in your scene
file:

```json
{ "SUBJECT_KIND": "object" }
```

| Kind | For |
|---|---|
| `person` | **Default, and the only kind with evidence behind it** |
| `animal` | Mammals, reptiles, anything with a face and a gait |
| `bird` | Perching, flying, feathers, quick head movements |
| `object` | Inanimate, any size. A teapot, a car, a lighthouse, a bridge |

⚠️ **The three non-person vocabularies are reasoned from the same rules, not measured.** They are correct
English that respects the library's findings; they have no render behind them. Treat your first generation
on a non-human subject as a test, and judge it rather than trusting it.

## What the kind changes

| Slot | `person` | `object` |
|---|---|---|
| `{PRONOUN}` / `{POSSESSIVE}` | her / her | it / its |
| `{MEDIUM_FRAMING}` | A waist-up medium close-up | A medium close-up |
| `{FACE}` | her face | it |
| `{LIFE}` | breathing softly, hair and clothing stirring, blinking… | completely still and inanimate, with `{AMBIENT}` moving around it |
| `{RETAINED}` | face, identity and clothing | shape, materials and markings |
| `{IDENTITY_LOCK}` | facial structure, features and proportions | shape, proportions, materials, wear and markings |
| `{DETAIL}` | her right eye, the iris filling the view | **no default — you must supply one** |
| `{STRIDE}` | with every stride | constantly |

Every one of them is overridable in your scene file, so if the `animal` vocabulary says "fur" and your
subject is a snake, set `LIFE` yourself. Run `build_prompt.py <shot> --slots --scene your-scene.json` to see
the vocabulary that will actually be used.

## ⭐ The "still must not mean frozen" rule inverts for an object

This is the one finding that genuinely changes shape, and it matters.

For a person, H3 has a strong prior that people in video move, and **fighting that prior is expensive** — a
subject told to hold "one single pose completely rigid" cost about 80% of the camera move in an otherwise
identical prompt. So you never write "completely still"; you write breathing, blinking, hair stirring.

**An object is genuinely inert, and asking it to breathe would be the error.** But you still cannot write a
dead frame, because the same prior wants motion somewhere. So the life clause moves **off the subject and
into the world around it**: rain streaming, grass flattening, cloud racing, dust in a light shaft, a
reflection travelling across a surface.

That is what `{AMBIENT}` is for, and the `object` kind requires it. Give the shot something that moves, or
the model will find its own thing to move and it may well be your subject.

⚠️ **Untested, and it is a real risk.** Whether H3 holds an object properly rigid, or drifts and deforms it
the way it insists on animating a person, is not known. If it warps, the thing to try is stating the rigidity
as an observable result — *"its shape and proportions do not change at any point"* — rather than as a
stylistic instruction.

## How each shot transfers

| Shot | person | animal / bird | object |
|---|---|---|---|
| `crash-zoom-in` | ✅ | ✅ | ✅ lands on the object rather than a face |
| `super-dolly-in` | ✅ | ✅ | ✅ the foreground rule is about the world, not the subject |
| `aerial-pullback` | ✅ | ✅ | ✅ arguably better — a static subject cannot spoil the lock |
| `dolly-zoom` / `-telephoto` | ✅ | ✅ | ✅ **and the subject lock should be easier**, since the library's lock failures were all subjects that drifted |
| `orbit-360` | ✅ | ✅ | ✅ |
| `dutch-angle` | ✅ | ✅ | ✅ |
| `rack-focus` | ✅ | ✅ | ⚠️ the verified take motivated the rack with the near subject turning to look. Give the far plane the motivation instead |
| `split-screen` | ✅ | ✅ | ⚠️ needs one continuous action readable from three angles. A static object gives the panels nothing to sync on |
| `eyes-in` | ✅ | ✅ | ⚠️ **no eye.** Supply `DETAIL` as a structural feature that can fill the frame |
| `yoyo-zoom` | ✅ | ✅ | ✅ |
| `crane-rise` | ✅ | ✅ | ❌ **the subject has to move.** It is a tracking shot |
| `handheld` | ✅ | ✅ | ❌ same. Shake has to be earned by motion |
| `snorricam` | ✅ | ✅ | ❌ the camera is attached to the subject, so the subject must travel under its own power. A vehicle or machine works; a building does not |

The three ❌ shots are not impossible for an object, they just need a *moving* object — a car, a train, a
drone, a boat. `build_prompt.py` prints the warning rather than refusing, because you may well have one.

## Multiple subjects of different kinds

Nothing stops you. `whip-pan` from a person to a parked car, `rack-focus` from a teapot to two people behind
it. Extra **character** plates cost no camera motion, whatever is on them.

The kind vocabulary applies to `<Subject 1>`. For the others, write `PLACE_2`, `FAR_ACTION` and the subject
definitions yourself, and override `RETAINED_2` / `RETAINED_3` if what is preserved differs:

```json
{
  "SUBJECT_KIND": "person",
  "SUBJECT_2_DEFINITION": "the red telephone box in <Picture 2>: chipped enamel paint, a crown moulding above the door, small square panes",
  "RETAINED_2": "shape, materials and markings",
  "PLACE_2": "standing at the far end of the platform"
}
```

## What has not changed

The camera findings are subject-independent and none of them are in question here:

- Steps, frame count, and the background-plate trade.
- `TYPE + AMPLITUDE + SPEED`, and that the modifiers do not stack.
- **Open at whichever end of the range the subject is largest.** A lighthouse needs the extreme-wide opening
  for a super dolly in exactly as much as a person does.
- Foreground is what makes travel legible.
- Lenses do almost nothing, and naming a rig that would be in frame renders it.
- You cannot place events in time.
