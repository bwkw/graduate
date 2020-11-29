import math

for i in range(26):
    length = 10 + 0.1*i
    volume = length**3
    density = 2048/volume
    distance = math.sqrt(2)*(length/16)
    dis_pow = abs((48*distance**(-12)-24*distance**(-6))/2048/2)
    pressure = 1/(volume)*(2048+2048*12*dis_pow/3) 
    with open("ideal-den-pre.dat", "a") as f:
        f.write("{} {}\n".format(density, pressure))