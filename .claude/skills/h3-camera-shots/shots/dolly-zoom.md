# Dolly Zoom (the Vertigo effect)

**Status:** verified, and **the least reliable shot in the library.** Read the whole file.
**Effect:** the subject's size and position in frame never change while the world behind them recedes,
shrinks and spreads apart into much greater depth.
**Primitives:** `Push In` + `Zoom Out`, at exactly cancelling rates — the only **contradictory** pair in the
library.
**Reference:** *Vertigo*; the *Jaws* beach reverse.

## Shot line

> Throughout the entire shot {SUBJECT}'s size and position in frame stay exactly constant: {PRONOUN_SUBJ}
> is framed identically in the last frame as in the first, neither closer nor further away, and never
> drifts from the centre of frame. {FACE_CAMERA} {ROOTED} The camera pushes in while simultaneously
> zooming out at exactly the matching rate, so that the size of {SUBJECT} in frame is cancelled out
> entirely and does not change, while {ENVIRONMENT_ELEMENTS} behind {PRONOUN} recede, shrink, and spread
> apart into much greater depth as the lens's focal length changes. Only the background transforms.

Reverse the pair for the opposite direction (`Pull Out` + `Zoom In`): the world closes in and compresses
instead.

## It needs BOTH halves, and that is the whole difficulty

A dolly zoom is **subject locked** *and* **background receding**. Either one alone is a different shot, and
this project got that wrong twice in opposite directions on the same week.

| | subject lock | background recession | reading |
|---|---|---|---|
| the good takes | **1.05-1.27x** | **0.47-0.53x** | ✅ both halves |
| composed on a new scene | 1.54x ❌ | 0.48x ✅ | a push-in wearing a Vertigo background |
| named-reference version | **1.00x** ✅ | **unmeasurable** | a locked subject in a shot where little happens |

**Opposition alone is not a dolly zoom — the subject must be locked. And lock alone is not one either — a
perfect 1.00x is exactly what a shot where nothing happens also produces.**

## Framing

Open **where it ends.** The subject's scale never changes, so there is no range to open into. Given a wide
opening this shot becomes a plain push-in. This is the exception to the wide-opening rule.
`../references/framing.md`.

## What ports and what does not

Moving the recipe to a new subject and a new scene: **the background behaviour ports perfectly.** 0.48x sits
right inside the band of every dolly zoom judged good. **What fails is the subject lock, and only the lock.**
Lock detail on the failing take: horizontal drift 3.15%, vertical 10.13%, size variation 13.3% — the subject
is not merely growing, she is wandering.

No lever has been found for it. `at slow speed` was added specifically to tighten the lock and the lock got
*worse*. The locked variant prompt (below) piles on every invariant clause that could be written and is the
current best attempt.

## ⚠️ Test it in a textured scene

Two attempts were judged on half the evidence because their scene defeated the measurement. A snowy forest
gave **0 usable background-tracking steps out of 24**; a rooftop with towers gave **24 of 24**. Trackable
structure is not optional if you want to know whether the background half worked.

⭐ And take "the tracker got nothing" as **evidence against** the shot, not as missing data. A background a
tracker cannot follow is probably a background that is not doing anything legible.

## The named-reference result, and its retraction

Worth knowing about, because it is the most tempting shortcut in this library.

Thirteen words — *"The camera performs a Hitchcock dolly zoom, the Vertigo effect, on `<Subject 1>`."* —
produced a **1.00x lock**, where fifty-six words of composed primitives produced 1.88x in the same scene with
the same subject, gear and length. MiniMax's own flagship example uses "the Hitchcock camera movement", so
naming a compound shot is not obviously outside the model's range.

**It was recorded as the project's headline finding and then retracted.** The same clip had **no measurable
background recession at all**, and three composed takes were judged better dolly zooms than it. What survives
is narrow: **naming beat composing on the lock axis, in one scene, n=1.** It is not a mandate to name shots
instead of composing them.

Still worth trying on a shot the primitives cannot reach. Just measure both halves before believing it.

## Gotchas

- **Do not add a background reference plate to fix the environment drift.** It halves the camera move, and
  this shot has none to spare. `../references/scaffold.md`.
- ⚠️ Without a background plate the environment *content* drifts — in one verified take a drum kit became a
  grand piano by the end. The camera move is correct; the scene is being re-invented as it goes. That is the
  trade.
- The verbs outrank the result clause. One variant's result clause described wide behaviour while its verbs
  asked for telephoto, and **the verbs won**. Get the primitive pair right first.
- A reference **video** of a real dolly zoom transfers no camera motion. Tested twice. Do not bother.

## Machine-readable

```json
{
  "id": "X-01",
  "slug": "dolly-zoom",
  "name": "dolly zoom",
  "status": "verified-unreliable",
  "motion": "stationary",
  "length": 124,
  "framing": "{MEDIUM_FRAMING}",
  "shot_line": "Throughout the entire shot {SUBJECT}'s size and position in frame stay exactly constant: {PRONOUN_SUBJ} is framed identically in the last frame as in the first, neither closer nor further away, and never drifts from the centre of frame. {FACE_CAMERA} {ROOTED} The camera pushes in while simultaneously zooming out at exactly the matching rate, so that the size of {SUBJECT} in frame is cancelled out entirely and does not change, while {ENVIRONMENT_ELEMENTS} behind {PRONOUN} recede, shrink, and spread apart into much greater depth as the lens's focal length changes. Only the background transforms.",
  "extra_slots": {},
  "scene_warning": "Use a scene with trackable structure (buildings, towers, fence lines). Low-texture scenes make the background half unmeasurable.",
  "framing_note": "Open where it ends. Do NOT open wide."
}
```

## Prompts as they ran

| File | What it is |
|---|---|
| `prompts/K-06n_dolly-zoom-k06.txt` | The base recipe on a concert stage. Measured subject 1.27x, background 0.47x — a correct dolly zoom |
| `prompts/X-01_dolly-zoom-composed.txt` | The portability test on a rooftop. Background ported, lock failed |
| `prompts/X-01b_dolly-zoom-composed-locked.txt` | Every invariant clause that could be written, stacked. The current best attempt at the lock |
