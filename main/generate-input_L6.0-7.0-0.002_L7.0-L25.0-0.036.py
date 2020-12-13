#inputファイルを作成

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

for i in range(501):
    r = 6 + i/500
    r = float(format(r, '.3f'))
    make_file("input/L{}.input".format(r), r)

for i in range(1,501):
    r = 7 + (18/500)*i
    r = float(format(r, '.3f'))
    make_file("input/L{}.input".format(r), r)
