import os
from flask import Flask, url_for, send_from_directory, redirect, render_template, request
from app import app
from werkzeug.utils import secure_filename
import base64
import numpy as np
import io
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
# import form from app.forms and set route for upload

def get_model():
    global model
    model = load_model('final_mn_dnd_model.h5')
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

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__),"kuvat")
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/classes', methods=["GET"])
def classes():
    return render_template('classes.html')


@app.route('/about', methods=["GET"])
def about():
    with open("wizardify-about.txt", "r", encoding = "ISO-8859-1") as file:
        content = file.read()
    return render_template('about.html', content=content)

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
         # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return "failure at 1"
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            #flash('No selected file')
            return "failure at 2"
        if file and not allowed_file(file.filename):
           
            #filename to random string maybe. gotta keep extensions!
            # 
          ##  return redirect(url_for('uploaded_file', filename=filename))
            return "failure num 3"
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image = Image.open(file)
        processed_image = preprocess_image(image, target_size=(224, 224))
        prediction = model.predict(processed_image).tolist()
        
        #luodaan array jossa sort
        prediction_array = {
                'Barbarian': prediction[0][0],
                'Bard': prediction[0][1],
                'Cleric': prediction[0][2],
                'Druid': prediction[0][3],
                'Fighter': prediction[0][4],
                'Monk': prediction[0][5],
                'Paladin': prediction[0][6],
                'Ranger': prediction[0][7],
                'Rogue': prediction[0][8],
                'Sorcerer': prediction[0][9],
                'Warlock': prediction[0][10],
                'Wizard': prediction[0][11]
            }

        sorted_predictions = sorted(prediction_array.items(), key=lambda p: p[1], reverse=True)    
        
       
        return render_template('result.html', firstitem = sorted_predictions[0], predictions = sorted_predictions, fileurl = url_for('uploaded_file', filename=filename))