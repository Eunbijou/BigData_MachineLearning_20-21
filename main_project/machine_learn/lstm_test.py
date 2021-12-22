from tensorflow.keras.layers import Dense, Dropout, LSTM, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
import pandas as pd
import numpy as np
import csv

input_file = 'input.csv'

study = np.loadtxt("study.csv", delimiter=",")
study_x = study[:, 0:-1]
study_y = study[:, [-1]]

test1 = np.loadtxt("test1.csv", delimiter=",")
test1_x = test1[:, 0:-1]
test1_y = test1[:, [-1]]

# test1 = []
# with open('test1.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, quotechar='|')
#     for row in spamreader:
#         test1.append(row)
#         test1 = [list(map(float, x)) for x in test1]

test2 = []
with open('test2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    for row in spamreader:
        test2.append(row)
        test2 = [list(map(float, x)) for x in test2]


def create_model(input_length):
    print ('Creating model...')
    model = Sequential()
    model.add(Embedding(input_dim = 3, output_dim = 13, input_length = input_length))
    model.add(LSTM(output_dim=256, activation='sigmoid', inner_activation='hard_sigmoid', return_sequences=True))
    model.add(Dropout(0.5))
    model.add(LSTM(output_dim=256, activation='sigmoid', inner_activation='hard_sigmoid'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))

    print ('Compiling...')
    model.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])
    return model

model = create_model(len(study_x[0]))

print ('Fitting model...')
hist = model.fit(study_x, study_y, batch_size=64, nb_epoch=10, validation_split = 0.1, verbose = 1)

score, acc = model.evaluate(test1_x, test, batch_size=1)
print('Test score:', score)
print('Test accuracy:', acc)