#inputファイルを作成
import math

def make_file(filename, length):
    with open(filename, "w") as f:
        f.write("units lj\n")
        f.write("atom_style atomic\n\n")
        f.write("read_data atoms/L{}.atoms\n\n".format(length))
        f.write("mass 1 1.0\n\n")
        f.write("reset_timestep  0\n")
        f.write("timestep        0.0001\n\n")
        f.write("pair_style lj/cut 1.12246\n")
        f.write("pair_modify shift yes\n")
        f.write("pair_coeff 1 1 1.0 1.0 1.0\n\n")
        f.write("fix 1 all nvt temp 1.0 1.0 0.01\n\n")
        f.write("thermo 10\n")
        f.write("thermo_style custom time temp press\n\n")
        f.write("run 20000")


for i in range(1500):
    density = 0.01+i/1000
    volume = 2048/density
    length = math.pow(volume, 1/3)
    make_file("input/L{}.input".format(length), length)
