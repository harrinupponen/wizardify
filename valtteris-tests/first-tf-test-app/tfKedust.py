import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # Poistaa errorviestin, ei korjaa mitään

DATADIR = "C:/Users/valtt/Desktop/Koulujutut/AMK/Ohjelmistoprojekti II/wizardify/Kedustajat" # Vaihda tämä oman koneen polkuun (pullaa gitistä omalle koneelle, en osannut luoda polkua gitiin, koska polussa pitää käyttää etukenoa ja gittiplolusta tulee mies- ja naiskansioille polkuun takakeno joten ohjelma sekoaa)
CATEGORIES = ["Mies", "Nainen"]

IMG_SIZE_X = 100 # Kuvakoko
IMG_SIZE_Y = 160 # Kuvakoko

training_data = [] 
def create_training_data(): # Tämä tekee datan
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category) # polku noihin mies ja nainen kansioihin
        class_num = CATEGORIES.index(category) # tekee kategorioille oman numeron (0 ja 1 tässä tapauksessa)
        for img in os.listdir(path): # käy kaikki kuvat läpi
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE) # muuttaa kuvan harmaaksi
                new_array = cv2.resize(img_array, (IMG_SIZE_X, IMG_SIZE_Y)) # vaihtaa kuvakoon
                training_data.append([new_array, class_num]) # syöttää käsitellyt kuvat trainingdataan 
            except Exception as e:
                pass

create_training_data()

import random
random.shuffle(training_data) # sekoittaa datan, jotta koulutus on tehokkaampaa


X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE_X, IMG_SIZE_Y, 1)
y = np.array(y)

train_images = X/255.0
test_images = X/255.0
train_labels = y
test_labels = y

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(IMG_SIZE_X,IMG_SIZE_Y,1)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=45)

# test_loss, test_acc = model.evaluate(test_images, test_labels)

# print("Tesed acc:", test_acc)

prediction = model.predict(test_images)

# print(prediction[0])
# print(np.argmax(prediction[0]))
# print(class_names[np.argmax(prediction[0])])

for i in range(5):
    plt.grid(False)
    plt.imshow(np.array(test_images[i]).reshape(IMG_SIZE_Y, IMG_SIZE_X), cmap="gray")
    plt.xlabel("Actual: " + CATEGORIES[test_labels[i]])
    plt.title("Prediction: " + CATEGORIES[np.argmax(prediction[i])])
    plt.show()