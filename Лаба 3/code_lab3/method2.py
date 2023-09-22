import numpy as np
from scipy.optimize import minimize_scalar

def method2(F, grad_F, x, Eps):

    max_iterations = 1000
    d = -grad_F(x)
    delta_new = np.dot(d, d)
    iter = 0
    for i in range(max_iterations):
        iter += 1
        gradient = grad_F(x)

        # Вычисляем оптимальное значение alpha методом золотого сечения
        res = minimize_scalar(lambda alpha: F(x + alpha * d))
        alpha = res.x
        
        x_new = x + alpha * d
        
        if np.linalg.norm(gradient) < Eps:
            break
        
        gradient_new = grad_F(x_new)
        beta = np.dot(gradient_new, gradient_new) / np.dot(gradient, gradient)
        d = -gradient_new + beta * d
        x = x_new
    
    return x, iter
