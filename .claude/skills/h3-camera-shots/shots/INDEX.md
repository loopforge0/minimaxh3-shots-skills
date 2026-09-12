# Shot index

Fourteen shots that produced a usable result, plus the mirror of one of them, plus one that cannot be done.
Every one was developed on a single subject set and re-rendered at 1344x768.

**Two axes were only ever tested on one setting**, and both are parameterised rather than hardcoded: the
subject was always a **person** (`../references/subjects.md`), and each shot writes the **one direction** that
was rendered (`../references/direction.md`).

**"Verified" means a person watched it and said it reads as the intended shot.** Not that a metric agreed — in
this project the metrics were confidently wrong four times, and each correction came from watching the clip.

| Shot | What a viewer sees | Primitives | Needs |
|---|---|---|---|
| [`crash-zoom-in`](crash-zoom-in.md) | Snaps wide to tight in one violent magnification. The world does not move | `Zoom In` + large + fast | wide opening |
| [`super-dolly-in`](super-dolly-in.md) | Charges the length of a space; foreground sweeps out past the frame edges | `Push In` + large + fast | **extreme wide opening, near objects** |
| [`dolly-zoom`](dolly-zoom.md) | Subject welded in place while the world stretches away behind them | `Push In` + `Zoom Out`, cancelling | opens where it ends, textured scene |
| [`dolly-zoom-telephoto`](dolly-zoom-telephoto.md) | The mirror: subject welded in place while the world flattens and looms closer | `Pull Out` + `Zoom In`, cancelling | same, and **weaker evidence** |
| [`yoyo-zoom`](yoyo-zoom.md) | Tears out to the far distance, holds, snaps back to the identical close-up | `Zoom Out` accel, hold, `Zoom In` large+fast | **192 frames** |
| [`eyes-in`](eyes-in.md) | Travels past the face until one eye fills the frame edge to edge | `Push In` + large + slow | a destination beyond the face |
| [`whip-pan`](whip-pan.md) | Tears sideways off one subject and lands on another, everything between smearing | `Pan Right` + a named destination | **two subjects** |
| [`orbit-360`](orbit-360.md) | Complete circle around the subject and back to the front | `Arc Shot` + large + fast | both modifiers |
| [`crane-rise`](crane-rise.md) | Starts at the feet of a runner, climbs, tips over to look straight down | `Tracking` + `Pedestal Up` + `Tilt Down` | subject must run |
| [`aerial-pullback`](aerial-pullback.md) | Rises and retreats until the subject is a speck and the place opens out | `Pull Out` + `Pedestal Up` | tight opening (the default) |
| [`handheld`](handheld.md) | Operator runs alongside; the frame lurches and corrects with every stride | `Shake Strongly` + `Tracking` | subject must run |
| [`dutch-angle`](dutch-angle.md) | Rolls into a canted frame and holds. Tilted horizon, subject off-axis | `Roll Counterclockwise` | a visible horizon or vertical |
| [`snorricam`](snorricam.md) | Face locked dead centre at constant size while the world lurches behind | none — a described result | subject must walk; **never name the rig** |
| [`rack-focus`](rack-focus.md) | Camera still; focus travels from a near face to a far pair | `Static Shot`, then no primitive | **two depth planes, 3 subjects** |
| [`split-screen`](split-screen.md) | Three panels, three angles on one action, revealed one at a time | none | **192 frames**; timing is not yours |
| [`bullet-time`](bullet-time.md) | ❌ **cannot be done.** Not a camera move | — | read it anyway |

## Pick by what the world does

Three shots all enlarge the subject and are separated only by the background:

| | The subject | The world |
|---|---|---|
| `dolly-zoom` | **locked at 1.0x** | warps — the lens undoes the travel |
| `super-dolly-in` | grows | **streams past the lens** |
| `crash-zoom-in` | grows | nothing, flat magnification |

**Without foreground, the last two are the same shot.**

## Reliability, honestly

| | |
|---|---|
| **First-time passes** | `dutch-angle`, `rack-focus`, `split-screen` (layout), `aerial-pullback` |
| **Needed two or three iterations** | `super-dolly-in`, `orbit-360`, `crane-rise`, `handheld`, `eyes-in`, `snorricam` |
| **Still imperfect** | `yoyo-zoom` (proportions), `split-screen` (timing), `dolly-zoom` (the subject lock) |
| **Rendered on weak evidence** | `dolly-zoom-telephoto` - correct physics, never validated with an identity plate attached |
| **Abandoned** | `bullet-time` |

## Not named shots, but the two things that turn out not to matter

| | |
|---|---|
| **Lenses and bodies** | Cosmetic. `../references/gear.md` |
| **Event timing** | You state the sequence; H3 picks the clock. `../references/performance.md` |
