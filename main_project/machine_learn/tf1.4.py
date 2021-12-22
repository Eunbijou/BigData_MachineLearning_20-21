import tensorflow as tf
import argparse
import os
import cv2
import numpy as np
from tqdm import tqdm


# train image resize and reshape
def image_resize(filename1, filename2):
    img_size = 224
    image = tf.io.read_file(filename1)
    image = tf.image.decode_png(image, channels=3)
    image = tf.image.resize(image, (img_size, img_size), method=2)
    re_image = tf.cast(image, tf.float32) / 255

    image_gt = tf.io.read_file(filename2)
    image_gt = tf.image.decode_png(image_gt, channels=1)
    image_gt = tf.image.resize(image_gt, (img_size, img_size), method=2)
    re_image_gt = tf.cast(image_gt, tf.float32) / 255

    return re_image, re_image_gt


def image_resize_t(filename):
    img_size = 224
    image = tf.io.read_file(filename)
    image = tf.image.decode_png(image, channels=3)
    image = tf.image.resize(image, (img_size, img_size), method=2)
    re_image = tf.cast(image, tf.float32) / 255

    image_gt = tf.io.read_file(filename)
    image_gt = tf.image.decode_png(image_gt, channels=1)
    re_image_gt = tf.image.resize(image_gt, (img_size, img_size), method=2)
    re_image_gt = tf.cast(re_image_gt, tf.float32) / 255

    return re_image, re_image_gt, image_gt


# paramatic-relu function
def prelu(_x, name):
    alphas = tf.get_variable(name, _x.get_shape()[-1], initializer=tf.constant_initializer(0.1), dtype=tf.float32,
                             trainable=True)
    pos = tf.nn.relu(_x)
    neg = alphas * (_x - abs(_x)) * 0.5

    return pos + neg


# residual block
def residual(_x, _demension):
    res = tf.layers.conv2d(_x, _demension, [3, 3], padding='SAME', activation=tf.nn.relu)
    res = tf.layers.conv2d(res, _demension, [3, 3], padding='SAME')
    res = _x + res

    return res


# model structure
def model(inputs_):
    # block1 (conv) 224x224
    conv1_1 = tf.layers.conv2d(inputs_, 64, [3, 3], padding='SAME', activation=tf.nn.relu)
    conv1_2 = tf.layers.conv2d(conv1_1, 64, [3, 3], padding='SAME', activation=tf.nn.relu)
    pool1_ = tf.layers.max_pooling2d(conv1_2, pool_size=[2, 2], strides=2)

    # block2 (res) 112x112
    conv2_1 = tf.layers.conv2d(pool1_, 128, [3, 3], padding='SAME', activation=tf.nn.relu)
    conv2_2 = tf.layers.conv2d(conv2_1, 128, [3, 3], padding='SAME', activation=tf.nn.relu)
    pool2_ = tf.layers.max_pooling2d(conv2_2, pool_size=[2, 2], strides=2)

    # block3 (res) 56x56
    conv3_1 = tf.layers.conv2d(pool2_, 256, [3, 3], padding='SAME', activation=tf.nn.relu)
    conv3_2 = tf.layers.conv2d(conv3_1, 256, [3, 3], padding='SAME', activation=tf.nn.relu)
    conv3_3 = tf.layers.conv2d(conv3_2, 256, [3, 3], padding='SAME', activation=tf.nn.relu)
    pool3_ = tf.layers.max_pooling2d(conv3_3, pool_size=[2, 2], strides=2)

    # block4 (res) 28x28
    conv4_1 = tf.layers.conv2d(pool3_, 512, [3, 3], padding='SAME', activation=tf.nn.relu)
    conv4_2 = tf.layers.conv2d(conv4_1, 512, [3, 3], padding='SAME', activation=tf.nn.relu)
    conv4_3 = tf.layers.conv2d(conv4_2, 512, [3, 3], padding='SAME', activation=tf.nn.relu)
    pool4_ = tf.layers.max_pooling2d(conv4_3, pool_size=[2, 2], strides=2)

    # block5 (res) 14x14
    conv5_1 = tf.layers.conv2d(pool4_, 1024, [3, 3], padding='SAME', activation=tf.nn.relu)
    conv5_2 = tf.layers.conv2d(conv5_1, 1024, [3, 3], padding='SAME', activation=tf.nn.relu)
    conv5_3 = tf.layers.conv2d(conv5_2, 1024, [3, 3], padding='SAME', activation=tf.nn.relu)

    conv5_3 = tf.layers.conv2d(conv5_3, 1024, [1, 1], padding='SAME', activation=tf.nn.relu)
    conv4 = tf.layers.conv2d(conv4_3, 512, [1, 1], padding='SAME', activation=tf.nn.relu)

    conv5 = tf.layers.conv2d_transpose(conv5_3, 512, [4, 4], [2, 2], padding='SAME')

    f1 = conv5 + conv4

    f1 = tf.layers.conv2d_transpose(f1, 256, [4, 4], [2, 2], padding='SAME')

    conv3 = tf.layers.conv2d(conv3_3, 256, [1, 1], padding='SAME', activation=tf.nn.relu)

    f2 = f1 + conv3

    outputs = tf.layers.conv2d_transpose(f2, 1, [8, 8], [4, 4], padding='SAME')

    return outputs


def train(parser):
    # train or test
    train_step = parser.train

    # setting
    img_size = parser.imgsize

    learning_rate = parser.learningrate
    epoch = parser.epoch
    batch_size = parser.batchsize
    path_text = str(parser.path)

    ckpt_path = './' + path_text + '/ckpt'
    result_path = './' + path_text + '/results'
    result_path_ = './' + path_text + '/results_MSRA10K'
    tensorboard_path = './' + path_text + '/tensorboard'

    train_img_path = './HKU-IS/imgs'
    train_gt_path = './HKU-IS/gt'
    test_img_path = './ECSSD/images'
    test_img_path_ = './MSRA10K/img'

    # check path or make path
    img_list = os.listdir(train_img_path)
    gt_list = os.listdir(train_gt_path)
    test_list = os.listdir(test_img_path)
    test_list_ = os.listdir(test_img_path_)

    # if not os.path.exists(dir_path):
    #    os.makedirs(dir_path)

    if not os.path.exists(ckpt_path):
        os.makedirs(ckpt_path)

    if not os.path.exists(result_path):
        os.makedirs(result_path)

    if not os.path.exists(result_path_):
        os.makedirs(result_path_)

    if not os.path.exists(tensorboard_path):
        os.makedirs(tensorboard_path)

    # setting train
    image_input = tf.placeholder(tf.float32, [None, img_size, img_size, 3])
    image_gt = tf.placeholder(tf.float32, [None, img_size, img_size, 1])

    image_out = model(image_input)

    # loss function
    loss_ = tf.reduce_mean(tf.square(image_out - image_gt))

    # setting optimizer / learning rate : 0.0001
    optim_ = tf.train.AdamOptimizer(learning_rate).minimize(loss_)

    # tensorboard
    sess = tf.Session()
    saver = tf.train.Saver()

    SummaryWriter = tf.summary.FileWriter
    writer = SummaryWriter(tensorboard_path, sess.graph)

    # start training
    if train_step == 0:
        ori_list = []
        gt_list = []
        for i, j in enumerate(img_list):
            ori_list.append(train_img_path + '/' + j)
            gt_list.append(train_gt_path + '/' + j)

        # dataset setting
        dataset = tf.data.Dataset.from_tensor_slices((ori_list, gt_list))
        dataset = dataset.map(map_func=image_resize, num_parallel_calls=3)
        dataset = dataset.shuffle(len(img_list)).batch(batch_size)
        dataset = dataset.repeat()

        dataset = dataset.prefetch(16)
        dataset_iterator = dataset.make_one_shot_iterator()
        img_train_, img_gt_ = dataset_iterator.get_next()

        loss_summary = tf.summary.merge([tf.summary.scalar("loss_", loss_)])

        sess.run(tf.initialize_all_variables())
        counter = 0
        counter_ = 0
        # epoch 100
        for e in range(epoch):
            # dataset : 4447, batch size : 8 or 16
            batch_count = int(len(img_list) / batch_size)

            # setting process bar
            pbar = tqdm(range(batch_count))

            # epoch counting
            counter += 1
            err_sum = 0

            # train with batch size
            for i in pbar:
                # resize train, gt
                img_train, img_gt = sess.run([img_train_, img_gt_])

                # training
                _, err = sess.run([optim_, loss_summary], feed_dict={image_input: img_train, image_gt: img_gt})
                writer.add_summary(err, counter_)
                counter_ += 1

                # load loss value
                err_ = loss_.eval(session=sess, feed_dict={image_input: img_train, image_gt: img_gt})
                err_sum += err_

                # show epoch, loss, process bar
                pbar.set_description("epoch : %d || loss : %f" % (e + 1, (err_sum / (i + 1))))

            # save each 10 epoch
            if counter % 10 == 0:
                saver.save(sess, ckpt_path + '/ckpt', global_step=counter)
        # save final step epoch
        saver.save(sess, ckpt_path + '/ckpt', global_step=counter)

    # test
    else:
        # load checkpoint file
        ckpt = tf.train.get_checkpoint_state(ckpt_path)
        if ckpt and ckpt.model_checkpoint_path:
            ckpt_path_ = str(ckpt.model_checkpoint_path)  # convert the unicode to string
            saver.restore(sess, os.path.join(os.getcwd(), ckpt_path_))
        counter = 0
        # load test image
        test_list_p = []
        for i, j in enumerate(test_list):
            test_list_p.append(test_img_path + '/' + j)

        dataset = tf.data.Dataset.from_tensor_slices(test_list_p)
        dataset = dataset.map(map_func=image_resize_t, num_parallel_calls=3)
        dataset = dataset.batch(1)

        dataset = dataset.prefetch(100)
        dataset_iterator = dataset.make_one_shot_iterator()
        img_train_, _, gt_ = dataset_iterator.get_next()

        for i, j in enumerate(test_list):
            counter += 1
            reshape_, image_gt = sess.run([img_train_, gt_])

            image_result = image_out.eval(session=sess, feed_dict={image_input: reshape_})
            _, t_height, t_width, _ = image_gt.shape
            result_ = np.reshape(image_result, (img_size, img_size))
            result_ = cv2.resize(result_, dsize=(t_width, t_height), interpolation=cv2.INTER_CUBIC)
            print("ECSSD : %d" % counter)

            cv2.imwrite(result_path + '/' + j, (result_ * 255))
        counter = 0

        # load test image
        test_list_p = []
        for i, j in enumerate(test_list_):
            test_list_p.append(test_img_path_ + '/' + j)

        dataset = tf.data.Dataset.from_tensor_slices(test_list_p)
        dataset = dataset.map(map_func=image_resize_t, num_parallel_calls=3)
        dataset = dataset.batch(1)

        dataset = dataset.prefetch(100)
        dataset_iterator = dataset.make_one_shot_iterator()
        img_train_, _, gt_ = dataset_iterator.get_next()
        for k, h in enumerate(test_list_):
            counter += 1
            reshape_, image_gt = sess.run([img_train_, gt_])
            _, t_height, t_width, _ = image_gt.shape
            image_result = image_out.eval(session=sess, feed_dict={image_input: reshape_})

            result_ = np.reshape(image_result, (img_size, img_size))
            result_ = cv2.resize(result_, dsize=(t_width, t_height), interpolation=cv2.INTER_CUBIC)
            print("MSRA10K : %d" % counter)

            cv2.imwrite(result_path_ + '/' + h, (result_ * 255))
    sess.close()


def get_parser():
    parser = argparse.ArgumentParser(
        prog='Image segmentation',
        usage='python hoi_relu.py',
        description='hoijun`s segmentation',
        add_help=True
    )

    parser.add_argument('-e', '--epoch', type=int, default=100, help='Number of epochs')
    parser.add_argument('-b', '--batchsize', type=int, default=16, help='Batch size')
    parser.add_argument('-l', '--learningrate', type=float, default=1e-4, help='Learning rate')
    parser.add_argument('-i', '--imgsize', type=int, default=224, help='Image size')
    parser.add_argument('-p', '--path', type=str, default='fcn', help='folder name')
    parser.add_argument('-t', '--train', type=int, default=0, help='train : 0 , test : 1')

    return parser


if __name__ == '__main__':
    parser = get_parser().parse_args()
    train(parser)