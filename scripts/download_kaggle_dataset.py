import os
import subprocess

DATASET_NAME = "zynicide/wine-reviews"  # sample dataset
OUTPUT_DIR = "data/raw"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Downloading dataset from Kaggle...")
subprocess.run([
    "kaggle", "datasets", "download",
    "-d", DATASET_NAME,
    "-p", OUTPUT_DIR
], check=True)

print("Download completed.")
