#モジュールをインポート
import numpy as np 
import matplotlib.pyplot as plt
import math

#データセット
x_all = np.load("density_L6.0-7.0-0.002_L7.0-L25.0-0.036.npy")
y_all = np.load("pressure_L6.0-7.0-0.002_L7.0-L25.0-0.036.npy")

n=len(x_all)

missing_value_rate = 0.03
sample_index = np.sort(np.random.choice(np.arange(n), int(n*missing_value_rate), replace=False))


#ガウス過程関数
def kernel(x, x_prime, p, q, r):
    if x == x_prime:
        delta = 1
    else:
        delta = 0

    return p*np.exp(-1 * (x - x_prime)**2 / q) + ( r * delta)

x_train = np.copy(x_all[sample_index])
y_train = np.copy(y_all[sample_index])

x_test = np.copy(x_all)

#main
# 平均
mu = []
# 分散
var = []

# 各パラメータ値
Theta_1 = 1.0
Theta_2 = 0.4
Theta_3 = 0.1

# 以下, ガウス過程回帰の計算の基本アルゴリズム
train_length = len(x_train)
# トレーニングデータ同士のカーネル行列の下地を準備
K = np.zeros((train_length, train_length))

for x in range(train_length):
    for x_prime in range(train_length):
        K[x, x_prime] = kernel(x_train[x], x_train[x_prime], Theta_1, Theta_2, Theta_3)

# 内積はドットで計算
yy = np.dot(np.linalg.inv(K), y_train)

test_length = len(x_test)

for xtest in range(test_length):
    # テストデータとトレーニングデータ間のカーネル行列の下地を準備
    k = np.zeros(train_length)
    for x in range(train_length):
        k[x] = kernel(x_train[x], x_test[xtest], Theta_1, Theta_2, Theta_3)

    s = kernel(x_test[xtest], x_test[xtest], Theta_1, Theta_2, Theta_3)
    #内積はドットで計算して, 平均値の配列に追加
    mu.append(np.dot(k, yy))
    #先に『k * K^-1』の部分を(内積なのでドットで)計算
    kK_ = np.dot(k,np.linalg.inv(K))
    # 後半部分との内積をドットで計算して, 分散の配列に追加
    var.append(abs(s - np.dot(kK_, k.T)))


std = abs(np.sqrt(var))

#リストをnumpy配列にしバイナリファイルで保存
mu = np.array(mu)
std = np.array(std)

np.save("30-Gauss-mu", mu)
np.save("30-Gauss-std", std)

