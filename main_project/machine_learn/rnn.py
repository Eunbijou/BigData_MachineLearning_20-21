import tensorflow as tf
import numpy as np
import os
import pandas as pd
import random
import tqdm

epoch = 100
batch_size = 32
timesteps = 1
step_per_batch = 200
train_able = True


# True : train, False : False

def check_file(path):
    if not os.path.exists(path):
        os.makedirs(path)


train_path = './train/'
val_path = './validation/'
test_path = './test/'
result = './t1/'
save_weight = result + 'save_weights/'
save_backup = result + 'back_weights/'
test_result = result + 'test/'
check_file(result)
check_file(save_weight)
check_file(save_backup)
check_file(test_result)
train_data = os.listdir(train_path)
# val_path = os.listdir(val_path)
test_data = os.listdir(test_path)
data_list = []


def train_data_processing(data):
    t, f = data.shape
    start = random.randint(0, t - timesteps - 1)
    input_data = np.reshape(data[start: start + timesteps, 0:3], (1, timesteps, 3))
    result_data = np.reshape(data[start: start + timesteps, 2], (1, timesteps))
    for i in range(batch_size - 1):
        start = random.randint(0, t - timesteps)
        input_data = np.append(input_data, np.reshape(data[start: start + timesteps, 0:3], (1, timesteps, 3)), axis=0)
        result_data = np.append(result_data, np.reshape(data[start: start + timesteps, 3], (1, timesteps)), axis=0)
    return input_data, result_data


def test_data_processing(data):
    t, f = data.shape
    input_data = np.reshape(data[0:timesteps, 0:3], (1, timesteps, 3))
    result_data = np.reshape(data[0:timesteps, 3], (1, timesteps))
    for i in range(8, t - timesteps, 3):
        input_data = np.append(input_data, np.reshape(data[i: i + timesteps, 0:3], (1, timesteps, 3)), axis=0)
        result_data = np.append(result_data, np.reshape(data[i: i + timesteps, 3], (1, timesteps)), axis=0)
    return input_data, result_data


def activation(x):
    x[x < 0.5] = 0
    x[x >= 0.5] = 1
    return np.array(x).astype(np.int64)


def accuracy(x, y):
    count = 0
    x = np.ravel(x, order='C')
    y = np.ravel(y, order='C')
    for i, j in enumerate(x):
        if j == y[i]:
            count += 1
    return count


def get_model():
    with tf.device('/cpu:0'):
        x_input = tf.keras.layers.Input(shape=(timesteps, 3))
        x = x_input
        for i in range(2):
            x = tf.keras.layers.LSTM(8, return_sequences=True)(x)
        x_return = tf.keras.layers.Dense(13, activation='softmax')(x)

    return tf.keras.models.Model(x_input, x_return)


# def get_model():
#    x_input = tf.keras.layers.Input(shape=(timesteps, 48))
#    x = tf.keras.layers.Flatten()(x_input)
#    x = tf.keras.layers.Dense(timesteps/2)(x)
#    x = tf.keras.layers.Dense(timesteps)(x)
#
#    return tf.keras.models.Model(x_input, x)

def train():
    if train_able:
        for i, j in enumerate(train_data):
            data_list.append(pd.read_csv(train_path + j).to_numpy())
        model = get_model()
        model.summary()
        model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=0.0001))
        for i in tqdm.tqdm(range(epoch), desc="epoch", mininterval=1):
            pbar = tqdm.tqdm(range(step_per_batch), desc="training", mininterval=1)
            total_accuracy = 0
            total_loss = 0;
            for j in pbar:
                x, y = train_data_processing(data_list[random.randint(0, len(train_data) - 1)])
                total_loss += model.train_on_batch(x, y)
                data = model.predict(x)
                total_accuracy += accuracy(activation(data), y) / (timesteps * batch_size)
                pbar.set_description("epoch %d : %d, batch %d : %d, Loss : %0.4f, accuracy : %0.4f%%" % (
                epoch, i + 1, step_per_batch, j + 1, total_loss / (j + 1), total_accuracy / (j + 1) * 100))
            model.save_weights(save_weight)
        model.save_weights(save_backup)
        return 0
    else:
        for i, j in enumerate(test_data):
            data_list.append(pd.read_csv(test_path + j).to_numpy())
        model = get_model()
        model.summary()
        model.load_weights(save_weight)
        for i, j in enumerate(data_list):
            f = open(test_result + test_data[i] + ".txt", 'w')
            x, y = test_data_processing(j)
            data = model.predict(x)
            print(test_data[i] + ' : ' + str(accuracy(activation(data), y) / (timesteps * len(x)) * 100) + '%')
            for i in range(len(x)):
                f.write('predict :\t\t' + str(activation(data[i])) + '\n')
                f.write('groundtruth :\t' + str(y[i]) + '\n')
                f.write('\n')
            f.close()


train()