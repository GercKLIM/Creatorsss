import numpy as np

def method3(F, grad_F, x, Eps):

    max_iterations = 1000
    d = -grad_F(x)
    delta_new = np.dot(d, d)
    iter = 0
    for i in range(max_iterations):
        gradient = grad_F(x)
        
        alpha = np.dot(d, gradient) / delta_new
        x_new = x + alpha * d
        
        if np.linalg.norm(gradient) < Eps:
            break
        
        gradient_new = grad_F(x_new)
        beta = np.dot(gradient_new, gradient_new - gradient) / delta_new
        
        # Коррекция шага
        alpha = alpha / (1 - beta)
        x_new = x + alpha * d
        
        gradient_new = grad_F(x_new)
        
        delta_new = np.dot(d, d)
        beta = np.dot(gradient_new, gradient_new - gradient) / delta_new
        d = -gradient_new + beta * d
        x = x_new
        iter += 1

    return x, iter
