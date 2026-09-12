# Judging

**A person decides whether a shot works. A measurement is evidence.**

That is not modesty. In this project the measurements were confidently wrong often enough that the rule had to
be written down and enforced.

## Four overturned conclusions

Every one of these was recorded as a finding, and every correction came from watching the clip.

| Recorded conclusion | What watching it showed |
|---|---|
| A crash-zoom prompt was "confounded" for naming a prime lens on a zoom shot, measured 3.15x against 8.97x for the zoom-lens version | That version was the keeper. Lenses do almost nothing, so the confound was never real |
| "The dolly zoom does not port" — three consecutive failures, the last measuring a 1.54x lock against ~1.1x on good takes | It ports. The failure was in the metric |
| A scaffold was banned for pinning framing and halving the move, and the test runner **throws** on it | The best dolly zoom in the project used that scaffold. The guard blocks the best recipe there is |
| "No clear motion transfer from a reference video, consistent with the earlier test" | Judged a pass and kept, which reopens the question |

And three metrics mis-described a single shot in one day.

**Run metrics privately as a sanity check. Never let one outrank your eyes.**

## Pick the axis to match the shot

A general-purpose metric will confidently mis-describe a specific shot. Recorded cases:

| It called | It was | Why |
|---|---|---|
| a crane rise | "a pull-out" | The rise and the retreat look the same to a scale metric |
| a 360 orbit | "weak" | Cumulative pan cancels over a circle. A perfect orbit measures near zero |
| a rack focus | "absent" | It sampled a fixed centre band as the subject, and the subject was right of frame |
| an unmeasurable background | `0.00x` | A reporting bug. "No data" printed as "no motion" |
| a snorricam's improvement | a regression | Global pan is a whole-frame homography; as the crop tightens, the locked face drags translation toward zero |

| Shot type | Judge on |
|---|---|
| Zoom / push / pull | subject scale first frame to last, **and** background scale — they must disagree for a dolly zoom and agree for a dolly move |
| Orbit | the stills. Faces camera → back to camera with the background behind → faces camera |
| Pan / whip | **peak single-step** displacement, not cumulative. A whip pan spikes; a pan glides |
| Crane / aerial | rise as a fraction of frame height, and whether the background shrinks *with* the subject |
| Handheld | frame-to-frame displacement against a locked reference. 5 px vs 0.11 px is a real handheld |
| Snorricam / dolly zoom | whether the face holds its **position**, not its scale. Horizontal and vertical drift, separately |
| Rack focus | near/far sharpness ratio over time, sampled where the subjects actually are. It must cross 1.0 monotonically |
| Roll / dutch | by eye. A roll gives a tracker nothing |
| Split screen | per-panel luminance over time. Unopened panels must be 0.0, not dim |

## The axis nobody had

⭐ Every metric in the project measured the camera, or the subject's **scale**. None measured whether the face
holds its **position** — which is the entire claim of a snorricam and half the claim of a dolly zoom. Three
versions of a snorricam were judged in an order the instrumentation could not reproduce, and the person judging
turned out to be working on an axis that did not exist yet.

If your metric disagrees with your eyes, **first ask whether it is measuring the thing the shot is about.**

## "Unmeasurable" is not neutral

A background-tracking chain needs trackable structure moving coherently. It scored 21/21 usable steps on a
concert stage and an arctic coast, and **0 of 24** in a snowy forest.

⭐ **Take that as evidence against the shot, not as missing data.** A background a tracker cannot follow is
probably a background that is not doing anything legible.

⚠️ Confounded, though: a low-texture scene defeats the tracker whether or not the shot worked. Two dolly zooms
were judged on half the evidence for exactly this reason. **Run motion tests in a textured scene** — buildings,
fence lines, towers — so the decisive half is measurable at all.

## Flags that a number is lying

- **A large spread between two metrics on the same clip.** A 9x disagreement means at least one is wrong.
- **A "subject scale" on a shot that ends with no subject in frame.** An eyes-in shot reported subject 1.19x and
  background 17.78x when the last frame is nothing but an iris.
- **A chained product built from a minority of good steps.** If most steps failed, the product is noise, and it
  should print as unmeasurable rather than as a value.
- **Corner luminance on a shot whose composition changed.** It measures the corners of the *frame*, so a reframe
  reads as a vignette.

## Iterating honestly

- **One variable per attempt, same seed.** Three re-runs in this project changed precision *and* length at once
  and stopped being attributable to either.
- **Record what an attempt disproved**, not just what it showed. Two theories here were expensive and wrong, and
  both are written down as disproofs so nobody spends the time again.
- **Keep every generation.** The best take in the project was one that had been written off.
- **Write the retraction, do not delete the claim.** Several rules in this library replaced an earlier rule that
  was wrong, and the wrong version is usually the more useful half to read.
