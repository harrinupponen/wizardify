import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # Poistaa errorviestin, ei korjaa mitään

DATADIR = "C:/Users/valtt/Desktop/Kedustajat"
TESTDATADIR = "C:/Users/valtt/Desktop/pics"
CATEGORIES = ["Mies", "Nainen"]

IMG_SIZE_X = 140 # Kuvakoko
IMG_SIZE_Y = 140 # Kuvakoko

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

test_data = [] 
def create_test_data(): # Tämä tekee datan
    for category in CATEGORIES:
        path = os.path.join(TESTDATADIR, category) # polku noihin mies ja nainen kansioihin
        class_num = CATEGORIES.index(category) # tekee kategorioille oman numeron (0 ja 1 tässä tapauksessa)
        for img in os.listdir(path): # käy kaikki kuvat läpi
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE) # muuttaa kuvan harmaaksi
                new_array = cv2.resize(img_array, (IMG_SIZE_X, IMG_SIZE_Y)) # vaihtaa kuvakoon
                test_data.append([new_array, class_num]) # syöttää käsitellyt kuvat trainingdataan 
            except Exception as e:
                pass

create_test_data()

import random
random.shuffle(test_data) # sekoittaa datan, jotta koulutus on tehokkaampaa


Z = []
o = []

for features, label in test_data:
    Z.append(features)
    o.append(label)

Z = np.array(Z).reshape(-1, IMG_SIZE_X, IMG_SIZE_Y, 1)
o = np.array(o)

train_images = X/255.0
train_labels = y
test_images = Z/255.0
test_labels = o

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(IMG_SIZE_X,IMG_SIZE_Y,1)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(2, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=60)

test_loss, test_acc = model.evaluate(test_images, test_labels)

print("Tested acc:", test_acc)

prediction = model.predict(test_images)

# print(prediction[0])
# print(np.argmax(prediction[0]))
# print(class_names[np.argmax(prediction[0])])

for i in range(13):
    plt.grid(False)
    plt.imshow(np.array(test_images[i]).reshape(IMG_SIZE_Y, IMG_SIZE_X), cmap="gray")
    plt.xlabel("Actual: " + CATEGORIES[test_labels[i]])
    plt.title("Prediction: " + CATEGORIES[np.argmax(prediction[i])])
    plt.show()
    #OpenCV