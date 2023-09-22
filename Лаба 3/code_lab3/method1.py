import numpy as np

def method1(F, grad_F, x, Eps):
    # Параметры метода сопряженных градиентов
    max_iterations = 1000

    # Начальное значение
    x = np.array([0.0, 0.0])
    d = -grad_F(x)
    delta_new = np.dot(d, d)

    iter = 0

    for i in range(max_iterations):
        gradient = grad_F(x)
        
        # Фиксированный шаг
        alpha = 0.01
        
        x_new = x + alpha * d
        
        if np.linalg.norm(gradient) < Eps:
            break
        
        gradient_new = grad_F(x_new)
        beta = np.dot(gradient_new, gradient_new - gradient) / delta_new
        d = -gradient_new + beta * d
        delta_new = np.dot(d, d)
        x = x_new
        iter += 1

    return x, iter