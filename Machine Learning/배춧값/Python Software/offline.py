#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()



import numpy as np
from pandas.io.parsers import read_csv

#model = tf.global_variables_initializer();       # 변수 초기화 오퍼레이션을 초기화

data = read_csv('price data.csv', sep=',')                                                           #01)  데이터 읽기
# 날짜,평균 풍속,최저 기온,최고 기온,강수량,평균 가격


xy = np.array(data, dtype=np.float32)     
#print(xy)                                                           #02) numpy에 쓰기
#print(xy.shape)                # (2922, 6)
#print(xy[0])


'''
[[ 2.0100100e+07 -4.9000001e+00 -1.1000000e+01  8.9999998e-01  0.0000000e+00  2.1230000e+03]
                      평균온도          최소온도          최대온도           강수량            가격
.     year,          avgTemp,       minTemp,       maxTemp,       rainFall,      avgPrice
.
.
[ 2.0171232e+07  2.0999999e+00 -2.0000000e+00  5.8000002e+00  4.0000001e-01  2.9010000e+03]]

2017-12-31,       2.5,           -2,              5.8,            0.4,             2901

'''

# 4개의 변인을 입력을 받습니다.
x_data = xy[:, 1:-1]               #[전체행,1열부터 마지막열 미만까지]  [0:3000,1:-1] 같다                        #03) 데이터 전처리
#print(x_data.shape)

#print(x_data)

'''
[[ -4.9  -11.   0.9   0. ]
 [ -3.1  -5.5   5.5   0.8]
 [ -2.9  -6.9   1.4   0. ]
 ...
 [  2.9  -2.1   8.    0. ]
 [  2.9  -1.6   7.1   0.6]
 [  2.1  -2.    5.8   0.4]]

-4.9,   -11 ,   0.9,   0  ,   2123
-3.1,   -5.5,   5.5,   0.8,   2123
-2.9,   -6.9,   1.4,   0  ,   2123
 ...
 2.9,   -2.1,   8  ,   0  ,   2901
 2.9,   -1.6,   7.1,   0.6,   2901
 2.1,   -2  ,   5.8,   0.4,   2901
'''


# 가격 값을 입력 받습니다.
y_data = xy[:, [-1]]                                                       #03) 데이터 전처리
#print(y_data)
'''
[[2123.]
 [2123.]
 [2123.]
 ...
 [2901.]
 [2901.]
 [2901.]]
'''


# 플레이스 홀더를 설정합니다.
X = tf.placeholder(tf.float32, shape=[None, 4])                             #04)tf.placeholder 설정
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([4, 1]), name="weight")                    #05)변수 설정
b = tf.Variable(tf.random_normal([1]), name="bias")

# 가설을 설정합니다.
hypothesis = tf.matmul(X, W) + b                                            #함수 설정
print(hypothesis)     #Tensor("add:0", shape=(?, 1), dtype=float32)         #06)가설 설정
#hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

# 비용 함수를 설정합니다.
#cost = tf.sigmoid(hypothesis-Y)
cost = tf.reduce_mean(tf.square(hypothesis-Y))                              #07)cost 설정

'''
# 98500  손실 비용:  0.0014705098
- 배추 가격:  [-0.02632101]
# 99000  손실 비용:  0.0014697206
- 배추 가격:  [-0.02631454]
# 99500  손실 비용:  0.0014689317
- 배추 가격:  [-0.02630809]
# 100000  손실 비용:  0.0014681434
- 배추 가격:  [-0.02630162]

# 94500  손실 비용:  [[3.6358833e-06]
 [5.9604645e-08]
 [6.2018633e-05]
 ...
 [3.0100346e-06]
 [1.5220827e-05]
 [4.9867616e-05]]
- 배추 가격:  [-12.527481]

'''
# 최적화 함수를 설정합니다.
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000005)       #08)최적화 함수 optimizer 설정
train = optimizer.minimize(cost)



model = tf.global_variables_initializer();                                  #09) 변수 초기화 오퍼레이션을 초기화

# 세션을 생성합니다.
sess = tf.Session()                                                         #10) 세션을 생성합니다.

# 글로벌 변수를 초기화합니다.
sess.run(model)
#sess.run(tf.global_variables_initializer())   # 초기화 오퍼레이션을 실행           #11) 글로벌 변수를 초기화합니다.

# 학습을 수행합니다.

for step in range(1):         #100001
    cost_, hypo_, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})         #12) 학습 실행
    print(cost_)
    if step % 500 == 0:
        print("#", step, " 손실 비용: ", cost_)
        print("- 배추 가격: ", hypo_[0])
        '''
        # 99000  손실 비용:  2229448.0
        #- 배추 가격:  [2584.2703]
        # 99500  손실 비용:  2229194.8
        #- 배추 가격:  [2584.3052]
        # 100000  손실 비용:  2228941.5(cost)
        '''
#print(hypo_.shape)   (2922, 1)
# 학습된 모델을 저장합니다.
saver = tf.train.Saver()                                                    #13) 학습 실행
save_path = saver.save(sess, "./saved.cpkt")
print('학습된 모델을 저장했습니다.')
