import keras
from keras.models import Sequential
from keras.layers import Activation
from keras.layers import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
import numpy as np
from random import randint
from sklearn.preprocessing import MinMaxScaler

#create mock data for TRAINING
train_lables = []
train_samples = []

for i in range(50):
    random_younger = randint(13, 64)
    train_samples.append(random_younger)
    train_lables.append(1)

    random_older = randint(65, 100)
    train_samples.append(random_older)
    train_lables.append(0)

for i in range(1000):
    random_younger = randint(13, 64)
    train_samples.append(random_younger)
    train_lables.append(0)

    random_older = randint(65, 100)
    train_samples.append(random_older)
    train_lables.append(1)

#convert to numpy arrays
train_lables = np.array(train_lables)
train_samples = np.array(train_samples)

#scale to 0-1
scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_samples = scaler.fit_transform((train_samples).reshape(-1,1))


#create mock data for PREDICTIONS/TESTING
test_lables = []
test_samples = []

for i in range(10):
    random_younger = randint(13, 64)
    test_samples.append(random_younger)
    test_lables.append(1)

    random_older = randint(65, 100)
    test_samples.append(random_older)
    test_lables.append(0)

for i in range(200):
    random_younger = randint(13, 64)
    test_samples.append(random_younger)
    test_lables.append(0)

    random_older = randint(65, 100)
    test_samples.append(random_older)
    test_lables.append(1)

#convert to numpy arrays
test_lables = np.array(test_lables)
test_samples = np.array(test_samples)

#scale to 0-1
scaler2 = MinMaxScaler(feature_range=(0,1))
scaled_test_samples = scaler2.fit_transform((test_samples).reshape(-1,1))

#-------------------Create the model (layers)---------------------
model = Sequential([
    Dense(16, input_shape=(1,), activation='relu'),
    Dense(32, activation='relu'),
    Dense(2, activation='softmax')
])

#print out the details of the model
#model.summary()

#--------------------------Compile and Train--------------------------

#compile the model
model.compile(Adam(lr=.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(scaled_train_samples, #training data
train_lables,                   #labels/classes
validation_split=0.1,           #splits the training data: 90% training, 10% validation
batch_size=10,                  #takes 10 samples at a time for training
epochs=20,                      #How many "rounds" of training
shuffle=True,                   #Shuffles the data = better training
verbose=2)                      #Shows a progress bar and "Epoch 1/20..2/20..3/20.." etc. | 0=shows nothing | 1=shows the progress bar

#--------------------------Predictions-----------------------------

predictions = model.predict(scaled_test_samples, batch_size=10, verbose=0)

""" for i in predictions:
    print(i) """

rounded_predictions = model.predict_classes(scaled_test_samples, batch_size=10, verbose=0)

""" for i in rounded_predictions:
    print(i) """

#-------------------------Create Confusion Matrix---------------------------

from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt

cm = confusion_matrix(test_lables, rounded_predictions)

def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):

    #This fn prints and plots the confusion matrix. Normalization can be applied by setting 'normalize=True'.

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print('Normalized confusion matrix')
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                horizontalalignment='center',
                color='white' if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

#----------------- Use Confusion Matrix---------------------

cm_plot_labels = ['no_side_effects', 'had_side_effects']                #Imaginary case, different aged people had or had not side effects
plot_confusion_matrix(cm, cm_plot_labels, title='Confusion Matrix')     #from particular medicines
plt.show()

#-------------------------Save Model, 3 different ways--------------------

""" 1.
model.save('medical_trial_model.h5') Saves the architechture, the weights, training conf
                                    (as loss, optimizer), the state of the optimizer so
                                    you can continue from where you left last time

from keras.models import load_model
new_model = load_model('medical_trial_model.h5')

new_model.summary()

2.
model.to_json() if you only need the architechture

3.
model.save_weights() for only weights of the model """
