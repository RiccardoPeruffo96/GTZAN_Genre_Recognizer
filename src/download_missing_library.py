import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(description="Instal package with pip")
parser.add_argument("package", help="Name of the package to install")
args = parser.parse_args()

subprocess.check_call([sys.executable, "-m", "pip", "install", args.package])