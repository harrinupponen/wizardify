import os
from flask import Flask, url_for, send_from_directory, redirect, render_template, request
from app import app
from werkzeug.utils import secure_filename
# import form from app.forms and set route for upload

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
   return render_template('about.html')

@app.route('/upload', methods=['POST'])
def upload_file():
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
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #filename to random string maybe. gotta keep extensions!
            fullpath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(fullpath)
            return redirect(url_for('uploaded_file', filename=filename))

    return url_for('uploaded_file', filename=filename)

    
@app.route('/downlooood/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/result')
def result():
    return render_template('result.html')