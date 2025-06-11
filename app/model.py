from app.download_model import download_model
import tensorflow as tf
import numpy as np
from PIL import Image
import io

label_info = {
    0: {
        "penyakit": "Karat Daun (Common Rust)",
        "penjelasan": "Disebabkan oleh jamur Puccinia sorghi, muncul bintik-bintik kemerahan seperti karat.",
        "solusi": "Gunakan fungisida seperti propiconazole, dan tanam varietas tahan karat."
    },
    1: {
        "penyakit": "Hawar Daun (Northern Leaf Blight)",
        "penjelasan": "Disebabkan oleh jamur Exserohilum turcicum, gejala berupa bercak lonjong memanjang.",
        "solusi": "Aplikasi fungisida seperti mancozeb atau azoxystrobin dan pilih varietas tahan penyakit."
    },
    2: {
        "penyakit": "Daun Sehat",
        "penjelasan": "Daun jagung dalam kondisi sehat, tanpa gejala penyakit.",
        "solusi": "Lanjutkan perawatan dan pemupukan rutin."
    },
    3: {
        "penyakit": "Bercak Daun (Gray Leaf Spot)",
        "penjelasan": "Disebabkan oleh jamur Cercospora zeae-maydis, muncul bercak-bercak abu-abu memanjang.",
        "solusi": "Gunakan fungisida berbasis strobilurin atau triazol, dan lakukan rotasi tanaman."
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