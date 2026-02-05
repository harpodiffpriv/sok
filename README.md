# Harpo Artifacts (USENIX Security '26)

This repository contains the artifacts for the paper:
**“SoK: A Practical Black-Box Framework for Evaluating Differential Privacy in Cyber-Physical Systems.”**

It provides:
- The Harpo evaluation inputs as structured JSON files (`paper.json`, `weight.json`)
- The scoring implementation used to compute **Privacy / Utility / Safety** scores in **[0,1]**
- Scripts to reproduce the figures and summary tables reported in the paper
- The dataset of reviewed papers’ scores (as used in the artifact page / plots)

> **Anonymity note:** This repository is intended for anonymous review. Please avoid linking it to personal accounts or identifiable information during the review period.

---

## Quick Start

1) Fill out `paper.json` for the paper you want to evaluate (following the rubric fields).

2) Run:
```bash
python blackbox.py paper.json weight.json


---

## Output
The output is a JSON object with three scores in [0,1]:

{
  "Privacy": 0.2,
  "Utility": 0.3,
  "Safety": 0.0
}

