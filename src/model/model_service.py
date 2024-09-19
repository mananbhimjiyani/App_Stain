from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import numpy as np
from PIL import Image
import io

class ModelService:
    def __init__(self, model_path: str):
        self.model = load_model(model_path)
        self.classes = ['chocolate', 'eye liner', 'food', 'ink', 'lipstick', 'tea or coffee', 'wine']

    def preprocess_image(self, image_data: bytes) -> np.ndarray:
        img = Image.open(io.BytesIO(image_data))
        img = img.resize((64, 64))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        return img_array

    def predict(self, img_array: np.ndarray) -> str:
        result = self.model.predict(img_array)
        predicted_class = self.classes[np.argmax(result)]
        return predicted_class