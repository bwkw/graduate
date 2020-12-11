filename = "task-lj.sh"

for i in range(111):
    r = format((0.6 + 0.005*i),'.3f')
    with open(filename, "a") as f:
        f.write("lmp_serial < lj-input/lj{}.input > lj-dat/lj{}.dat\n".format(r, r))

for i in range(1, 11):
    r = format((1.15 + 0.2*i),'.3f')
    with open(filename, "a") as f:
        f.write("lmp_serial < lj-input/lj{}.input > lj-dat/lj{}.dat\n".format(r, r))