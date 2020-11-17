filename = "task.sh"

for i in range(51):
    r = 10 + i/5
    with open(filename, "a") as f:
        f.write("lmp_serial < L{}.input > L{}.dat\n".format(r, r))
