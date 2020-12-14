import re
import numpy as np
import math

def loadfile(filename):
    with open(filename) as f:
        a = 0
        for line in f:
            if re.match("Time", line):
                a = 1
                continue
            elif re.match("Loop", line):
                a = 0
                break
            if a == 1:
                line = line.split()
                tp_list.append(line)
        for i in range(len(tp_list)):
            a = tp_list[i][2]
            pressure.append(a)

density_list = []
pressure_list = []

density_list.append(0)
pressure_list.append(0)

length_list = []
for i in range(1,11):
    density = i
    volume = 2048/density
    length = math.pow(volume, 1/3)
    length = float(format(length, '.3f'))
    length_list.append(length)

for i in range(len(length_list)):
    tp_list = []
    pressure = []
    length = length_list[i]
    V = length**3
    N = 2048
    density = round(N/V, 0)
    loadfile("dat/L{}.dat".format(length))
    int_pressure = [float(a) for a in pressure]
    ave_pressure = sum(int_pressure[78:1992])/len(int_pressure[78:1992])
    pressure_list.append(ave_pressure)
    density_list.append(density)
    
    
#リストをnumpy配列として保存
ar_density = np.array(density_list)
ar_pressure = np.array(pressure_list)

#numpy配列をバイナリファイルとして保存
np.save("density_den0.0-10.0", ar_density)
np.save("pressure_den0.0-10.0", ar_pressure)


