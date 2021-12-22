import tensorflow as tf
import numpy as np
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
tf.model.add(tf.keras.layers.Dense(input_dim=3, units=3))
tf.model.add(tf.keras.layers.Dense(input_dim=3, units=1))# 4개 입력 3개로 출력 바이어스(y절편) 사용
tf.model.add(tf.keras.layers.Activation('softmax'))  # 활성화 함수 softmax

tf.model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.SGD(lr=1e-5), metrics=['accuracy'])
# 모델 설정 loss 함수 categorical_crossentropy 최적화 경사하강법 검증 accuracy
tf.model.summary()  # 요약 출력

history = tf.model.fit(study_x, study_y, epochs=2000)  # 학습

print("모델 생성")
print("테스트 전용 데이터셋 값 예측 시작")
for i in range(0, 29):
    print("예측된 값: ", tf.model.predict(np.array([[test1[i][0], test1[i][1], test1[i][2]]])), "  실제 값 : ", test1[i][3])

print("학습된 데이터셋 값 예측 시작")
for i in range(0, 29):
    print("예측된 값: ", tf.model.predict(np.array([[test2[i][0], test2[i][1], test2[i][2]]])), "  실제 값 : ", test2[i][3])

print("모델 생성")
tf.model.save('model.h5')
