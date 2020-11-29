import GPyOpt
import matplotlib.pyplot as plt
import numpy as np

try_ = 1

initial_x = np.array([-1, 0.5])
initial_y = np.array([1, 0.25])

initial_x = initial_x.reshape((-1,1)) #n×1の行列に変換
initial_y = initial_y.reshape((-1,1))

def f(x):
    global try_

    print("Try : " , try_ , "next x is ", x)
    score = float(input("Input y : "))

    try_ += 1

    return score

bounds = [{'name': 'a', 'type': 'continuous', 'domain': (-10,10)}]
myBopt = GPyOpt.methods.BayesianOptimization(f=f,
                                             domain=bounds,
                                             X = initial_x,
                                             Y = initial_y,
                                             normalize_Y = False,
                                             model_type='GP', 
                                             acquisition_type='EI',
                                             initial_design_numdata=0)

myBopt.run_optimization(max_iter=5)

print(myBopt.x_opt)
print(myBopt.fx_opt)

myBopt.plot_acquisition()