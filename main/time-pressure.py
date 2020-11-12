#Lのdatファイルを読み込み、tpファイルを作成

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
    with open(filename, "w") as f:
        for i in range(len(tp_list)):
            f.write("{} {}\n".format(time[i], pressure[i]))

for i in range(11):
    r = 10 + i/10
    tp_list = []
    time = []
    pressure = []
    loadfile("L{}.dat".format(r))
    makefile("L{}-tp.dat".format(r))