#モジュールをインポート
import numpy as np 
import matplotlib.pyplot as plt
import math
import japanize_matplotlib

#測定値（全点）
x_all = np.load("density_d0.01-15.0-0.01.npy")
y_all = np.load("pressure_d0.01-15.0-0.01.npy")
x_all = x_all.tolist()
y_all = y_all.tolist()
x_all.insert(0,0)
y_all.insert(0,0)

#試行点
x_train = []
y_train = []
for i in range(3):
    density = 750*i
    xtrain = x_all[density]
    ytrain = y_all[density]
    x_train.append(xtrain)
    y_train.append(ytrain)

gauss = []
gauss.append(271)
gauss.append(1021)
gauss.append(510)
gauss.append(1260)
gauss.append(135)
gauss.append(885)
gauss.append(1380)
gauss.append(630)
gauss.append(1140)
gauss.append(390)
gauss.append(203)
gauss.append(953)
gauss.append(67)
gauss.append(817)
gauss.append(1440)
gauss.append(570)
gauss.append(1200)
gauss.append(449)
gauss.append(690)
gauss.append(1320)
gauss.append(1080)
gauss.append(330)
gauss.append(33)
gauss.sort()

for i in range(len(gauss)):
    x_train.append(x_all[gauss[i]])
    y_train.append(y_all[gauss[i]])

#ガウス過程関数
def kernel(x, x_prime, p, q, r):
    if x == x_prime:
        delta = 1
    else:
        delta = 0
    return p*np.exp(-1 * (x - x_prime)**2 / q) + (r * delta)

x_test = np.copy(x_all)

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
        K[x, x_prime] = kernel
        (x_train[x], x_train[x_prime], Theta_1, Theta_2, Theta_3)


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

#描画
fig=plt.figure(figsize=(10, 5))
plt.xlabel('$\it{ρ}$', fontsize=18)
plt.ylabel('$\it{P}$', fontsize=18)

# 測定値
plt.plot(x_all, y_all, 'x', color='green', label='測定値')
# 試行点
plt.plot(x_train, y_train, 'o', color='red', label='試行点')

# ガウス過程で求めた平均値を可視化
plt.plot(x_all, mu, color='blue', label='平均')
# ガウス過程で求めた標準偏差を可視化
plt.fill_between(x_all, mu+1000000*std, mu-1000000*std, 
alpha=0.3, color='orange', label= '標準偏差')

#凡例
plt.legend(loc='upper left', borderaxespad=0, fontsize=20)

#平均・標準偏差・画像を保存
mu = np.array(mu)
std = np.array(std)
np.save("Gauss-mu/26-Gauss-mu", mu)
np.save("Gauss-std/26-Gauss-std", std)
fig.savefig("Gauss-plt/26plot-Gauss")

#標準偏差が最大となるdensity(密度)を取得する
std_max_in = np.argmax(std)
std_max_density = 0.01*std_max_in

print("{}:{}".format("density",std_max_density))