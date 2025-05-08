from keras.preprocessing import image
from PIL import Image
import numpy as np
import io

def predict_image(model, file):
    img = Image.open(io.BytesIO(file.read())).convert("RGB")
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = model.predict(img_array)
    confidence = float(prediction[0][0])

    if confidence < 0.5:
        result = "Batik Luar Madura"
        suggestion = "Ini adalah batik yang berasal dari luar Madura."
    else:
        result = "Batik Madura"
        suggestion = "Ini adalah batik yang berasal dari Madura."

    return result, confidence, suggestion
