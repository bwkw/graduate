import numpy as np
import matplotlib.pyplot as plt

#プロット全体
x_all = np.load("density_L6.0-7.0-0.002_L7.0-L25.0-0.036.npy")
y_all = np.load("pressure_L6.0-7.0-0.002_L7.0-L25.0-0.036.npy")

#一部のデータをとってくる
n=len(x_all)
missing_value_rate = 0.03
np.random.seed(0)
sample_index = np.sort(np.random.choice(np.arange(n), int(n*missing_value_rate), replace=False))

#sample_index=np.sort(np.append(sample_index, 513))
#sample_index=np.sort(np.append(sample_index, 581))
#sample_index=np.sort(np.append(sample_index, 522))
#sample_index=np.sort(np.append(sample_index, 506))
#sample_index=np.sort(np.append(sample_index, 602))

x_train = np.copy(x_all[sample_index])
y_train = np.copy(y_all[sample_index])

#mu(平均),std(標準偏差)のバイナリファイルを読み込む
mu = np.load("Gauss-mu/30-Gauss-mu.npy")
std = np.load("Gauss-std/30-Gauss-std.npy")

#描画
fig=plt.figure(figsize=(10, 5))
plt.xlabel("density")
plt.ylabel("pressure")
plt.ylim(-100000,2000000)
plt.title('35plot d-p prediction by Gaussian process', fontsize=20)

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
fig.savefig("Gauss-plt/30plot d-p prediction by Gaussian process")