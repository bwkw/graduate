#wcaのinputファイルを作成

def make_file(filename, distance):
    with open(filename, "w") as f:
        f.write("units lj\n")
        f.write("atom_style atomic\n\n")
        f.write("read_data lj-atoms/lj{}.atoms\n\n".format(distance))
        f.write("mass 1 1.0\n\n")
        f.write("pair_style lj/cut 2.5\n")
        f.write("pair_modify shift yes\n")
        f.write("pair_coeff 1 1 1.0 1.0 2.5\n\n")
        f.write("thermo 1\n")
        f.write("thermo_style custom pe\n\n")
        f.write("run 0")

for i in range(111):
    r = format((0.6 + 0.005*i),'.3f')
    make_file("lj-input/lj{}.input".format(r), r)  

for i in range(1, 11):
    r = format((1.15 + 0.2*i),'.3f')
    make_file("lj-input/lj{}.input".format(r), r)  
