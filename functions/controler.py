import tensorflow as tf
import numpy as np

MODEL_PATH = "../reconhecimentoImagem/model/reconhecimento_incendio.keras"

class_names = ["incendio", "naoIncendio"]

IMG_HEIGHT = 224
IMG_WIDTH = 224


def predict_image(imgPath):
    import tensorflow as tf

    model = tf.keras.models.load_model(MODEL_PATH)

    img = tf.keras.preprocessing.image.load_img(
        imgPath, target_size=(IMG_HEIGHT, IMG_WIDTH)
    )

    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) 

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    return class_names[np.argmax(score)], 100 * np.max(score)