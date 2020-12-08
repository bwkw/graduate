import re
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
    

def makefile(filename):
    with open(filename, "a") as f:
        int_pressure = [float(n) for n in pressure]
        ave_pressure = sum(int_pressure[78:1992])/len(int_pressure[78:1992])
        f.write("{} {} {}\n".format(volume, density, ave_pressure))
        

tp_list = []
time = []
pressure = []
int_pressure = []
density = 0.00334022
volume = 2048/density
length = math.pow(volume, 1/3)
length = float(format(length, '.3f'))
loadfile("L{}.dat".format(length))
makefile("vdp.dat")