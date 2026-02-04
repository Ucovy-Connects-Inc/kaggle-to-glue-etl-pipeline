import zipfile
import os

ZIP_PATH = "data/raw"
EXTRACT_PATH = "data/raw/extracted"

os.makedirs(EXTRACT_PATH, exist_ok=True)

for file in os.listdir(ZIP_PATH):
    if file.endswith(".zip"):
        zip_file = os.path.join(ZIP_PATH, file)
        print(f"Extracting {zip_file}...")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(EXTRACT_PATH)

print("Extraction completed. Files ready for processing.")
