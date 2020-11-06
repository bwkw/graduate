import re

a = 0

list1 = []
with open("nonideal.dat") as f:
    for line in f:
        if re.match("Time", line):
            a = 1
            continue
        elif re.match("Loop", line):
            a = 0
            break
        if a == 1:
            line = line.split()
            list1.append(line)

time = []
temperature = []

for i in range(len(list1)):
    a = list1[i][0]
    b = list1[i][1]
    time.append(a)
    temperature.append(b)

with open("time-temperature.dat", "w") as f:
    for i in range(len(list1)):
        f.write("{} {}\n".format(time[i], temperature[i]))
