import tensorflow as tf

# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
# import numpy as np
# from IPython.display import Image


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

print(x_train.shape)
print(x_test.shape)

x_val = x_train[50000:60000]
x_train = x_train[0:50000]
y_val = y_train[50000:60000]
y_train = y_train[0:50000]

print("train data has " + str(x_train.shape[0]) + " samples")
print("every train data is " + str(x_train.shape[1])
      + " * " + str(x_train.shape[2]) + " image")
print("validation data has " + str(x_val.shape[0]) + " samples")
print("every train data is " + str(x_val.shape[1])
      + " * " + str(x_train.shape[2]) + " image")
# sample to show gray scale values
print(x_train[0][8])
# sample to show labels for first train data to 10th train data
print(y_train[0:9])
print("test data has " + str(x_test.shape[0]) + " samples")
print("every test data is " + str(x_test.shape[1])
      + " * " + str(x_test.shape[2]) + " image")

x_train = x_train.reshape(50000, 784)
x_val = x_val.reshape(10000, 784)
x_test = x_test.reshape(10000, 784)

print(x_train.shape)
print(x_test.shape)

x_train[0]

x_train = x_train.astype('float32')
x_val = x_val.astype('float32')
x_test = x_test.astype('float32')

gray_scale = 255
x_train /= gray_scale
x_val /= gray_scale
x_test /= gray_scale

num_classes = 10
y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_val = tf.keras.utils.to_categorical(y_val, num_classes)
y_test = tf.keras.utils.to_categorical(y_test, num_classes)

y_train

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])


def mlp(x):
    # hidden layer1
    w1 = tf.Variable(tf.random_uniform([784, 256]))
    b1 = tf.Variable(tf.zeros([256]))
    h1 = tf.nn.relu(tf.matmul(x, w1) + b1)

    # hidden layer2
    w2 = tf.Variable(tf.random_uniform([256, 128]))
    b2 = tf.Variable(tf.zeros([128]))
    h2 = tf.nn.relu(tf.matmul(h1, w2) + b2)

    # output layer
    w3 = tf.Variable(tf.random_uniform([128, 10]))
    b3 = tf.Variable(tf.zeros([10]))
    logits = tf.matmul(h2, w3) + b3

    return logits


logits = mlp(x)

loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
    logits=logits, labels=y))

train_op = tf.train.AdamOptimizer(learning_rate=0.01).minimize(loss_op)

# initialize
init = tf.global_variables_initializer()

# train hyperparameters
epoch_cnt = 30
batch_size = 1000
iteration = len(x_train) // batch_size

# Start training
with tf.Session() as sess:
    # Run the initializer
    sess.run(init)
    for epoch in range(epoch_cnt):
        avg_loss = 0.
        start = 0;
        end = batch_size

        for i in range(iteration):
            _, loss = sess.run([train_op, loss_op],
                               feed_dict={x: x_train[start: end],
                                          y: y_train[start: end]})
            start += batch_size;
            end += batch_size
            # Compute average loss
            avg_loss += loss / iteration

        # Validate model
        preds = tf.nn.softmax(logits)  # Apply softmax to logits
        correct_prediction = tf.equal(tf.argmax(preds, 1), tf.argmax(y, 1))
        # Calculate accuracy
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        cur_val_acc = accuracy.eval({x: x_val, y: y_val})
        print("epoch: " + str(epoch) + ", validation accuracy: "
              + str(cur_val_acc) + ', loss: ' + str(avg_loss))

    # Test model
    preds = tf.nn.softmax(logits)  # Apply softmax to logits
    correct_prediction = tf.equal(tf.argmax(preds, 1), tf.argmax(y, 1))

    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print("[Test Accuracy] :", accuracy.eval({x: x_test, y: y_test}))