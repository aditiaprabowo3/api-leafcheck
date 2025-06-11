from app.download_model import download_model
import tensorflow as tf
import numpy as np
from PIL import Image
import io

label_info = {
    0: {
        "penyakit": "Karat Daun (Common Rust)",
        "penjelasan": (
            "Disebabkan oleh jamur *Puccinia sorghi*. Gejala ini ditandai dengan bintik-bintik bulat berwarna oranye hingga cokelat "
            "seperti karat, menyebar di permukaan atas dan bawah daun. Infeksi parah menyebabkan daun mengering dan menurunkan hasil panen."
        ),
        "solusi": (
            "1. Gunakan fungisida seperti Propiconazole, Tebuconazole, atau campuran Triazole + Strobilurin (1–2 mL/L air).\n"
            "2. Tanam varietas jagung yang tahan terhadap karat daun.\n"
            "3. Lakukan rotasi tanaman dan bersihkan sisa tanaman terinfeksi untuk mencegah penyebaran.\n"
            "4. Kurangi kelembaban daun dengan mengatur irigasi dan jarak tanam."
        )
    },
    1: {
        "penyakit": "Hawar Daun (Northern Leaf Blight)",
        "penjelasan": (
            "Disebabkan oleh jamur *Exserohilum turcicum*. Gejala berupa bercak lonjong memanjang berwarna abu-abu atau cokelat, "
            "yang dapat bergabung dan menyebabkan kerusakan luas pada daun."
        ),
        "solusi": (
            "1. Semprot fungisida seperti Mancozeb (2–2.5 g/L air) atau Azoxystrobin (0.5–1 mL/L air).\n"
            "2. Gunakan varietas tahan penyakit untuk mencegah infeksi lanjutan.\n"
            "3. Lakukan rotasi tanaman dan hindari tanam jagung berturut-turut di lahan yang sama.\n"
            "4. Bakar sisa tanaman terinfeksi dan tanam lebih awal untuk menghindari musim lembap."
        )
    },
    2: {
        "penyakit": "Daun Sehat",
        "penjelasan": (
            "Daun jagung dalam kondisi sehat, hijau merata, tanpa gejala penyakit atau stres lingkungan."
        ),
        "solusi": (
            "1. Lanjutkan pemupukan secara rutin dengan NPK seimbang (misalnya 15-15-15).\n"
            "2. Pastikan pengairan cukup, terutama pada fase pembentukan tongkol.\n"
            "3. Kendalikan gulma dan pantau hama secara berkala.\n"
            "4. Jaga rotasi tanaman dan sanitasi lahan setelah panen."
        )
    },
    3: {
        "penyakit": "Bercak Daun (Gray Leaf Spot)",
        "penjelasan": (
            "Disebabkan oleh jamur *Cercospora zeae-maydis*. Gejalanya berupa bercak persegi panjang atau oval memanjang "
            "berwarna abu-abu sampai cokelat terang, sering terlihat sejajar dengan tulang daun."
        ),
        "solusi": (
            "1. Gunakan fungisida berbasis Strobilurin (Azoxystrobin, Trifloxystrobin) atau Triazol (Difenoconazole, Tebuconazole).\n"
            "2. Lakukan aplikasi fungisida pada saat gejala awal dan ulangi setiap 7–14 hari jika perlu.\n"
            "3. Gunakan varietas tahan Gray Leaf Spot.\n"
            "4. Lakukan rotasi tanaman dan bersihkan sisa tanaman untuk mencegah infeksi ulang.\n"
            "5. Atur jarak tanam agar sirkulasi udara lebih baik dan kelembaban daun berkurang."
        )
    }
}

def load_model():
    download_model()  # ini akan download kalau model belum ada
    model = tf.keras.models.load_model("model/model_jagung.h5")
    return model

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array.astype(np.float32)

def predict(model, image_bytes):
    input_data = preprocess_image(image_bytes)
    preds = model.predict(input_data)
    
    confidence = np.max(preds[0])
    class_index = np.argmax(preds[0])

    info = label_info.get(class_index, {
        "penyakit": "Tidak diketahui",
        "penjelasan": "Label tidak terdaftar di sistem.",
        "solusi": "Periksa kembali label atau latih ulang model."
    })

    # Tambahkan confidence ke hasil
    info_with_confidence = info.copy()
    info_with_confidence["confidence"] = float(confidence)

    return info_with_confidence