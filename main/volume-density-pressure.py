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
    

def makefile(filename):
    with open(filename, "a") as f:
        int_pressure = [float(n) for n in pressure]
        volume = V
        density = N/V
        ave_pressure = sum(int_pressure[78:1992])/len(int_pressure[78:1992])
        f.write("{} {} {}\n".format(volume, density, ave_pressure))
        
for i in range(11):
    r = 10 + i/10
    tp_list = []
    time = []
    pressure = []
    int_pressure = []
    V = r**3
    N = 2048
    loadfile("L{}.dat".format(r))
    makefile("vdp.dat")
    