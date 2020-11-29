#距離10~12.8まで
import math
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
            a = tp_list[i][0]
            b = tp_list[i][2]
            time.append(a)
            pressure.append(b)

def makefile(filename):
    with open(filename, "a") as f:
        int_pressure = [float(n) for n in pressure]
        co_distance = 2*R-r
        ave_pressure = sum(int_pressure[78:1992])/len(int_pressure[78:1992])
        f.write("{} {}\n".format(co_distance, ave_pressure))

for i in range(15):
    l = format((10.0 + 0.2*i),'.1f')
    r = math.sqrt((float(l)/16)**2+(float(l)/16)**2)
    R = 0.9
    tp_list = []
    time = []
    pressure = []
    loadfile("L{}.dat".format(l))
    makefile("dis-pre.dat")

