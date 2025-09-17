######################
### NOT TESTED YET ###
######################

# Script copied from Kaggle documentation 
try:
    import kagglehub
except ImportError:
    raise ImportError("Mandatory libraries not founds: kagglehub -> Run the following command to install it: pip install kagglehub")

# Download latest version
path = kagglehub.dataset_download("achgls/gtzan-music-genre")

print("Path to dataset files:", path)