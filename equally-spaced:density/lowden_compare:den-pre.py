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

for i in range(101):
    density = 0.01 * i
    if density == 0:
        density = 0
        pressure = 0
    else:
        volume = 2048/density
        length = math.pow(volume, 1/3)
        distance = math.sqrt(2)*(length/16)
        pressure = (1/(volume))*(2048) 
    with open("lowden_compare:den-pre.dat", "a") as f:
        f.write("{} {} {}\n".format(density, pressure, y_all[i]))