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

fitting5_list = []
for i in range(1501):
    x = i/100
    a = 1
    b = 8.40579
    c = -29.0885
    d = 0.0158545
    e = 24.2634
    y = a*x + b*x**2 +c*x**3 + d*x**4 + e*x**5
    fitting5_list.append(y)


for i in range(len(x_all)):
    with open("5den-pre.dat", "a") as f:
        f.write("{} {} {}\n".format(x_all[i], y_all[i], fitting5_list[i]))

gap_list = []
for i in range(1,len(x_all)):
    measurement = y_all[i]
    fitting = fitting5_list[i]
    gap = abs(((measurement-fitting)/measurement))*100
    gap_list.append(gap)

average_gap = sum(gap_list)/len(gap_list)

print(average_gap)
