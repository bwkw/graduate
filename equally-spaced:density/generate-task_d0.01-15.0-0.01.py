filename = "task_d0.0-15.0-0.01.sh"
import math

for i in range(1500):
    density = float(format(0.01+i/100, "2f"))
    volume = 2048/density
    length = math.pow(volume, 1/3)
    with open(filename, "a") as f:
        f.write("./lmp_serial < input/d{}.input > dat/d{}.dat\n".format(density, density))
