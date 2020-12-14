import math
filename = "task_density:1.0-10.0.sh"

length_list = []
for i in range(1,11):
    density = i
    volume = 2048/density
    length = math.pow(volume, 1/3)
    length = float(format(length, '.3f'))
    length_list.append(length)

for i in range(len(length_list)):
    length = length_list[i]
    with open(filename, "a") as f:
        f.write("lmp_serial < input/L{}.input > dat/L{}.dat\n".format(length, length))