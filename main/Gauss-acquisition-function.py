import numpy as np

std = np.load("Gauss-std/30-Gauss-std.npy")

std_max = np.amax(std)
std_max_in = np.argmax(std)

#標準偏差が最大となるLを取得する
if std_max_in <= 500:
    std_max_L = 6.0+0.002*std_max_in
else:
    std_max_L = 7.0 + (18/500)*(std_max_in-500)

std_max_density = 2048/((std_max_L)**3)

print("{}:{}".format("index",std_max_in))
print("{}:{}".format("L",std_max_L))
print("{}:{}".format("density",std_max_density))
