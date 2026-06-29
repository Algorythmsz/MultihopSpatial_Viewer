# MultihopSpatial

**Multi-hop Compositional Spatial Reasoning Benchmark for Vision-Language Models**

> Youngwan Lee, Soojin Jang, Yoorhim Cho, Seunghwan Lee, Yong-Ju Lee, Sung Ju Hwang
> KAIST · ETRI · *arXiv 2603.18892* (March 2026)

**[📄 Paper](https://arxiv.org/abs/2603.18892)** · **[🌐 Project Page](https://youngwanlee.github.io/multihopspatial)** · **[🔍 I/O Browser](https://algorythmsz.github.io/MultihopSpatial_Viewer/)**

---

## Overview

Existing spatial reasoning benchmarks focus on elementary single-hop relations, overlooking the **multi-hop compositional reasoning** and **precise visual grounding** required in real-world embodied scenarios. MultihopSpatial addresses this gap with:

- **4,500 test QA pairs** — fully balanced across hop levels and viewpoints
- **Multi-hop queries** composing 1–3 spatial reasoning steps
- **Joint evaluation** of answer selection *and* bounding box localization (Acc@50IoU)
- **37 VLMs evaluated**, showing compositional spatial reasoning remains a formidable challenge

---

## Dataset Statistics

| Split | Samples |
|---|---|
| **Test** | 4,500 |
| **Train** (MultihopSpatial-Train) | 6,791 |
| Unique images | 3,563 |

**Balance:** 1,500 questions per hop level × 750 ego-centric + 750 exo-centric  
**Inter-rater agreement:** Krippendorff's α = 0.90  
**Image sources:** COCO, PACO-Ego4D

---

## Task Design

### Spatial Concept Tags

Each question is annotated with one or more of three spatial reasoning primitives:

| Tag | Type | Example |
|---|---|---|
| **POS** | Positional relation | *behind*, *on the left side*, *in front of* |
| **REL** | Relative distance / comparison | *closest*, *farthest*, *largest*, *lowest* |
| **ATT** | Object attribute | *round*, *white*, *rectangular*, *silver* |

### Hop Levels

| Hop | Composition | Viewpoints | Count |
|---|---|---|---|
| **1-hop** | POS *or* REL | ego + exo | 1,500 |
| **2-hop** | ATT+POS, ATT+REL, *or* POS+REL | ego + exo | 1,500 |
| **3-hop** | ATT + POS + REL | ego + exo | 1,500 |

### Question Format

Each sample is a 4-option MCQ paired with a bounding box localization task:

> *"From the perspective of the woman wearing a gray T-shirt, which object **behind** the woman is **farthest** from her? (a) white dishcloth (b) kettle (c) faucet (d) flowerpot — And provide the bounding box coordinate of the region related to your answer."*

---

## Evaluation Metrics

| Metric | Definition |
|---|---|
| **MCQ Accuracy** | Standard multiple-choice correctness |
| **Acc@50IoU** | Correct answer *and* IoU(predicted bbox, GT bbox) ≥ 0.5 |
| **Avg. IoU** | Mean IoU computed over MCQ-correct samples |

Acc@50IoU is the primary metric — it penalizes models that select the right answer without accurate spatial localization.

---

## Key Findings (37 VLMs evaluated)

| Model | MCQ Acc | Acc@50IoU |
|---|---|---|
| Gemini-3-Pro | 64.7% | 40.6% |
| Qwen3-VL-32B-Thinking | 46.8% | 37.4% |
| GLM-4.6V | 43.2% | 35.2% |

- **Grounding gap:** Average ungrounded ratio reaches **59%** — models frequently select the correct answer but fail to localize it
- **Ego-centric floor:** Even strong models hit a 20–25% floor on ego-centric tasks, masking real capability differences
- **3-hop hardness:** Only 3 of 37 models exceed the 25% random baseline on 3-hop ego-centric samples
- **Encoder bottleneck:** Vision encoder capacity matters more than LM size; small fixed encoders saturate early in grounding performance

---

## Training Corpus & Post-training

GRPO fine-tuning on MultihopSpatial-Train (Qwen3-VL-4B):

| | Before | After |
|---|---|---|
| MCQ Accuracy | 37.8% | 62.9% |
| Acc@50IoU | 31.0% | 53.8% |
| CALVIN task completion | — | +0.23 avg |
| LIBERO success rate | 35.8% | 40.0% |

Spatial reasoning gains transfer to downstream embodied manipulation tasks.

---

## Browser Usage

Open `index.html` after placing images in `./images/`:

```
images/
  000000062608.jpg
  ...
index.html
```

Images load from `./images/` first, then fall back to COCO dataset URLs.

**Controls:** `←` / `→` browse samples · `↑` / `↓` switch category · `1`–`6` jump · **▦ gallery** toggle grid view
