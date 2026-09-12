# Gear

**Short version: the gear line is cosmetic. Do not spend an iteration on it.**

Most prompt guidance for video models tells you to name a camera body and a lens. It is satisfying to
write and it reads like film-making. On H3 it was tested properly and it did nothing.

## The controlled run

Same character plate, same seed, same scene, 124 frames, **gear the only variable**:

| | corner / centre luma | horizon | framing |
|---|---|---|---|
| **no gear named** | 0.59 | 55% | baseline |
| ARRI Alexa + Cooke S4 **50mm** | 0.60 | 55% | identical to baseline |
| IMAX + Petzval **8mm** | **0.44** | 55% | **identical to baseline** |
| RED V-Raptor + Zeiss Ultra Prime **75mm** | 0.78 | **70%** | visibly **tighter** |

Verdict from the person judging: *"I did not really see any major difference in the outputs
regardless of the gear specified."*

What the instruments found, for the record:

- **Focal length is asymmetric.** The 75mm renders - subject and background larger, less foreground,
  compressed depth. The 8mm does not; it is pixel-for-pixel a 50mm. An 8mm is a 6x wider field of
  view, so if it were being simulated the two could not match. Plausible cause, untested: cinematic
  training footage is overwhelmingly 35-85mm, so a telephoto is in distribution and a fisheye is not.
- **The Petzval genuinely darkens the corners** - 0.44 against 0.59, a 25% drop in an otherwise
  identical frame. Vintage-glass character comes through as *tone* even when geometry does not.
- ⚠️ The 75mm's 0.78 is **not** a vignette reading. Corner luma assumes a fixed composition, and that
  frame's composition changed. The number is measuring the reframe.

Neither of the two real effects reads as a difference to a viewer.

## The rule that survives: gear changes CONTENT, not OPTICS

Gear only affects the output when it names something that would be **in the scene**.

| | Effect |
|---|---|
| *"Snorricam body rig"* | ❌ H3 **rendered the rig** in frame |
| *"an array of still cameras fired in sequence"* | ❌ told a video model the camera does not travel; camera motion collapsed from 108% to 22% |
| Cooke S4 vs Petzval vs Zeiss, 8mm vs 50mm vs 75mm | nothing a viewer would call a difference |

**So: never name a rig a camera could see, and do not expect a lens to do anything.**

## What to write instead

- **State framing as framing.** `framing.md`.
- **Describe the effect, not the equipment.** The snorricam recipe says *"the camera, fixed rigidly
  to her body, holds her face locked dead-centre at exactly the same size and position throughout"*
  and never names a rig. That is what made it work.
- Keep a plausible gear line if you like the flavour - it costs nothing. Just do not debug with it.

## One historical note, since the prompts show it

Early guidance in this project said a zoom shot needs a **zoom lens**, because naming a prime while
asking the lens to zoom is self-contradictory. The crash-zoom prompt that shipped names a Cooke S4,
which is a prime, and it was the version picked over the zoom-lens one. On the evidence above the
distinction matters far less than it appeared to. The rule is not wrong so much as irrelevant.
