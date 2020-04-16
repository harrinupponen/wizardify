import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#Create paths to data
train_path = 'dnd_classes/train'
valid_path = 'dnd_classes/valid'
test_path = 'dnd_classes/test'

#Prepare image data for the model
train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet.preprocess_input).flow_from_directory(train_path, target_size=(224, 224), batch_size=10)
valid_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet.preprocess_input).flow_from_directory(valid_path, target_size=(224, 224), batch_size=4)
test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet.preprocess_input).flow_from_directory(test_path, target_size=(224, 224), batch_size=60)

#Import the ready VGG16-model
mobile = tf.keras.applications.mobilenet.MobileNet()

x = mobile.layers[-6].output
predictions = Dense(12, activation='softmax')(x)
model = Model(inputs=mobile.input, outputs=predictions)

for layer in model.layers[:-5]:
    layer.trainable=False

model.compile(Adam(lr=.0001), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit_generator(train_batches, steps_per_epoch=60, validation_data=valid_batches, validation_steps=10, epochs=5, verbose=2)

model.save('mn_dnd_model.h5')