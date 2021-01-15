#モジュールをインポート
import numpy as np 
import matplotlib.pyplot as plt
import math

#データセット
x_all = np.load("density_d0.01-15.0-0.01.npy")
y_all = np.load("pressure_d0.01-15.0-0.01.npy")

x_all = x_all.tolist()
y_all = y_all.tolist()
x_all.insert(0,0)
y_all.insert(0,0)

x_all = x_all[80:121]
y_all = y_all[80:121]
y_all = [math.log(i) for i in y_all]

for i in range(41):
    with open("middleden-logarithm_den-pre.dat", "a") as f:
        f.write("{} {}\n".format(x_all[i], y_all[i]))