# Shot index

Twenty-nine shots that produced a usable result, plus the mirror of one of them, plus one that cannot be done.
Fourteen are from Part 1 and fifteen from Part 2. Part 1 was developed on a single subject set and
re-rendered at 1344x768; Part 2 was rendered at 1344x768 across a wider cast and more locations.

**The crash zooms need a step after the render.** H3 takes 1.7 to 2.6 seconds over a zoom that should take a
fifth of one, whatever the prompt says. `scripts/snap.py` finds the zoom in the clip and ramps it to three
frames. See `crash-zoom-in.md` and `crash-zoom-out.md`.

**Two axes were only ever tested on one setting**, and both are parameterised rather than hardcoded: the
subject was always a **person** (`../references/subjects.md`), and each shot writes the **one direction** that
was rendered (`../references/direction.md`).

**"Verified" means a person watched it and said it reads as the intended shot.** Not that a metric agreed — in
this project the metrics were confidently wrong four times, and each correction came from watching the clip.

## Part 1

| Shot | What a viewer sees | Primitives | Needs |
|---|---|---|---|
| [`crash-zoom-in`](crash-zoom-in.md) | Snaps wide to tight in one violent magnification. The world does not move | `Zoom In` + large + fast | wide opening; **`snap.py` after the render** (Part 2) |
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

## Part 2

| Shot | What a viewer sees | Primitives | Needs |
|---|---|---|---|
| [`pov`](pov.md) | The eyes of an unseen viewer; only their hand ever appears | `POV` | **192 frames**; your action says where the subject starts |
| [`slow-pan-reveal`](slow-pan-reveal.md) | Turns slowly across the place and finds the person at the end | `Pan Right` + slow, camera in place | subject out of frame at the start, doing something |
| [`time-lapse`](time-lapse.md) | Subject at normal speed while crowds, traffic and light rush past | `Static Shot` + a described time-lapse | a busy place |
| [`fisheye`](fisheye.md) | A very wide lens almost on the face, pushing in as they lean in | `Push In` + a described warp | **not a true fisheye**; describe the picture, not the lens |
| [`cutaway-montage`](cutaway-montage.md) | Face, four split-second inserts of hands getting ready, face again | none: seven timed `[Shot N]` cuts | name each object, where the hand works, which hand, and where it ends |
| [`crash-zoom-out`](crash-zoom-out.md) | Held close-up, one violent zoom out to wide, held wide | `Zoom Out`, a flat lens change | tight opening; **`snap.py` after the render** |
| [`hero-spin`](hero-spin.md) | Low camera circles and looks up as they rise from a crouch | `Arc Shot` + large + fast, low | crouched opening |
| [`rooftop-swing`](rooftop-swing.md) | Leaps off a rooftop, swings across the gap, lands, turns round | `Tracking Shot` + large + fast | a city of tall buildings; facing stated at every stage |
| [`fpv-drone`](fpv-drone.md) | Dives from high, banks, skims the ground, pulls up to a medium shot | a described flight | high wide opening |
| [`overhead-swing`](overhead-swing.md) | Straight overhead, swings down in a quarter-circle to face-on | a described arc with a tilt | **an open place**; never say "drone" |
| [`walk-past-camera`](walk-past-camera.md) | Walks at the lens, passes beside it, the camera pans to follow | `Pan Right` + fast | subject must walk; wide opening |
| [`crane-down`](crane-down.md) | High and looking down, descends and levels out on the face | `Pedestal Down` + `Tilt Up` | high wide opening; one render |
| [`jib-up`](jib-up.md) | Rises up and over them, ends looking down with the place around | a rise + `Tilt Down`, one arc | medium opening; one render |
| [`low-angle-hero`](low-angle-hero.md) | Low and looking up, pushes in until they tower over the frame | `Push In` + slow, low | **gentler angle than the name**; see the file |
| [`tilt-up-reveal`](tilt-up-reveal.md) | Opens on the feet, tilts up the body, lands on the face | `Tilt Up` + slow, camera in place | face out of frame at the start |

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
| **Part 2, needed several rounds** | `pov`, `cutaway-montage`, `overhead-swing`, `rooftop-swing` (the landing), `fisheye` |
| **Part 2, verified on one render only** | `crane-down`, `jib-up` |
| **Part 2, fixed after the render** | `crash-zoom-in`, `crash-zoom-out`: H3 will not snap, `snap.py` does |
| **Part 2, still imperfect** | `fisheye` (no true bulge), `low-angle-hero` (the angle is mild) |
| **Rendered on weak evidence** | `dolly-zoom-telephoto` - correct physics, never validated with an identity plate attached |
| **Abandoned** | `bullet-time` |

## Not named shots, but the two things that turn out not to matter

| | |
|---|---|
| **Lenses and bodies** | Cosmetic. `../references/gear.md` |
| **Event timing** | You state the sequence; H3 picks the clock. `../references/performance.md` |
