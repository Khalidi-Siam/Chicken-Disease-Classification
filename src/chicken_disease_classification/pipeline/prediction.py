import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename


    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        img = image.load_img(self.filename, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)


        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)[0]
        
        if predicted_class == 0:
            prediction = "Coccidiosis"
        else:
            prediction = "Healthy"

        return [{"image" : prediction}]

