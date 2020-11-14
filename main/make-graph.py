#密度と圧力の関係をグラフに

import matplotlib.pyplot as plt

dp_list = []
density = []
pressure = []

for i in range(11):
    r = 10 + i/10
    filename = "L{}-av_pre.dat".format(r)
    with open(filename)as f:
        for line in f:
            line = line.split(" ")
            dp_list.append(line)

for i in range(len(dp_list)):
    density.append(dp_list[i][0])
    pressure.append(dp_list[i][1])

density = [float(i) for i in density]
pressure = [float(i) for i in pressure]

fig = plt.figure()
plt.title("density-pressure in wca potentials")
plt.xlabel("density")
plt.ylabel("pressure")
plt.plot(density, pressure, marker="o", color = "blue")
fig.savefig("dp.png")


    


