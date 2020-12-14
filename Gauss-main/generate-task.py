import math
filename = "task_density:0.0-10.0_0.005.sh"

length_list = []
for i in range(1,2001):
    density = 0.005*i
    volume = 2048/density
    length = math.pow(volume, 1/3)
    length = float(format(length, '.5f'))
    length_list.append(length)

for i in range(len(length_list)):
    length = length_list[i]
    with open(filename, "a") as f:
        f.write("./lmp_serial < input/L{}.input > dat/L{}.dat\n".format(length, length))
