import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#入れ物を用意する
x=tf.placeholder(tf.float32,[None,5])
w=tf.Variable(tf.zeros([5,1]))
y=tf.matmul(x,w)
t=tf.placeholder(tf.float32,[None,1])

#y=xwとtを比較し、それを最小にしていく
#損失関数
#二乗の和を計算
loss=tf.reduce_sum(tf.square(y-t))
#損失関数を最小にするadamアルゴリズム
train_step=tf.train.AdamOptimizer().minimize(loss)

#変数を使うために、tf.initialize_all_variables()で変数を初期化
sess=tf.Session()
sess.run(tf.initialize_all_variables())

#訓練データとしてsin(2.0*np.pi*i/11)上の点を食わせる(tは答え)
train_t=np.array([np.sin(2.0*np.pi*i/11) for i in range(12)])
train_t=train_t.reshape([12,1])

#訓練データとして格子状の点を食わせる(xはランダムに配置し重みwによってyを出力、tと比較)
train_x=np.zeros([12,5])
for row,m in enumerate(range(1,13)):
    for col,n in enumerate(range(0,5)):
        train_x[row][col]=m**n

#学習段階
i=0
for _ in range(100000):
    i+=1
    sess.run(train_step,feed_dict={x:train_x,t:train_t})
    if i % 1000==0:
        loss_val=sess.run(loss,feed_dict={x:train_x,t:train_t})
        print ('Step:%d, Loss:%f'%(i,loss_val))

#学習後の重みを出力
w_val=sess.run(w)
print(w_val)

#完成した重みをもとに予想yの出力
def predict(x):
    result=0.0
    for n in range(0,5):
        result+=w_val[n][0]* x**n
    return result

fig=plt.figure()
subplot=fig.add_subplot(1,1,1)
subplot.set_xlim(1,12)
subplot.scatter(range(1,13),train_t)
linex=np.linspace(1,12,100)
liney=predict(linex)
subplot.plot(linex,liney)
plt.show()