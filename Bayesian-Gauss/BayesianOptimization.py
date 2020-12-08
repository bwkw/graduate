import numpy as np
import matplotlib.pyplot as plt
import GPy
import GPyOpt

data = 1
x_all = np.load("density_L6.0-7.0-0.002_L7.0-L25.0-0.036.npy")
y_all = np.load("pressure_L6.0-7.0-0.002_L7.0-L25.0-0.036.npy")

max_density = np.max(x_all) 
max_pressure = np.max(y_all)

#max_density 9.481481481481481
#max_pressure 1835345.523354229 → 50

n = len(x_all)

missing_value_rate = 0.01
sample_index = np.sort(np.random.choice(np.arange(n), int(n*missing_value_rate), replace=False))

initial_density = np.copy(x_all[sample_index])
initial_pressure = np.copy(y_all[sample_index])


initial_density = initial_density.reshape((-1,1)) #n×1の行列に変換
initial_pressure = initial_pressure.reshape((-1,1))

def f(density):
    global data
    print("data_num : " , data)
    print("next density is ", density)
    pressure = float(input("pressure : "))
    data += 1
    return pressure


bounds = [{'name': 'a', 'type': 'continuous', 'domain': (0.0, 9.5)}]
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
