import gdown
import os

def download_model():
    url = "https://drive.google.com/uc?id=1TsGy9PhXoGXAwBuJ8vVPfCA5e0B2WjTD"
    output_path = "model/model_jagung.h5"

    if not os.path.exists(output_path):
        os.makedirs("model", exist_ok=True)
        print("Mengunduh model dari Google Drive...")
        gdown.download(url, output_path, quiet=False)
    else:
        print("Model sudah tersedia secara lokal.")