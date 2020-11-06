class Atom:
    def __init__(self, x, y, z, xvel):
        self.x = x
        self.y = y
        self.z = z
        self.type = 1
        self.vx = xvel
        self.vy = 0
        self.vz = 0

def add_ball(atoms, pos, xvel):
    r = 10
    n = 8
    s = r/n
    h = s/2
    for ix in range(0,n):
        for iy in range(0,n):
            for iz in range(0,n):
                x = ix*s + pos
                y = iy*s + pos
                z = iz*s + pos
                atoms.append(Atom(x, y, z, xvel))
                atoms.append(Atom(x+h, y+h, z, xvel))
                atoms.append(Atom(x+h, y, z+h, xvel))
                atoms.append(Atom(x, y+h, z+h, xvel))

def make_file(filename, atoms):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write("{} atoms\n".format(len(atoms)))
        f.write("1 atom types\n\n")
        f.write("0.0 10.0 xlo xhi\n")
        f.write("0.0 10.0 ylo yhi\n")
        f.write("0.0 10.0 zlo zhi\n")
        f.write("\n")
        f.write("Atoms\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {} {}\n".format(i+1, a.type, a.x, a.y, a.z))
        f.write("\n")
        f.write("Velocities\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {}\n".format(i+1, a.vx, a.vy, a.vz))
    print("Generated {}".format(filename))
    print(len(atoms))

atoms = []

add_ball(atoms, 0.0, 1.0)

make_file("nonideal.atoms", atoms)  