import numpy as np

std = np.load("Gauss-std/26-Gauss-std.npy")

std_max = np.amax(std)
std_max_in = np.argmax(std)

#標準偏差が最大となるLを取得する
std_max_density = 0.01*std_max_in

print("{}:{}".format("index",std_max_in))
print("{}:{}".format("density",std_max_density))
