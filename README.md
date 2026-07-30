# MedVis

> **Inspect. Decide. Process. Quantify.**

MedVis is a modular, rule-based image processing pipeline designed to automate the conversion of raw medical images into structured, analyzable data using classical computer vision techniques.

Unlike traditional image processing scripts that rely on manually tuned parameters, MedVis follows a deterministic decision-making pipeline. It first inspects the image quality, applies predefined rules to select the most suitable processing strategy, extracts meaningful foreground structures, converts pixel-level information into structured data, and benchmarks its own performance using objective quality metrics.

The project is being developed as an engineering-focused prototype emphasizing reproducibility, automation, modularity, and zero human intervention.

---

## Objectives

* Automated image quality inspection
* Rule-based decision engine
* Classical image enhancement and denoising
* Foreground extraction and segmentation
* Pixel-to-data conversion
* Quantitative image quality benchmarking
* Fully automated processing pipeline
* Reproducible experimentation

---

## Development Philosophy

MedVis follows four fundamental principles:

**Inspect → Decide → Process → Quantify**

Every module inside the project contributes to one or more of these stages.

---

## Repository Structure

```text
configs/          Configuration files
datasets/         Public datasets (excluded from Git)
docs/             Project documentation
outputs/          Generated outputs
src/              Source code
tests/            Unit tests
```
---

## Technology Stack

* Python
* OpenCV
* NumPy
* scikit-image
* Pillow
* PyYAML
* Pandas
* Pytest

---

## License

MIT License.
