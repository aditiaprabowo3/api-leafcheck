import tensorflow as tf

# Load model
model = tf.keras.models.load_model("model/model_jagung.h5")

# Tampilkan ringkasan model
model.summary()

# Atau lihat input shape langsung
print("Input shape:", model.input_shape)