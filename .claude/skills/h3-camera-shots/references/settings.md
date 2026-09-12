# Generation settings

These are not defaults. Several of them decide whether the camera move happens at all, and a wrong
one cannot be fixed by a better prompt.

| Setting | Value | Why |
|---|---|---|
| **Steps** | **20** | 4-step turbo suppresses camera motion almost entirely |
| **Turbo LoRA** | **off** | Same. Distillation trades away motion range |
| Sampler / scheduler | `res_multistep` / `simple` | What every verified run used |
| Node | `MiniMaxH3ReferenceToVideo` (Ref2VA) | An image reference gives excellent identity fidelity |
| Reference plates | **identity only** - no background plate | A background plate halves the camera move |
| `ref_image_size` | **`max`** | `match` renders the plate as frame 0 and the subject is missing for ~16 frames |
| Reference **video** | **none** | Transferred no camera motion in two tests |
| Length | **124 frames minimum** | Below H3's trained range. See below |
| Resolution | 1344x768 native, 864x480 to iterate | See below |

## Frame count is load-bearing

H3's trained range is **124 to 362 frames**. Lengths must satisfy `% 17 == 5`, so the usable values
are 124, 192, 243, 362.

- **124 frames** (~5.2s) suits a single move.
- **192 frames** (~8s) is **required** for anything with three phases. A yo-yo zoom never completed
  its out-hold-return at 96 frames; at 192 all three phases fit. A triptych with two staggered
  reveals plus a shared run-out needs the same.

⚠️ Early work in this project ran at 96 frames, which is **below the trained range**. Those results
are not reliable and are marked as such where they appear.

## Resolution

**1344x768 is the node's native canvas** and the resolution every published clip was rendered at.
It matches the profile in MiniMax's own vLLM-Omni recipe, which is independent confirmation.

864x480 is fine for iterating on whether a move happens. Confirm at native before judging quality.

## Two traps that cost real work

**1. A reference image can be silently discarded.** ComfyUI's `COMFY_AUTOGROW_V3` inputs need flat
dot-notation keys - `ref_images.ref_image_0`, `ref_videos.ref_video_0`. The nested form passes
validation, reports success, and drops the reference. Four early gear comparisons ran with **no
reference at all**, invented four different characters in four different scenes, and were compared as
if only the lens differed.

```bash
node scripts/verify_refs.mjs <workflow.json>   # points each ref at a nonexistent node;
                                               # a properly connected input rejects it
```

**2. A generated reference plate can be pure black.** One image checkpoint rendered mean luma 0 with
no error - the job reported success and wrote a valid, entirely black PNG. Suspected fp8 numerical
overflow. **Check every generated plate before using it:**

```bash
ffmpeg -v error -i plate.png -vf scale=1:1 -f rawvideo -pix_fmt gray - | od -An -tu1
# 0 means a black frame and a failed generation
```

## Quantisation

Development ran on a pruned int8 UNET with an NVFP4 text encoder on a 12 GB card; the published
renders used higher precision on a rented 24 GB card. **How far a shot moves under a different quant
is not characterised here.** Viewers will all be on different weights, so treat precision as an
uncontrolled variable rather than a settled one.
