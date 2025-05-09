import tensorflow as tf
import os
import requests
import tempfile
from tensorflow.keras.models import load_model

async def load_model():
    url = os.getenv('MODEL_URL')
    response = requests.get(url)
    response.raise_for_status()
    with tempfile.NamedTemporaryFile(suffix=".keras", delete=False) as tmp:
        tmp.write(response.content)
        tmp.flush()
        model = tf.keras.models.load_model(tmp.name)
    return model
