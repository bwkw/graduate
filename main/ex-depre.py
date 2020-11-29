#Lのdatファイルを読み込み、av_preファイルを作成

import re

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
    
for i in range(51):
    r = 10 + i/5
    tp_list = []
    pressure = []
    density = []
    V = r**3
    N = 2048
    d = N/V
    loadfile("L{}.dat".format(r))
    density.append(d)

print(pressure)
print(density)
#リストをnumpy配列として保存
