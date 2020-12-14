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
volume_list = []

for i in range(501):
    tp_list = []
    pressure = []
    r = 6 + i/500
    r = float(format(r, '.3f'))
    V = r**3
    N = 2048
    density = N/V
    loadfile("dat/L{}.dat".format(r))
    int_pressure = [float(a) for a in pressure]
    ave_pressure = sum(int_pressure[78:1992])/len(int_pressure[78:1992])
    pressure_list.append(ave_pressure)
    density_list.append(density)
    volume_list.append(V)

for i in range(1,501):
    tp_list = []
    pressure = []
    r = 7 + (18/500)*i
    r = float(format(r, '.3f'))
    V = r**3
    N = 2048
    density = N/V
    loadfile("dat/L{}.dat".format(r))
    int_pressure = [float(a) for a in pressure]
    ave_pressure = sum(int_pressure[78:1992])/len(int_pressure[78:1992])
    pressure_list.append(ave_pressure)
    density_list.append(density)
    volume_list.append(V)

#max_pressure = max(pressure_list)
#max_pressure 1835345.523354229

#圧力を[0.50]に正規化
#pressure_list = [(50*i/max_pressure) for i in pressure_list]
#リストをnumpy配列として保存
ar_density = np.array(density_list)
ar_pressure = np.array(pressure_list)
ar_volume = np.array(volume_list)

#numpy配列をバイナリファイルとして保存
np.save("density_L6.0-7.0-0.002_L7.0-L25.0-0.036", ar_density)
np.save("pressure_L6.0-7.0-0.002_L7.0-L25.0-0.036", ar_pressure)
np.save("volume_L6.0-7.0-0.002_L7.0-L25.0-0.036", ar_volume)

