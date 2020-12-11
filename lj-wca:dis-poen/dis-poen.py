import re

def wca_loadfile(filename):
    with open(filename) as f:
        a = 0
        for line in f:
            if re.match("PotEng", line):
                a = 1
                continue
            elif re.match("Loop", line):
                a = 0
                break
            if a == 1:
                line = line.split()
                wca_energy.append(line[0])

def lj_loadfile(filename):
    with open(filename) as f:
        a = 0
        for line in f:
            if re.match("PotEng", line):
                a = 1
                continue
            elif re.match("Loop", line):
                a = 0
                break
            if a == 1:
                line = line.split()
                lj_energy.append(line[0])

def makefile(filename, distance):
    with open(filename, "a") as f:
        f.write("{} {} {}\n".format(distance, wca_energy[0], lj_energy[0]))


for i in range(111):
    wca_energy = []
    lj_energy = []
    r = format((0.6 + 0.005*i),'.3f')
    wca_loadfile("wca-dat/wca{}.dat".format(r)) 
    lj_loadfile("lj-dat/lj{}.dat".format(r))
    makefile("dis-poen.dat", r)

for i in range(1, 11):
    wca_energy = []
    lj_energy = []
    r = format((1.15 + 0.2*i),'.3f')
    wca_loadfile("wca-dat/wca{}.dat".format(r)) 
    lj_loadfile("lj-dat/lj{}.dat".format(r))
    makefile("dis-poen.dat", r)

