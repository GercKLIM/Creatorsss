import numpy as np

def method1(F, grad_F, hessian_F, x, Eps):

    max_iterations = 1000
    iter_x = [[x[0], x[1]]]

    for iteration in range(max_iterations):
        gradient = grad_F(x)
        hessian = hessian_F(x)
        delta_x = -np.linalg.solve(hessian, gradient)
        x += delta_x

        iter_x.append([x[0], x[1]])
        # Проверка критерия остановки
        if np.linalg.norm(delta_x) < Eps:
            break

    return x, iter_x
