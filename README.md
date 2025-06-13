# 🌿 LeafCheck API With FastAPI

Backend ini dibangun menggunakan FastAPI dan berfungsi untuk melakukan prediksi penyakit pada gambar daun jagung menggunakan model Convolutional Neural Network (CNN) yang telah dilatih.

REST API untuk mendeteksi penyakit pada daun tanaman menggunakan model CNN dan FastAPI.

Teknologi yang Digunakan
- Python
- FastAPI
- Railway

## 🚀 Cara Menjalankan API Secara Lokal

1. **Clone Repository**

```bash
git clone https://github.com/aditiaprabowo3/api-leafcheck.git
```

2. **Buat Virtual Environment**

Jalankan pada terminal
```bash
python -m venv venv
```

Jalankan pada cmd/powersheel untuk mengaktifkan
```bash
venv\Scripts\activate
```

3. **Install dependencies**
   
```bash
pip install -r requirements.txt
```
   
4. **Download Model Terlatih**

Model tidak disimpan di repo karena ukurannya besar. Unduh file .h5 melalui link berikut:

🔗 https://drive.google.com/file/d/1TsGy9PhXoGXAwBuJ8vVPfCA5e0B2WjTD/view?usp=sharing

5. **Tempatkan Model**
   
- Buat folder dengan nama model untuk menyimpan model h5 
- Letakkan file model_jagung.h5 ke dalam folder model/

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

8. **Jalankan Server API**
   ```bash
   uvicorn main:app --reload
   ```
- Akses API di http://localhost:8000
- pada link tersebut tambahkan **\docs**
- Kunjungi dokumentasi interaktif FastAPI (Swagger UI)
- Mencoba mengetes api apakah sudah sesuai atau belum
