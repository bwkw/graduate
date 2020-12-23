import numpy as np
import matplotlib.pyplot as plt

#データセット
x_all = np.load("density_d0.01-15.0-0.01.npy")
y_all = np.load("pressure_d0.01-15.0-0.01.npy")
x_all = x_all.tolist()
y_all = y_all.tolist()
x_all.insert(0,0)
y_all.insert(0,0)

x_train = []
y_train = []

for i in range(2):
    density = 1500*i
    xtrain = x_all[density]
    ytrain = y_all[density]
    x_train.append(xtrain)
    y_train.append(ytrain)

#mu(平均),std(標準偏差)のバイナリファイルを読み込む
mu = np.load("Gauss-mu/2-Gauss-mu.npy")
std = np.load("Gauss-std/2-Gauss-std.npy")

#描画
fig=plt.figure(figsize=(10, 5))
plt.xlabel("density")
plt.ylabel("pressure")
plt.ylim(-100000,2000000)
plt.title('2plot d-p prediction by Gaussian process', fontsize=20)

# 元の信号
plt.plot(x_all, y_all, 'x', color='green', label='correct signal')
# 部分的なサンプル点
plt.plot(x_train, y_train, 'o', color='red', label='sample dots')

# ガウス過程で求めた平均値を信号化
plt.plot(x_all, mu, color='blue', label='mean by Gaussian process')
# ガウス過程で求めた標準偏差を範囲化 *範囲に関してはコード末を参照
plt.fill_between(x_all, mu+std, mu-std, alpha=0.3, color='orange', label= 'standard deviation by Gaussian process')

plt.legend(loc='upper left', borderaxespad=0, fontsize=12)
plt.show()
fig.savefig("Gauss-plt/2plot d-p prediction by Gaussian process")