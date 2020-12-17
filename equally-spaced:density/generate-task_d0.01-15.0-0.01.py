filename = "task_de0.0-15.0-0.01.sh"
import math

for i in range(1500):
    density = 0.01+i/1000
    volume = 2048/density
    length = math.pow(volume, 1/3)
    with open(filename, "a") as f:
        f.write("./lmp_serial < input/L{}.input > dat/L{}.dat\n".format(length, length))
