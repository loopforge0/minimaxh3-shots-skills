# Direction

**Most of the twelve primitives are directional pairs, and this library only ever exercised one side of
most of them.** That is a gap in the testing, not a property of the model.

Every shot recipe here writes one specific direction, because that is the direction that was rendered and
judged. Where direction is a free axis rather than part of the shot's identity, it is a **slot with a
default**, so you can flip it without rewriting the shot line.

## The direction slots

| Shot | Slot | Default | The other value |
|---|---|---|---|
| `whip-pan` | `{PAN_DIRECTION}` | `right` | `left` |
| `dutch-angle` | `{ROLL_DIRECTION}` | `counterclockwise` | `clockwise` |
| `eyes-in` | `{EYE}` | `right` | `left` |

Set them in your scene file like any other slot:

```json
{ "PAN_DIRECTION": "left", "ROLL_DIRECTION": "clockwise" }
```

⚠️ **Only the defaults were tested.** `Pan Left` and `Roll Clockwise` are documented primitives, so there is
no reason to expect them to behave differently from their mirrors, but this library has no evidence either
way. Treat a flipped direction as untested and watch the first render.

## Where direction is the shot, not a slot

These are not parameterised, because reversing them produces a **different shot** with its own framing
requirement:

| Shot | Why |
|---|---|
| `crash-zoom-in` | A crash zoom *out* opens tight and ends wide, so it inverts the framing rule. Untested here |
| `super-dolly-in` | A dolly *out* is `aerial-pullback` territory and needs different foreground staging |
| `aerial-pullback` | The rise and the retreat are the shot |
| `crane-rise` | `Pedestal Up` + `Tilt Down` is the move; inverting gives a descent, untested |
| `yoyo-zoom` | Out-hold-return is the shot. An in-hold-return has no name and was not tried |
| `snorricam` | Forward walk. A backward walk was not tried and would probably fight the lock |
| `dolly-zoom` | **Both directions exist as separate recipes.** See below |

## The dolly zoom has two directions and both were rendered

They are genuinely different shots, so they are separate files:

| | Primitives | The background |
|---|---|---|
| [`dolly-zoom`](../shots/dolly-zoom.md) | `Push In` + `Zoom Out` | recedes, shrinks and **spreads apart** into greater depth |
| [`dolly-zoom-telephoto`](../shots/dolly-zoom-telephoto.md) | `Pull Out` + `Zoom In` | **flattens and looms closer**, the classic *Vertigo* stairwell read |

⚠️ Both were rendered and measured, **but in a run where the reference image was being silently discarded**,
so both were effectively text-only. The wide direction has since been re-rendered with a plate attached many
times over; the telephoto direction has not. Take the telephoto recipe as the weaker of the two on evidence.

## What this library actually exercised

The full documented vocabulary against what has a render behind it here. Anything marked untested is
**documented by MiniMax and simply not tried by me** — no conclusion should be drawn from its absence.

| Primitive | Exercised | Where |
|---|---|---|
| `Zoom In` | ✅ | crash zoom, yo-yo return, dolly zoom telephoto |
| `Zoom Out` | ✅ | yo-yo departure, dolly zoom wide |
| `Push In` | ✅ | super dolly in, eyes-in, dolly zoom wide |
| `Pull Out` | ✅ | aerial pullback, dolly zoom telephoto |
| `Pan Right` | ✅ | whip pan |
| `Pan Left` | ❌ **untested** | — |
| `Truck Left` / `Truck Right` | ❌ **neither tested** | — |
| `Tilt Down` | ✅ | crane rise |
| `Tilt Up` | ❌ **untested** | — |
| `Pedestal Up` | ✅ | crane rise, aerial pullback |
| `Pedestal Down` | ❌ **untested** | — |
| `Arc Shot` | ✅ direction never specified | 360 orbit |
| `Tracking Shot` | ✅ | crane rise, handheld |
| `Static Shot` | ✅ | rack focus, split screen |
| `Shake Strongly` | ✅ | handheld |
| `Shake Slightly` | ❌ **untested.** A different shot, a nervous lock-off | — |
| `Roll Counterclockwise` | ✅ | dutch angle |
| `Roll Clockwise` | ❌ **untested** | — |
| `POV` | ❌ **untested** | — |

**Four of the twelve have no render behind them at all**: `Truck`, `POV`, and the unexercised halves of
`Tilt` and `Pedestal`. A truck is the obvious gap — it is a lateral translation, so it should produce
parallax the way a push does, and the foreground rule in `../shots/super-dolly-in.md` ought to apply to it.
That is a prediction, not a result.

## On the arc

`Arc Shot` carries no documented direction, and the verified 360 orbit never specified one. You can write
*"sweeping a complete circle around her to the left"* and it may well work, since the model clearly
understands more than the twelve labels. It is undocumented and untried, so watch the first render.
