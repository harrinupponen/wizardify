import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

DATADIR = "C:/Users/valtt/Desktop/Koulujutut/AMK/Ohjelmistoprojekti II/wizardify/Kedustajat" # Vaihda tämä oman koneen polkuun (pullaa gitistä omalle koneelle, en osannut luoda polkua gitiin, koska polussa pitää käyttää etukenoa ja gittiplolusta tulee mies- ja naiskansioille polkuun takakeno joten ohjelma sekoaa)
CATEGORIES = ["Mies", "Nainen"]

IMG_SIZE_X = 40 # Kuvakoko
IMG_SIZE_Y = 60 # Kuvakoko

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

create_training_data() # kutsuu funktiota
print(len(training_data)) # näyttää montako kuvaa on datassa, tämän voi kkommentoida pois

import random
random.shuffle(training_data) # sekoittaa datan, jotta koulutus on tehokkaampaa

for sample in training_data[:5]: # tämä tulostaa 5 kpl näytteitä datasta, eli sample[1] on kategoria (0 mies tai 1 nainen) ja sample[0] näyttää kyseisen kuvan
    print(sample[1])
    plt.imshow(sample[0], cmap="gray")
    plt.show()

# alla oleva tallentaa datan, en ole varma toimiiko tämä

# X = []
# y = []

# for features, label in training_data:
#     X.append(features)
#     y.append(label)

# x = np.array(X).reshape(-1, IMG_SIZE_X, IMG_SIZE_Y, 1)

# import pickle

# pickle_out = open("X.pickle", "wb")
# pickle.dump(X, pickle_out)
# pickle_out.close()

# pickle_out = open("y.pickle", "wb")
# pickle.dump(y, pickle_out)
# pickle_out.close()

# pickle_in = open("X.pickle", "rb")
# X = pickle.load(pickle_in)

# X[1]

    
