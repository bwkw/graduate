#Lのdatファイルを読み込み、densityとpressureのリスト作成
#numpy配列として保存し、machine-learnig.pyにかける

import re
import numpy as np

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

for i in range(201):
    tp_list = []
    pressure = []
    r = 5 + i/10
    V = r**3
    N = 2048
    density = N/V
    loadfile("L{}.dat".format(r))
    int_pressure = [float(a) for a in pressure]
    ave_pressure = sum(int_pressure[78:1992])/len(int_pressure[78:1992])
    pressure_list.append(ave_pressure)
    density_list.append(density)

#リストをnumpy配列として保存
ar_density = np.array(density_list)
ar_pressure = np.array(pressure_list)

#numpy配列をバイナリファイルとして保存
np.save("density", ar_density)
np.save("pressure", ar_pressure)


