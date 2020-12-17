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


for i in range(501):
    length = 6 + i/500
    length = float(format(length, '.3f'))
    volume = length**3
    density = 2048/volume
    distance = math.sqrt(2)*(length/16)
    dis_pow = abs((48*distance**(-12)-24*distance**(-6))*12*2048/2048/2)
    pressure = (1/(volume))*(2048+2048*dis_pow/3) 
    with open("compare:den-pre.dat", "a") as f:
        f.write("{} {} {}\n".format(density, pressure, y_all[i]))

for i in range(501):
    length = 6 + i/500
    length = float(format(length, '.3f'))
    volume = length**3
    density = 2048/volume
    distance = math.sqrt(2)*(length/16)
    pressure = (1/(volume))*(2048) 
    with open("compare:den-pre.dat", "a") as f:
        f.write("{} {} {}\n".format(density, pressure, y_all[i]))
