import numpy as np

# Параметры метода градиентного спуска
max_iterations = 10000
speed = 1.0
beta = 0.5  # Фактор дробления шага


def method2(f, grad_f, x, Eps):
    for i in range(max_iterations):
        gradient = grad_f(x)
        koef = speed
        
        while f(x - koef * gradient) > f(x):
            koef *= beta
        
        x_new = x - koef * gradient
        
        if np.linalg.norm(gradient) < Eps:
            break
        
        x = x_new

    print("Минимум функции:", f(x))
    print("Вычисленное значение переменной:", x)
    print("Количество итераций:", i)
