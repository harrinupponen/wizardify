import tensorflow as tf
import base64
import numpy as np
import io
from PIL import Image
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_model():
    global model
    model = load_model('mn_dnd_model.h5')
    print(' * Model loaded!')

def preprocess_image(image, target_size):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image = image.resize(target_size)
    image = img_to_array(image)
    image = image.astype('float32')
    image = (image - 127.5) / 127.5
    image = np.expand_dims(image, axis=0)

    return image

print(' * Loading Keras model...')
get_model()

@app.route('/predictdnd', methods=['POST'])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224, 224))
    prediction = model.predict(processed_image).tolist()
    
    response = {
        'prediction': {
            'barbarian': prediction[0][0],
            'bard': prediction[0][1],
            'cleric': prediction[0][2],
            'druid': prediction[0][3],
            'fighter': prediction[0][4],
            'mage': prediction[0][5],
            'monk': prediction[0][6],
            'paladin': prediction[0][7],
            'rogue': prediction[0][8],
            'sorcerer': prediction[0][9],
            'warlock': prediction[0][10],
            'wizard': prediction[0][11]
        }
    }
    return jsonify(response)