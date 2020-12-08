#atomsファイルを作成
import math

class Atom:
    def __init__(self, x, y, z, xvel):
        self.x = x
        self.y = y
        self.z = z
        self.type = 1
        self.vx = xvel
        self.vy = 0
        self.vz = 0

def add_ball(atoms, xvel, length):
    r = length
    n = 8
    s = r/n
    h = s/2
    for ix in range(0,n):
        for iy in range(0,n):
            for iz in range(0,n):
                x = ix*s
                y = iy*s
                z = iz*s
                atoms.append(Atom(x, y, z, xvel))
                atoms.append(Atom(x+h, y+h, z, xvel))
                atoms.append(Atom(x+h, y, z+h, xvel))
                atoms.append(Atom(x, y+h, z+h, xvel))

def make_file(filename, atoms, length):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write("{} atoms\n".format(len(atoms)))
        f.write("1 atom types\n\n")
        f.write("0.0 {} xlo xhi\n".format(length))
        f.write("0.0 {} ylo yhi\n".format(length))
        f.write("0.0 {} zlo zhi\n".format(length))
        f.write("\n")
        f.write("Atoms\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {} {}\n".format(i+1, a.type, a.x, a.y, a.z))
        f.write("\n")
        f.write("Velocities\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {}\n".format(i+1, a.vx, a.vy, a.vz))

atoms = []
density = 3.56502778
volume = 2048/density
length = math.pow(volume, 1/3)
length = float(format(length, '.3f'))
add_ball(atoms, 1.0, length)
make_file("L{}.atoms".format(length), atoms, length)
