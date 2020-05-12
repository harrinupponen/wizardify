# Details of the ML part of the project

### The Idea

Using Tensorflow and Keras deep learning to train a convolutional neural network model to predict
which Dungeons & Dragons class the user's selfie looks like the most.

There are 12 classes to compare with.

### Prerequisites (at the moment)

- h5py 2.10.0
- numpy 1.18.2
- Pillow 7.0.0
- pip 20.0.2
- Python 3.6.8
- (Python) setuptools 46.1.3
- tensorflow 2.0.0

### Data augmentation and preparation

First we surfed the internet for two male and two female pictures of every twelve DnD-class that showed the whole character. We then cropped those pictures by hand to get four more pictures of face area.

The eight pictures of every class were then put through the augmentation-algorithm, that created about 425 training images, 230 validation images and 96 test images of every class. See the [`final_data_tree.txt`](https://github.com/harrinupponen/wizardify/blob/master/final-model/final_data_tree.txt) for details.

The augmentation was done by iterating through every classes source folder and the eight pictures in them. The pictures ran nine iterations for training, five for validation and two for testing. Each iteration added to the values of the augmentation settings, so that the data would be consistent but at the same time varying. Then the algorithm iterated five times per each setting, so that every picture would go through all the stages. All five versions were saved to hard drive. The details of this process can be seen in [`data_augmentation.py`](https://github.com/harrinupponen/wizardify/blob/master/final-model/data_augmentation.py).

For the augmentation and details for the ImageDataGenerator processes check out:

[ImageDataGenerator Class](https://keras.io/api/preprocessing/image/)

### Creating and fine tuning model (MobileNet) to own use + save the model

Specified comments in the [`train_model.py`](https://github.com/harrinupponen/wizardify/blob/master/final-model/train_model.py)

But in a nutshell:

Create paths for training and validation data, prepare the data, import the pre-trained model, fine-tune it for own purposes, compile and fit the
new model and save it.

### Loading the model

We have the [`routes.py`](https://github.com/harrinupponen/wizardify/blob/latest/app/routes.py) in `app/` and the model
`final_mn_dnd_model.h5` in the root of the project.
Then in the routes.py there is a function to load the model:

```python
from tensorflow.keras.models import load_model
.
.
.
def get_model():
    global model
    model = load_model('final_mn_dnd_model.h5')
    print(' * Model loaded!')
```

### User's image preparation for the model

Check out the [`routes.py`](https://github.com/harrinupponen/wizardify/blob/latest/app/routes.py) for the details
