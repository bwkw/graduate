filename = "task_L6.0-7.0-0.002_L7.0-L25.0-0.036.sh"

for i in range(501):
    r = 6 + i/500
    r = float(format(r, '.3f'))
    with open(filename, "a") as f:
        f.write("./lmp_serial < input/L{}.input > dat/L{}.dat\n".format(r, r))

for i in range(1,501):
    r = 7 + (18/500)*i
    r = float(format(r, '.3f'))
    with open(filename, "a") as f:
        f.write("./lmp_serial < input/L{}.input > dat/L{}.dat\n".format(r, r))
