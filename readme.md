# GTZAN Genre Recognizer

A machine learning system for music genre classification, developed for the Fundamentals of Machine Learning course at the University of Verona (A.Y. 2024/2025).

## Table of Contents
- [System Objectives](#system-objectives)
- [Dataset Details](#dataset-details)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Authors](#authors)

---

## System Objectives

This project aims to develop a machine learning system capable of accurately classifying music tracks into their respective genres. By extracting relevant audio features and applying appropriate classification algorithms, the system can identify the genre of an input audio file. The project serves both as an educational exploration of audio processing techniques and as a practical application of machine learning principles to music information retrieval.

---

## Dataset Details

The project utilizes the GTZAN dataset, a benchmark dataset for music genre classification research:

- **Source**: [GTZAN Dataset](https://www.tensorflow.org/datasets/catalog/gtzan)
- **Size**: 1000 audio tracks (30 seconds each)
- **Format**: 22050Hz Mono 16-bit WAV files
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
│   └── genres/           # Dataset directory (created after download)
├── models/               # Saved trained models
├── notebooks/           
│   ├── 01_download.ipynb # Dataset acquisition
│   ├── 02_features.ipynb # Feature extraction exploration
│   ├── 03_training.ipynb # Model training and evaluation
│   ├── 04_comparison.ipynb # Model comparison
│   └── 05_inference.ipynb # Prediction on new samples
├── src/
│   ├── download_data.py  # Dataset download utilities
│   ├── feature_extraction.py # Audio feature extraction
│   └── os_path_management.py # Path handling across platforms
├── config.json          # Configuration parameters
└── README.md
```

---

## Features

- **Audio Feature Extraction**: Extracts MFCCs, chroma, spectral contrast, and other acoustic features
- **Multiple Classification Models**: Implements and compares various algorithms (Random Forest, SVM, etc.)
- **Cross-Platform Compatibility**: Works across different operating systems
- **Configurable Parameters**: Audio processing parameters can be modified via config.json
- **Jupyter Notebooks**: Step-by-step workflow from data acquisition to inference

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

3. Download the GTZAN dataset: 
   in \config.json set 
   ```
   download_missing_dataset = true
   ```
   This will set the dataset during execution
   or
   ```
   python -m src.download_data
   ```
   This will download the dataset to `data/GTZAN.zip` and extract it to `data/genres/`.

---

## Usage

### Training a Model

Run the training notebook:
```
jupyter notebook GTZAN_Project.ipynb
```

### Predicting Genre for a New Audio Sample

TODO
---

## Model Performance

The best model achieves the following performance metrics on the GTZAN dataset:

- **Accuracy**: 
- **F1 Score**: 
- **Training Time**: 

---

## Authors

- Riccardo Peruffo - [GitHub](https://github.com/RiccardoPeruffo96)