# 🌿 LeafCheck API - Backend (FastAPI)

Backend ini dibangun menggunakan FastAPI dan berfungsi untuk melakukan prediksi penyakit pada gambar daun jagung menggunakan model Convolutional Neural Network (CNN) yang telah dilatih.

REST API untuk mendeteksi penyakit pada daun tanaman menggunakan model CNN dan FastAPI.

## 🚀 Cara Menjalankan di Lokal

1. **Persiapan**
Pastikan kamu sudah menginstall:
- Python 3.8 atau lebih tinggi
- pip
- virtualenv (opsional tapi disarankan)

2. **Kloning repo ini**  `git clone https://github.com/aditiaprabowo3/api-leafcheck`.
   
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   
4. Download Model Terlatih

Model_jagung.h5 tidak disimpan langsung di repo karena ukurannya besar. Silakan unduh model secara manual melalu tautan di bawah ini:

https://drive.google.com/file/d/1TsGy9PhXoGXAwBuJ8vVPfCA5e0B2WjTD/view?usp=sharing

5. Letakkan hasil unduhan di:
Unudhan di letakan pada folder model, sehingga kamu harus membuat folder model terlebih dahulu selanjutkan masukan model yang udah di download ke folder tersebut.

6. Struktur direktori yang dibutuhkan di akhir:
api-leafcheck/
├── app/
    ├── __init__.py
    ├── download_model.py
│   ├── main.py
│   ├── model.py
│   └── schemas.py
├── model/
│   └── model_jagung.h5 
├── requirements.txt

7. Jalankan API
   ```bash
   uvicorn main:app --reload
   
8. Akses link yang didapat setelah menjalankan code tadi seprti contoh http://127.0.0.1:8000, dan setelah itu tambahkan '\docs' dan setelah itu kita bsia mengetes api yang kita buat pada fastapi

9. Endpoint Utama
    
POST /predict

