import numpy as np
import scipy.optimize as opt

def method2(F, grad_F, hessian_F, x, Eps):

    max_iterations = 1000
    iter_x = [[x[0], x[1]]]

    for iteration in range(max_iterations):
        gradient = grad_F(x)
        hessian = hessian_F(x)
        
        delta_x_newton = -np.linalg.solve(hessian, gradient)
        
        def line_search(alpha):
            return F(x + alpha * delta_x_newton)
        
        alpha_optimal = opt.golden(line_search)
        
        x += alpha_optimal * delta_x_newton
        iter_x.append([x[0], x[1]])
        
        if np.linalg.norm(alpha_optimal * delta_x_newton) < Eps:
            break

    return x, iter_x
