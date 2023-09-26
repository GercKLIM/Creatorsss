import numpy as np
import scipy.optimize as opt


def method2(F, grad_F, hessian_F, x0, Eps):

    # Установка параметров метода
    max_iterations = 1000

    # Итерации метода Ньютона с оптимальным шагом и наискорейшим спуском
    for iteration in range(max_iterations):
        gradient = grad_F(x0)
        hessian = hessian_F(x0)
        
        # Вычислите шаг метода Ньютона
        delta_x_newton = -np.linalg.solve(hessian, gradient)
        
        # Определите функцию, которая будет минимизирована для вычисления наискорейшего спуска
        def line_search(alpha):
            return F(x0 + alpha * delta_x_newton)
        
        # Найдите оптимальный шаг с помощью наискорейшего спуска
        alpha_optimal = opt.golden(line_search)
        
        # Обновление точки
        x0 += alpha_optimal * delta_x_newton
        
        # Проверка критерия остановки
        if np.linalg.norm(alpha_optimal * delta_x_newton) < Eps:
            break

    # Результат
    return x0
