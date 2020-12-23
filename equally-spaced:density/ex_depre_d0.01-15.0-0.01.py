#Lのdatファイルを読み込み、densityとpressureのリスト作成
#numpy配列として保存し、machine-learnig.pyにかける

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

for i in range(1500):
    tp_list = []
    pressure = []
    density = float(format(0.01+i/100, "2f"))
    volume = 2048/density
    length = math.pow(volume, 1/3)
    loadfile("dat/d{}.dat".format(density))
    int_pressure = [float(a) for a in pressure]
    ave_pressure = sum(int_pressure[78:1992])/len(int_pressure[78:1992])
    pressure_list.append(ave_pressure)
    density_list.append(density)
   
#リストをnumpy配列として保存
ar_density = np.array(density_list)
ar_pressure = np.array(pressure_list)

#numpy配列をバイナリファイルとして保存
np.save("density_d0.01-15.0-0.01", ar_density)
np.save("pressure_d0.01-15.0-0.01", ar_pressure)

