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
x_train.append(x_all[1380])
x_train.append(x_all[630])
x_train.append(x_all[1140])
x_train.append(x_all[390])
x_train.append(x_all[203])
x_train.append(x_all[953])
x_train.append(x_all[67])
x_train.append(x_all[817])
x_train.append(x_all[1440])
x_train.append(x_all[570])
x_train.append(x_all[1200])
x_train.append(x_all[449])
x_train.append(x_all[690])
x_train.append(x_all[1320])
x_train.append(x_all[1080])
x_train.append(x_all[330])
x_train.append(x_all[33])
x_train.sort()
y_train.append(y_all[271])
y_train.append(y_all[1021])
y_train.append(y_all[510])
y_train.append(y_all[1260])
y_train.append(y_all[135])
y_train.append(y_all[885])
y_train.append(y_all[1380])
y_train.append(y_all[630])
y_train.append(y_all[1140])
y_train.append(y_all[390])
y_train.append(y_all[203])
y_train.append(y_all[953])
y_train.append(y_all[67])
y_train.append(y_all[817])
y_train.append(y_all[1440])
y_train.append(y_all[570])
y_train.append(y_all[1200])
y_train.append(y_all[449])
y_train.append(y_all[690])
y_train.append(y_all[1320])
y_train.append(y_all[1080])
y_train.append(y_all[330])
y_train.append(y_all[33])
y_train.sort()

for i in range(len(x_train)):
    with open("gauss-fitting.dat", "a") as f:
        f.write("{} {}\n".format(x_train[i], y_train[i]))