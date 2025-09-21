# GTZAN Genre Recognizer

A machine learning system for music genre classification, developed for the Fundamentals of Machine Learning course at the University of Verona (A.Y. 2024/2025).

## Table of Contents
- [System Objectives](#system-objectives)
- [Dataset Details](#dataset-details)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Authors](#authors)

---

## System Objectives

This project aims to develop a machine learning system capable of accurately classifying music tracks into their respective genres. By extracting relevant audio features and applying appropriate classification algorithms.
The system will try different model to define which is the best solution, with hyperparameters, to achive the best result related this specific problem.

---

## Dataset Details

The project utilizes the GTZAN dataset, a benchmark dataset for music genre classification research:

- **Source**: [GTZAN Dataset](https://www.kaggle.com/datasets/achgls/gtzan-music-genre/data)
- **Size**: 1000 audio tracks (30 seconds each)
- **Format**: 22050Hz Mono 16-bit WAV (or AU) files
- **Classes**: 10 genres with 100 tracks each
  * Blues
  * Classical
  * Country
  * Disco
  * Hip-hop
  * Jazz
  * Metal
  * Pop
  * Reggae
  * Rock

---

## Project Structure

```
GTZAN_Genre_Recognizer/
├── data/
│   └── genres/                       # Dataset directory (created after download)
│       ├── blues/
│       │   ├── blues.00000.au
│       │   ├── ...
│       │   └── blues.00099.au
│       ├── classical/
│       │   ├── classical.00000.au
│       │   └── ...
│       └── ...
├── models/                           # Saved trained models
├── notebooks/
│   ├── 01_download.ipynb             # Dataset acquisition
│   ├── 02_features.ipynb             # Feature extraction exploration
│   ├── 03_training.ipynb             # Model training and evaluation
│   └── 04_evaluation.ipynb           # Model evaluation
├── reports/
│   ├── dataset_doc_link.txt          # Dataset download links
│   └── presentation.pptx             # PPT presentation
│   └── Technical_Report.pdf          # PDF technical report
├── src/
│   ├── download_data.py              # Dataset download utilities [not used]
│   ├── download_missing_library.py   # Script to download missing package
│   ├── feature_extraction.py         # Audio feature extraction
│   └── os_path_management.py         # Path handling across platforms
├── config.json                       # Configuration parameters
├── GTZAN_Project.ipynb               # Entry point software
└── README.md
```

---

## Features

- **Audio Feature Extraction**: Extracts MFCCs, chroma, spectral contrast, and other acoustic features
- **Multiple Classification Models**: Implements and compares various algorithms (Random Forest, SVM, etc.)
- **Cross-Platform Compatibility**: Works across different operating systems
- **Configurable Parameters**: Audio processing parameters can be modified via config.json
- **Jupyter Notebooks**: Step-by-step workflow from data acquisition to evaluation

---

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/RiccardoPeruffo96/GTZAN_Genre_Recognizer.git
   cd GTZAN_Genre_Recognizer
   ```

2. Install dependencies:
   in \config.json set 
   ```
   install_missing_libraries = true
   ```

3. Download the GTZAN dataset, link in reports/dataset_doc_link.txt
   Store the files as define in [Project Structure](#project-structure)

4. Run the training notebook:
   ```
   jupyter notebook GTZAN_Project.ipynb
   ```

---

## Authors

- Riccardo Peruffo - [GitHub](https://github.com/RiccardoPeruffo96)
