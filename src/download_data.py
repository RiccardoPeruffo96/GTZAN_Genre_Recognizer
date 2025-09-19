######################
### NOT TESTED YET ###
######################

# Download zip in 'data/GTZAN.zip' (no unzip)
import os
import zipfile

# Script copied from Kaggle documentation 
try:
    try:
        __import__(kagglehub)
    except ImportError:
        if INSTALL_MISSING_LIBRARIES:
            print(f"Installing kagglehub library...")
            !python "{script_download_missing_library}" "kagglehub"
    import kagglehub
except ImportError:
    raise ImportError("Mandatory libraries not founds: kagglehub -> Run the following command to install it: pip install kagglehub")

# Step 1
_DEFAULTS = { "INSTALL_MISSING_LIBRARIES": True, "REPOSITORY": "achgls/gtzan-music-genre" }

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
                out["INSTALL_MISSING_LIBRARIES"] = cfg.get("install_missing_libraries", _DEFAULTS["REPOSITORY"])
                out["REPOSITORY"] = cfg.get("repository", _DEFAULTS["REPOSITORY"])
                return out
        except Exception:
            # Ignore and continue to fallback
            continue
    return _DEFAULTS.copy()

# Load defaults at import time
_CFG = _load_defaults_from_config() # configuration parameters
DATA_DIR = _CFG["DATA_DIR"]
INSTALL_MISSING_LIBRARIES = _CFG["INSTALL_MISSING_LIBRARIES"]
REPOSITORY = _CFG["REPOSITORY"]

os.makedirs('data', exist_ok=True)
zip_path = os.path.join('data', 'GTZAN.zip')
kagglehub.login(username="your_username", key="your_api_key")
downloaded_path = kagglehub.dataset_download(REPOSITORY, path=zip_path, unzip=False)
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
extract_dir = os.path(DATA_DIR)
os.makedirs(extract_dir, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print("Dataset downloaded path:", zip_path)
print("Dataset extracted path:", extract_dir)