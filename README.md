# MultihopSpatial

An interactive I/O browser for the **MultihopSpatial** benchmark — a spatial reasoning evaluation suite that tests multi-step egocentric and exocentric spatial understanding.

**[View Browser →](https://algorythmsz.github.io/MultihopSpatial_Viewer/)**

---

## Benchmark Overview

| | |
|---|---|
| **Total test samples** | 4,500 |
| **Question type** | MCQ (4 options) + bounding box localization |
| **Evaluation metric** | Acc@50IoU — answer must match GT *and* predicted bbox must have IoU ≥ 0.5 with GT bbox |
| **Image sources** | COCO, PACO-Ego4D |

## Categories

The benchmark is organized by reasoning complexity (hop count) and viewpoint:

| Category | Hop | Viewpoint |
|---|---|---|
| 1hop · ego | 1-step | Egocentric |
| 1hop · exo | 1-step | Exocentric |
| 2hop · ego | 2-step | Egocentric |
| 2hop · exo | 2-step | Exocentric |
| 3hop · ego | 3-step | Egocentric |
| 3hop · exo | 3-step | Exocentric |

## Question Tags

Questions are annotated with three spatial reasoning concept types:

- **POS** — positional relation (e.g., *behind*, *on the left side*)
- **REL** — relative distance (e.g., *closest*, *farthest*)
- **ATT** — object attribute (e.g., *round*, *white*, *rectangular*)

Multi-hop questions combine two or more of these (e.g., `POS + REL`, `ATT + POS + REL`).

## Browser Usage

Open `index.html` locally after placing the images:

```
images/
  000000062608.jpg
  ...
index.html
```

Images are loaded from `./images/{filename}` first, then fallen back to COCO URLs.

**Keyboard shortcuts:** `←` / `→` sample · `↑` / `↓` category · `1`–`6` jump to category · `▦ gallery` button to toggle grid view
