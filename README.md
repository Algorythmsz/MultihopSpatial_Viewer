# MultihopSpatial Viewer

An interactive I/O browser for the **MultihopSpatial** benchmark test set (4,500 samples).  
This repository is an unofficial viewer — it is not affiliated with the original authors.

**[🔍 Open Viewer](https://algorythmsz.github.io/MultihopSpatial_Viewer/)**

---

## Original Benchmark

> **MultihopSpatial: Multi-hop Compositional Spatial Reasoning Benchmark for Vision-Language Model**  
> Youngwan Lee, Soojin Jang, Yoorhim Cho, Seunghwan Lee, Yong-Ju Lee, Sung Ju Hwang  
> arXiv:2603.18892 (March 2026)

**[📄 Paper](https://arxiv.org/abs/2603.18892)** · **[🌐 Project Page](https://youngwanlee.github.io/multihopspatial)**

### Motivation

> "Existing benchmarks predominantly focus on elementary, single-hop relations, neglecting the multi-hop compositional reasoning and precise visual grounding essential for real-world scenarios." — §1

MultihopSpatial addresses this gap by requiring models to jointly perform **multi-step spatial reasoning** and **precise bounding box localization** in a single question.

### Dataset Statistics

| | |
|---|---|
| Test QA pairs | **4,500** (perfectly balanced) |
| Training corpus (MultihopSpatial-Train) | **6,791** samples |
| Unique images | **3,563** |
| Hop levels | **1 / 2 / 3** |
| Per hop | 750 ego-centric + 750 exo-centric = **1,500** |
| Inter-rater agreement | Krippendorff's α = **0.90** |
| Image sources | COCO, PACO-Ego4D |

### Spatial Concept Tags

Each question is annotated with one or more primitives:

| Tag | Type | Example phrases |
|---|---|---|
| **POS** | Positional relation | *behind, on the left side, in front of* |
| **REL** | Relative distance / comparison | *closest, farthest, largest, lowest* |
| **ATT** | Object attribute | *round, white, rectangular, silver* |

- **1-hop:** single primitive (POS or REL)
- **2-hop:** two primitives combined (ATT+POS, ATT+REL, or POS+REL)
- **3-hop:** all three (ATT + POS + REL)

### Evaluation Metrics

| Metric | Definition |
|---|---|
| **MCQ Accuracy** | Standard multiple-choice correctness (4 options) |
| **Acc@50IoU** | Correct answer *and* IoU(predicted bbox, GT bbox) ≥ 0.5 |
| **Avg. IoU** | Mean IoU over MCQ-correct samples only |

> "The metric penalizes models that select the right answer without accurate spatial localization." — §3

### Results (37 VLMs evaluated)

| Model | MCQ Acc | Acc@50IoU |
|---|---|---|
| Gemini-3-Pro | 64.7% | 40.6% |
| Qwen3-VL-32B-Thinking | 46.8% | 37.4% |
| GLM-4.6V | 43.2% | 35.2% |

> "Compositional spatial reasoning remains a formidable challenge … average ungrounded ratio reaches 59%." — §4

For full results across all 37 models, see the [paper](https://arxiv.org/abs/2603.18892) and [project page](https://youngwanlee.github.io/multihopspatial).

---

## Viewer Usage

Open `index.html` locally after placing the images in `./images/`:

```
images/
  000000062608.jpg
  ...
index.html
```

Images are loaded from `./images/{filename}` first, then fallen back to COCO dataset URLs.

**Controls:** `←` / `→` browse samples · `↑` / `↓` switch category · `1`–`6` jump · **▦ gallery** toggle grid view
