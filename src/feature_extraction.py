"""Feature extraction utilities for audio, parameters tuned for GTZAN dataset.

Provides:
- _agg_stats(x): safe mean/std aggregation
- extract_features(path, sr=22050, n_fft=2048, hop_length=512, n_mfcc=13, rolloff_percent=0.85)

This module is intentionally dependency-light at import-time. It imports numpy and librosa when needed by the functions.
"""
import json
import librosa
import numpy as np
import os
from pathlib import Path
from typing import Tuple

_DEFAULTS = {
    "SR": 22050,
    "N_FFT": 2048,
    "HOP": 512,
    "MFCC_N": 13,
    "ROLLOFF_PERCENT": 0.85,
}

def _load_defaults_from_config() -> dict:
    """Try to read `config.json` from the project root and return audio defaults.

    If the file is missing or keys are invalid/missing, fall back to built-in defaults.
    """
    # Search for config.json in repository root (two levels up from src)
    possible = [
        Path(__file__).resolve().parents[1] / "config.json",
        Path(__file__).resolve().parents[2] / "config.json",
        Path.cwd() / "config.json",
    ]
    for p in possible:
        try:
            if p.exists():
                with open(p, "r", encoding="utf-8") as fh:
                    cfg = json.load(fh)
                audio = cfg.get("audio_defaults", {})
                # Validate and coerce types
                out = {}
                out["SR"] = int(audio.get("SR", _DEFAULTS["SR"]))
                out["N_FFT"] = int(audio.get("N_FFT", _DEFAULTS["N_FFT"]))
                out["HOP"] = int(audio.get("HOP", _DEFAULTS["HOP"]))
                out["MFCC_N"] = int(audio.get("MFCC_N", _DEFAULTS["MFCC_N"]))
                out["ROLLOFF_PERCENT"] = float(audio.get("ROLLOFF_PERCENT", _DEFAULTS["ROLLOFF_PERCENT"]))
                return out
        except Exception:
            # Ignore and continue to fallback
            continue
    return _DEFAULTS.copy()

# Load defaults at import time
_CFG = _load_defaults_from_config() # configuration parameters
SR = _CFG["SR"]
N_FFT = _CFG["N_FFT"]
HOP = _CFG["HOP"]
MFCC_N = _CFG["MFCC_N"]
ROLLOFF_PERCENT = _CFG["ROLLOFF_PERCENT"]

def _agg_stats(x: np.ndarray) -> Tuple[float, float]:
    """Compute mean and standard deviation for a 1-d feature array.

    Converts NaN/inf values to 0 before computing statistics to avoid
    propagation of invalid values.
    """
    x = np.nan_to_num(x, nan=0.0, posinf=0.0, neginf=0.0)
    return float(np.mean(x)), float(np.std(x))

def extract_features(path: str,
                     sr: int = 22050,
                     n_fft: int = 2048,
                     hop_length: int = 512,
                     n_mfcc: int = 13,
                     rolloff_percent: float = 0.85) -> np.ndarray:
    """Extract a fixed-length feature vector from an audio file.

    The returned vector concatenates aggregated statistics (mean,std)
    for MFCCs, chroma, spectral contrast and a few other spectral
    descriptors plus estimated tempo. The shape is (N,) where N is
    deterministic given the parameters.

    Parameters mirror those used elsewhere in the notebooks so the
    function can be called without passing values.
    """

    y, sr = librosa.load(path, sr=sr, mono=True)
    S = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length))

    # --- MFCC ---
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, hop_length=hop_length)
    mfcc_stats = [val for i in range(n_mfcc) for val in _agg_stats(mfcc[i])]

    # --- Chroma ---
    chroma = librosa.feature.chroma_stft(S=S, sr=sr, hop_length=hop_length)
    chroma_stats = [val for i in range(chroma.shape[0]) for val in _agg_stats(chroma[i])]

    # --- Spectral Contrast ---
    contrast = librosa.feature.spectral_contrast(S=S, sr=sr, hop_length=hop_length)
    contrast_stats = [val for i in range(contrast.shape[0]) for val in _agg_stats(contrast[i])]

    # --- Centroid, Bandwidth, Rolloff, ZCR, RMS ---
    centroid_stats = _agg_stats(librosa.feature.spectral_centroid(S=S, sr=sr)[0])
    bandwidth_stats = _agg_stats(librosa.feature.spectral_bandwidth(S=S, sr=sr)[0])
    rolloff_stats = _agg_stats(librosa.feature.spectral_rolloff(S=S, sr=sr, roll_percent=rolloff_percent)[0])
    zcr_stats = _agg_stats(librosa.feature.zero_crossing_rate(y, hop_length=hop_length)[0])
    rms_stats = _agg_stats(librosa.feature.rms(S=S)[0])

    # --- Tempo (BPM) ---
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr, hop_length=hop_length)
    tempo = 0.0 if np.isnan(tempo) else float(tempo)

    # Concatenate all features into a single vector
    features = np.array(
        mfcc_stats +
        chroma_stats +
        contrast_stats +
        list(centroid_stats) +
        list(bandwidth_stats) +
        list(rolloff_stats) +
        list(zcr_stats) +
        list(rms_stats) +
        [tempo],
        dtype=np.float32,
    )
    
    return features
