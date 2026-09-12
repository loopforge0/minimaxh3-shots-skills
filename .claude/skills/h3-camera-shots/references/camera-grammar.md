# Camera grammar

## The twelve primitives

Reproduced from §4.3 of MiniMax's `base-en.txt`. **There is nothing else.** Anything not on this
list is undocumented - which means untested, not impossible (see the bottom of this file).

| Dimension | Expression | What it does |
|---|---|---|
| Motion type | `Zoom In / Zoom Out` | Focal length changes, camera body stays put |
| Motion type | `Push In / Pull Out` | The camera moves forward / backward |
| Motion type | `Pan Left / Pan Right` | Camera in place, lens pivots horizontally |
| Motion type | `Truck Left / Truck Right` | The camera translates horizontally |
| Motion type | `Tilt Up / Tilt Down` | Camera in place, lens pivots vertically |
| Motion type | `Pedestal Up / Pedestal Down` | The whole camera moves up / down |
| Motion type | `Arc Shot` | The camera moves in an arc around the subject |
| Motion type | `Tracking Shot` | The camera follows a moving subject |
| Motion type | `Static Shot` | Position and lens both still |
| Motion type | `Shake Slightly / Shake Strongly` | Slight / strong camera shake |
| Motion type | `POV` | The subject's point of view |
| Motion type | `Roll Clockwise / Roll Counterclockwise` | The camera rolls around the lens axis |
| Amplitude | `with small amplitude` / `with large amplitude` | Range of compositional change |
| Speed | `at slow speed` / `at fast speed` | Pacing of that change |

Write it as an action inside the sentence, not as labels stacked at the end:

> The camera pushes in with small amplitude at slow speed toward the folded letter in her hands.

## Zoom is not push, and that distinction is the whole library

`Zoom In` changes focal length. `Push In` moves the camera. On a real set they look different
because travel produces parallax and a focal-length change does not. H3 honours the distinction,
and three shots that all enlarge the subject are separated only by what the *world* does:

| Shot | The subject | The world |
|---|---|---|
| Dolly zoom | **locked at 1.0x** | warps - the lens undoes the travel |
| Super dolly in | grows | **streams past the lens** |
| Crash zoom in | grows | nothing, flat magnification |

**Without foreground, the last two are the same shot.** A dolly in past distant geometry is
indistinguishable from a zoom, because distant things barely change scale when the camera
translates. If a shot's identity is travel, put something near the lens for the camera to pass.

## What the modifiers measured

Bare push-in, one variable at a time, same seed and scene. Subject scale, first frame to last:

| Clause | Subject scale | Reading |
|---|---|---|
| *(none)* | 1.53x | the usable move |
| `with small amplitude` | 1.47x | **inert.** Not a brake |
| `with large amplitude` | 3.18x | over-drives; the final frame loses all detail |
| `at fast speed` | 2.90x | same scale as large, temporal coherence collapses |
| `large amplitude` + `at fast speed` | 2.83x | **saturates. Modifiers do not stack** |

So: **omit the modifiers by default** - not because `small` brakes, but because `large` and `fast`
over-drive. State them only where the shot's identity is the size or the speed of the move: a crash
zoom, a whip pan, a 360 orbit that has to complete a circle.

⚠️ `small amplitude` behaves differently on a **compound** move. Damping one of two opposing
primitives collapses the effect entirely. The "small kills motion dead" folklore comes from there,
not from single primitives.

## Composing more than one primitive

Count is not the problem. **Contradiction** is.

| | |
|---|---|
| **Complementary** primitives compose well | A crane rise stacks `Tracking Shot` + `Pedestal Up` + `Tilt Down` and produced the most complete shot in the set |
| **Contradictory** primitives fight | A dolly zoom's `Push In` + `Zoom Out` must cancel *exactly* to hold the subject, and that is the one thing in this library that still fails intermittently |
| **Undocumented** requests produce nothing | "frozen", "bullet time" - no primitive behind them |

The cleanest pass in the whole set used **one** primitive (`Roll Counterclockwise`, for a dutch
angle). Adding primitives buys nothing on its own.

## Transitions need a FROM and a TO

Naming the destination took a whip pan from 23 px/step to **218**. Speed comes from having somewhere
to arrive.

⚠️ **Asking for motion blur does not produce motion blur.** The destination produces the speed, and
the speed produces the blur. Requesting the blur directly did nothing.

## The twelve are an interface, not a boundary

Three shots landed with no primitive behind them at all:

- **Rack focus** - there is no focus primitive. It produced a clean monotonic rack, near-to-far
  sharpness ratio 2.88 to 0.40, crossing over smoothly.
- **Three-panel split screen** - there is no layout primitive and no timed-event primitive. It
  produced the triptych with staggered reveals.
- A named compound (**"the Hitchcock dolly zoom, the Vertigo effect"**) produced the best subject
  lock in the set from thirteen words, where fifty-six words of composed primitives did not. ⚠️ That
  result is **narrow** - the same clip showed no measurable background recession, which is the other
  half of a dolly zoom, so naming beat composing on one axis in one scene and nothing more.

In all three cases the prompt described **what the viewer should see**, not which primitives to
combine.

**Treat "not in the twelve" as untested, never as impossible.** But start from the twelve, because
that is what is documented, and reach for a described result when the primitives run out.
