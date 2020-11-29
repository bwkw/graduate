filename = "task.sh"

for i in range(201):
    r = 5 + i/10
    with open(filename, "a") as f:
        f.write("lmp_serial < L{}.input > L{}.dat\n".format(r, r))
