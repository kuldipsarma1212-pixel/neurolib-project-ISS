# EEG Data Analysis using MNE-Python

## Overview

This repository contains an EEG preprocessing and feature extraction pipeline developed during my summer research internship.

The project uses MNE-Python for EEG signal processing and extracts frequency-domain features for further statistical analysis.

---

## Dataset

Dataset:
DS003490

Contains

- EEG recordings
- Channel information
- Electrode locations
- Event markers

---

## Processing Pipeline

Step 1
Load EEG dataset

Step 2
Filtering

- Bandpass Filter
- Notch Filter

Step 3
Bad Channel Detection

Step 4
ICA Artifact Removal

Step 5
Feature Extraction

- Power Spectral Density
- Alpha Power
- Beta Power
- Theta Power
- Delta Power

---

## Technologies

- Python
- MNE-Python
- NumPy
- Pandas
- SciPy
- Matplotlib

---

## Folder Structure

```text
neurolib_python/
    step1_load_explore.py
    step2_filtering.py
    step3_bad_channels.py
    step4_ica.py
    step5_feature_extraction.py
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Author

Kuldip Sarma

Integrated MSc Mathematics

Tezpur University

India