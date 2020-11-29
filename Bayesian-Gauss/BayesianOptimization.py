import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import GPy
import GPyOpt

data = 1
initial_density = np.array([1.86, 1.4577259475218662, 1.0238075241854532,0.256, 0.00])
initial_pressure = np.array([376.1, 85.09328955538143, 2.2665168930511985, 0.2564432474033441, 0.00])

initial_density = initial_density.reshape((-1,1)) #n×1の行列に変換
initial_pressure = initial_pressure.reshape((-1,1))

def f(density):
    global data
    print("data_num : " , data)
    print("next density is ", density)
    pressure = float(input("pressure : "))
    data += 1
    return pressure


bounds = [{'name': 'a', 'type': 'continuous', 'domain': (0.0, 2.1)}]
myBopt = GPyOpt.methods.BayesianOptimization(f=f,
                                             domain=bounds,
                                             X = initial_density,
                                             Y = initial_pressure,
                                             normalize_Y = False,
                                             model_type='GP', 
                                             acquisition_type='EI',
                                             initial_design_numdata=0)

myBopt.run_optimization(max_iter=5)

myBopt.plot_acquisition()