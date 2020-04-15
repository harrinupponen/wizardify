import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

gen = ImageDataGenerator(rotation_range=10, width_shift_range=0.1,
        height_shift_range=0.1, shear_range=0.15, zoom_range=0.1,
        channel_shift_range=10., horizontal_flip=True)

image_path = 'dnd_classes/samples/wizard_sample.jpg'

image = np.expand_dims(plt.imread(image_path), 0)

i = 0

for batch in gen.flow(image, batch_size=1,
    save_to_dir='dnd_classes/test/wizard',
    save_prefix='wizard',
    save_format='jpeg'):

    i += 1
    if i > 5:
        break