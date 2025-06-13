# 🌿 LeafCheck API With FastAPI

Backend ini dibangun menggunakan FastAPI dan berfungsi untuk melakukan prediksi penyakit pada gambar daun jagung menggunakan model Convolutional Neural Network (CNN) yang telah dilatih.

REST API untuk mendeteksi penyakit pada daun tanaman menggunakan model CNN dan FastAPI.

## 🚀 Cara Menjalankan di Lokal

1. **Persiapan**
   
Pastikan kamu sudah menginstall:
- Python 3.8 atau lebih tinggi
- pip
- virtualenv (opsional tapi disarankan) supaya tidak tercampur dengan project python lain

Saya menggunakan venv, ini merupakan tool bawaan Python untuk membuat virtual environment langkah-langkahnya seperti berikut :

- Buat virtual environment pada terminal
  
``` bash
python -m venv venv
```

- Aktifkan virtual environment di cmd/powershell
  
``` bash
venv\Scripts\activate
```

2. **Clone repo ini**

`git clone https://github.com/aditiaprabowo3/api-leafcheck`.
   
4. **Install dependencies**
   
```bash
pip install -r requirements.txt
```
   
5. **Download Model Terlatih**

Model_jagung.h5 tidak disimpan langsung di repo karena ukurannya besar. Silakan unduh model secara manual melalu tautan di bawah ini:

https://drive.google.com/file/d/1TsGy9PhXoGXAwBuJ8vVPfCA5e0B2WjTD/view?usp=sharing

5. **Letakkan hasil unduhan di folder model**
   
Model yang sudah terdownload di letakan pada folder model, sebelumnya kamu harus membuat folder dengan nama **model** masukan model yang udah di download ke folder tersebut.

7. **Struktur direktori yang dibutuhkan di akhir**
   
```
api-leafcheck-main/
├── app/
│   ├── __init__.py
│   ├── download_model.py
│   ├── main.py
│   ├── model.py
│   └── schemas.py
├── model/
│   └── model_jagung.h5
├── README.md
```

8. **Menjalankan API Pada Lokal**
   ```bash
   uvicorn main:app --reload
   ```
API akan tersedia di http://localhost:8000.

Akses link yang didapat setelah menjalankan code tadi seprti contoh http://127.0.0.1:8000, dan setelah itu tambahkan '\docs' yang akan diarahkan untuk mengetes api yang kita buat pada fastapi
