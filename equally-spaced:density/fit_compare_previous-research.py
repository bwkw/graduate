import numpy as np
import math

fit_list = []
for s in range(0,501):
    x = s/100
    a = 1
    b = 2/3 * math.pi
    c = (5/8) * b**2
    d = 0.2869495 * b**3
    e = 0.110252 * b**4
    f = 0.038808 * b**5
    g = 0.013071 * b**6
    h = 0.00432 * b**7
    y = a*x + b*x**2 + c*x**3 +d*x**4 + e*x**5 + f*x**6 + g*x**7 + h*x**8 

    fita = 1
    fitb = 8.40579
    fitc = -29.0885
    fitd = 0.0158545
    fite = 24.2634
    fity = (fita*x + fitb*x**2 + fitc*x**3 + fitd*x**4 + fite*x**5) * 1.6068411114802712
    if fity == 0:
        fit = 1
    else:
        fit = y/fity
    fit_list.append(fit)
    with open("fit_compare_previous-research.dat", "a") as f:
        f.write("{} {} {}\n".format(x,y,fity))

fit_list=fit_list[200:341]
fit_average = sum(fit_list)/len(fit_list)
print(fit_average)