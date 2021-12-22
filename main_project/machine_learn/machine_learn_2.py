# 다중 입력 값
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import csv


study = np.loadtxt("study.csv", delimiter=",")
study_x = study[:, 0:-1]
study_y = study[:, [-1]]

test1 = []
with open('test1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    for row in spamreader:
        test1.append(row)
        test1 = [list(map(float, x)) for x in test1]

test2 = []
with open('test2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    for row in spamreader:
        test2.append(row)
        test2 = [list(map(float, x)) for x in test2]

tf.model = tf.keras.Sequential()

tf.model.add(tf.keras.layers.Dense(units=3, input_dim=3, activation='linear'))
tf.model.add(tf.keras.layers.Dense(units=1, input_dim=3, activation='linear'))
tf.model.compile(loss='mse', optimizer=tf.keras.optimizers.SGD(lr=1e-5), metrics=['categorical_accuracy'])
tf.model.summary()
history = tf.model.fit(study_x, study_y, epochs=3000000)

plt.plot(history.history['loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
print("모델 생성")
print("테스트 전용 데이터셋 값 예측 시작")
for i in range(0, 29):
    print("예측된 값: ", tf.model.predict(np.array([[test1[i][0], test1[i][1], test1[i][2]]])), "  실제 값 : ", test1[i][3])

print("학습된 데이터셋 값 예측 시작")
for i in range(0, 29):
    print("예측된 값: ", tf.model.predict(np.array([[test2[i][0], test2[i][1], test2[i][2]]])), "  실제 값 : ", test2[i][3])

print("모델 생성")
tf.model.save('model.h5')
