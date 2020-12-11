#atomsファイルを作成
#隣接距離0.5~2.5

def make_file(filename, distance):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write("2 atoms\n")
        f.write("1 atom types\n\n")
        f.write("0.0 10.0 xlo xhi\n")
        f.write("0.0 10.0 ylo yhi\n")
        f.write("0.0 10.0 zlo zhi\n")
        f.write("\n")
        f.write("Atoms\n\n")
        f.write("{} {} {} {} {}\n".format(1, 1, distance, 0.0, 0.0))
        f.write("{} {} {} {} {}\n".format(2, 1, 0.0, 0.0, 0.0))
        f.write("\n")
        f.write("Velocities\n\n")
        for i in range(2):
            f.write("{} 1.0 0.0 0.0\n".format(i+1))

for i in range(131):
    r = format((0.5 + 0.005*i),'.3f')
    make_file("wca-atoms/wca{}.atoms".format(r), r)  

for i in range(1,6):
    r = format((1.15 + 0.2*i),'.3f')
    make_file("wca-atoms/wca{}.atoms".format(r), r)  
