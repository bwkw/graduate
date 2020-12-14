import numpy as np
import matplotlib.pyplot as plt

#プロット全体
x_all = np.load("density_L6.0-7.0-0.002_L7.0-L25.0-0.036.npy")
y_all = np.load("pressure_L6.0-7.0-0.002_L7.0-L25.0-0.036.npy")

#一部のデータをとってくる
x_train = np.load("density_den0.0-10.0.npy")
y_train = np.load("pressure_den0.0-10.0.npy")


#mu(平均),std(標準偏差)のバイナリファイルを読み込む
mu = np.load("Gauss-mu/11-Gauss-mu.npy")
std = np.load("Gauss-std/11-Gauss-std.npy")

#描画
fig=plt.figure(figsize=(10, 5))
plt.xlabel("density")
plt.ylabel("pressure")
plt.ylim(-100000,2000000)
plt.title('11plot d-p prediction by Gaussian process', fontsize=20)

# 元の信号
plt.plot(x_all, y_all, 'x', color='green', label='correct signal')
# 部分的なサンプル点
plt.plot(x_train, y_train, 'o', color='red', label='sample dots')

# ガウス過程で求めた平均値を信号化
plt.plot(x_all, mu, color='blue', label='mean by Gaussian process')
# ガウス過程で求めた標準偏差を範囲化 *範囲に関してはコード末を参照
plt.fill_between(x_all, mu+100000*std, mu-100000*std, alpha=0.3, color='orange', label= 'standard deviation by Gaussian process')

plt.legend(loc='upper left', borderaxespad=0, fontsize=12)
plt.show()
fig.savefig("Gauss-plt/11plot d-p prediction by Gaussian process")