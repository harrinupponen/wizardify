import cv2
import tensorflow as tf
CATEGORIES = ["men", "women"]
def prepare(file):
    IMG_SIZE_x = 40
    IMG_SIZE_y = 60
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE_x, IMG_SIZE_y))
    return new_array.reshape(-1, IMG_SIZE_x, IMG_SIZE_y, 1)
model = tf.keras.models.load_model("CNN.model")
image = "hnupponen.png" #your image path
prediction = model.predict([image])
prediction = list(prediction[0])
print(CATEGORIES[prediction.index(max(prediction))])