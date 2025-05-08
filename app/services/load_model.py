import tensorflow as tf
import os
import requests
import tempfile

async def load_model():
    model_url = os.getenv('MODEL_URL')
    if not model_url:
        raise ValueError("MODEL_URL environment variable is not set")

    response = requests.get(model_url)
    response.raise_for_status()

    # Simpan model ke file temporer
    with tempfile.NamedTemporaryFile(suffix=".keras", delete=False) as tmp:
        tmp.write(response.content)
        tmp_path = tmp.name

    # Load model dari file temporer
    model = tf.keras.models.load_model(tmp_path)
    return model
