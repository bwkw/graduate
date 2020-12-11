filename = "task.sh"

for i in range(131):
    r = format((0.5 + 0.005*i),'.3f')
    with open(filename, "a") as f:
        f.write("lmp_serial < wca{}.input > wca{}.dat\n".format(r, r))

for i in range(1,11):
    r = format((1.15 + 0.2*i),'.3f')
    with open(filename, "a") as f:
        f.write("lmp_serial < wca{}.input > wca{}.dat\n".format(r, r))

