import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(description="Installa un pacchetto con pip")
parser.add_argument("package", help="Nome del pacchetto da installare")
args = parser.parse_args()

subprocess.check_call([sys.executable, "-m", "pip", "install", args.package])