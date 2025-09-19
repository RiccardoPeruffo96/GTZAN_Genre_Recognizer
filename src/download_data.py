######################
### NOT TESTED YET ###
######################

# Download zip in 'data/GTZAN.zip' (no unzip)
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import zipfile
from os_path_management import adapt_path

# Step 1
_DEFAULTS = { "DATA_DIR": adapt_path("data/genres"), "DOWNLOAD_MISSING_DATASET": True, "INSTALL_MISSING_LIBRARIES": True, "REPOSITORY": "achgls/gtzan-music-genre" }

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
                # Validate and coerce types
                out = {}
                out["DATA_DIR"] = cfg.get("data_dir", _DEFAULTS["DATA_DIR"])
                out["DOWNLOAD_MISSING_DATASET"] = cfg.get("download_missing_dataset", _DEFAULTS["DOWNLOAD_MISSING_DATASET"])
                out["INSTALL_MISSING_LIBRARIES"] = cfg.get("install_missing_libraries", _DEFAULTS["INSTALL_MISSING_LIBRARIES"])
                out["REPOSITORY"] = cfg.get("repository", _DEFAULTS["REPOSITORY"])
                return out
        except Exception:
            # Ignore and continue to fallback
            continue
    return _DEFAULTS.copy()

# Load defaults at import time
_CFG = _load_defaults_from_config() # configuration parameters
DATA_DIR = _CFG["DATA_DIR"]
DOWNLOAD_MISSING_DATASET = _CFG["DOWNLOAD_MISSING_DATASET"]
INSTALL_MISSING_LIBRARIES = _CFG["INSTALL_MISSING_LIBRARIES"]
REPOSITORY = _CFG["REPOSITORY"]

# Script copied from Kaggle documentation 
try:
    try:
        importlib.import_module("kagglehub")
    except ImportError:
        if INSTALL_MISSING_LIBRARIES:
            print("Installing kagglehub via pip...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "kagglehub"])
    import kagglehub
except ImportError:
    raise ImportError("Mandatory libraries not founds: kagglehub -> Run the following command to install it: pip install kagglehub")

os.makedirs('data', exist_ok=True)
zip_path = os.path.join('data', 'GTZAN.zip')
#temporary credentials
#kagglehub.login(username="rporki", key="1b38f0653a251cf116c146989ba760df")
downloaded_path = kagglehub.dataset_download("achgls/gtzan-music-genre")
# move and rename file
if downloaded_path != zip_path:
    try:
        os.replace(downloaded_path, zip_path)
    except Exception:
        # fallback: copy and remove
        import shutil
        shutil.copy2(downloaded_path, zip_path)
        os.remove(downloaded_path)

# Extract in 'data/genres/'
zip_extract_dir = os.path.join('data', 'genres')
#extract_dir = os.path(DATA_DIR)
os.makedirs(zip_extract_dir, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(zip_extract_dir)

print("Dataset downloaded path:", zip_path)
print("Dataset extracted path:", zip_extract_dir)