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


for i in range(41):
    density = 0.80 + 0.01*i
    volume = 2048/density
    with open("middleden_den-pre.dat", "a") as f:
        f.write("{} {}\n".format(x_all[80+i], y_all[80+i]))
