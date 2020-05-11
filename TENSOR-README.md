# Actoress lookalike predictor app

### The Idea

Using Tensorflow and Keras deep learning to train a convolutional neural network model to predict
which Dungeons & Dragons class the user's selfie looks like the most.

There are 12 classes to compare with.

### Prerequisites (at the moment)

- Flask 1.1.1
- Flask-Cors 3.0.8
- gunicorn 20.0.4
- h5py 2.10.0
- numpy 1.18.2
- Pillow 7.0.0
- pip 20.0.2
- Python 3.6.8
- (Python) setuptools 46.1.3
- tensorflow 2.0.0
- Heroku for deploying

### Data augmentation and preparation

# Valtteri kirjotatko tämän:

I picked up 2 images of each actor/actress and augmented 25 + 25 images
for training and 5 + 5 images for validation. So for each actor/actress 50 training images and 10 validation images. Check out the `actoress-data-tree.txt`

For the augmentation and details for the ImageDataGenerator processes check out:

[ImageDataGenerator Class](https://keras.io/api/preprocessing/image/)

### Creating and fine tuning model (MobileNet) to own use + save the model

Specified comments in the `create_save_model.py`

But in a nutshell:

Create paths for training and validation data, prepare the data, import the pre-trained model, fine-tune it for own purposes, compile and fit the
new model and save it.

### Loading the model

I have the `app.py` and the model `mn_actoress_model2.h5` in the root of my project.
Then in the app.py there is a function to load the model:

```python
def get_model():
    global model
    model = load_model('mn_actoress_model2.h5')
    print(' * Model loaded!')
```

### User's image preparation for the model

Check out the `app.py` for the details
