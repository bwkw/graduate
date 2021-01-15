import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

#データセット
x_all = np.load("density_d0.01-15.0-0.01.npy")
y_all = np.load("pressure_d0.01-15.0-0.01.npy")
x_all = x_all.tolist()
y_all = y_all.tolist()
x_all.insert(0,0)
y_all.insert(0,0)

x_train = []
y_train = []

for i in range(3):
    density = 750*i
    xtrain = x_all[density]
    ytrain = y_all[density]
    x_train.append(xtrain)
    y_train.append(ytrain)

x_train.append(x_all[271])
x_train.append(x_all[1021])
x_train.append(x_all[510])
x_train.append(x_all[1260])
x_train.append(x_all[135])
x_train.append(x_all[885])
#x_train.append(x_all[1380])
#x_train.append(x_all[630])
#x_train.append(x_all[1140])
#x_train.append(x_all[390])
#x_train.append(x_all[203])
#x_train.append(x_all[953])
#x_train.append(x_all[67])
#x_train.append(x_all[817])
#x_train.append(x_all[1440])
#x_train.append(x_all[570])
#x_train.append(x_all[1200])
#x_train.append(x_all[449])
#x_train.append(x_all[690])
#x_train.append(x_all[1320])
#x_train.append(x_all[1080])
#x_train.append(x_all[330])
#x_train.append(x_all[33])
x_train.sort()

y_train.append(y_all[271])
y_train.append(y_all[1021])
y_train.append(y_all[510])
y_train.append(y_all[1260])
y_train.append(y_all[135])
y_train.append(y_all[885])
#y_train.append(y_all[1380])
#y_train.append(y_all[630])
#y_train.append(y_all[1140])
#y_train.append(y_all[390])
#y_train.append(y_all[203])
#y_train.append(y_all[953])
#y_train.append(y_all[67])
#y_train.append(y_all[817])
#y_train.append(y_all[1440])
#y_train.append(y_all[570])
#y_train.append(y_all[1200])
#y_train.append(y_all[449])
#y_train.append(y_all[690])
#y_train.append(y_all[1320])
#y_train.append(y_all[1080])
#y_train.append(y_all[330])
#y_train.append(y_all[33])
y_train.sort()

#mu(平均),std(標準偏差)のバイナリファイルを読み込む
mu = np.load("Gauss-mu/9-Gauss-mu.npy")
std = np.load("Gauss-std/9-Gauss-std.npy")

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
plt.fill_between(x_all, mu+1000000*std, mu-1000000*std, alpha=0.3, color='orange', label= '標準偏差')

#凡例
plt.legend(loc='upper left', borderaxespad=0, fontsize=20)
fig.savefig("Gauss-plt/26plot-Gauss")