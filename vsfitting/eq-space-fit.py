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
for i in range(26):
    density = 60*i
    xtrain = x_all[density]
    ytrain = y_all[density]
    x_train.append(xtrain)
    y_train.append(ytrain)

for i in range(len(x_train)):
    with open("eq-space-fitting.dat", "a") as f:
        f.write("{} {}\n".format(x_train[i], y_train[i]))