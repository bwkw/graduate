import numpy as np
import matplotlib.pyplot as plt
import GPy
import GPyOpt

data = 1
x_all = np.load("density_d0.01-15.0-0.01.npy")
y_all = np.load("pressure_d0.01-15.0-0.01.npy")

x_all = np.insert(x_all,0,0)
y_all = np.insert(y_all,0,0)

initial_density = np.array([])
initial_pressure = np.array([])

for i in range(2):
    p = i*1500
    initial_density = np.append(initial_density, x_all[p])
    initial_pressure = np.append(initial_pressure, y_all[p])

print(initial_density)
initial_density = initial_density.reshape((-1,1)) #n×1の行列に変換
initial_pressure = initial_pressure.reshape((-1,1))

def f(density):
    global data
    print("data_num : " , data)
    print("next density is ", density)
    pressure = float(input("pressure : "))
    data += 1
    return pressure


bounds = [{'name': 'a', 'type': 'continuous', 'domain': (0.0, 15.0)}]
myBopt = GPyOpt.methods.BayesianOptimization(f=f,
                                             domain=bounds,
                                             X = initial_density,
                                             Y = initial_pressure,
                                             normalize_Y = False,
                                             model_type='GP', 
                                             acquisition_type='EI',
                                             initial_design_numdata=0)

for _ in range(10):
    myBopt.run_optimization(max_iter=1)
    myBopt.plot_acquisition()
    plt.show()
