import openpyxl
import numpy as np
from matplotlib import pyplot as plt
from method1 import *
from method2 import *

# Функция 1
def F1(x):
    F = 6 * x[0]**2 - 4 * x[0] * x[1] + 3 * x[1]**2 + 4 * np.sqrt(5) * (x[0] + 2 * x[1]) + 22
    return F

# Функция 2
def F2(x):
    F = 4.9 * (x[0]**2 - x[1]**2) + (x[0] - 1)**2
    return F

def grad_F1(x):
    grad = np.zeros(2)
    grad[0] = 12 * x[0] - 4 * x[1] + 4 * np.sqrt(5)
    grad[1] = -4 * x[0] + 6 * x[1] + 8 * np.sqrt(5)
    return grad

def hessian_F1(x):
    d2f_dx0x0 = 12
    d2f_dx0x1 = -4
    d2f_dx1x0 = -4
    d2f_dx1x1 = 6
    return np.array([[d2f_dx0x0, d2f_dx0x1], [d2f_dx1x0, d2f_dx1x1]])

def grad_F2(x):
    grad = np.zeros(2)
    grad[0] = 9.8 * x[0] + 2 * x[0] - 9.8 * x[1] - 2
    grad[1] = -9.8 * x[0] + 9.8 * x[1]
    return grad

def hessian_F2(x):
    d2f_dx0x0 = 9.8 + 2
    d2f_dx0x1 = -9.8
    d2f_dx1x0 = -9.8
    d2f_dx1x1 = 9.8
    return np.array([[d2f_dx0x0, d2f_dx0x1], [d2f_dx1x0, d2f_dx1x1]])


# Параметры точности
Eps1 = 0.01
Eps2 = 0.00001

# Начальные точки
x0_1 = np.array([0.0, 0.0])
x0_2 = np.array([10.0, 10.0])

# ЗАДАЧА:
# Найти минимум функций F1 и F2




def graphics(f, grad_F, hessian_F, x0):
    # 1) Метод сопряженных градиентов

    x, W = method1(f, grad_F, hessian_F, x0, Eps1)
    print(W)
    print(iter)

    fig, ax = plt.subplots()
    x = np.linspace(min(W[:][0]) - 1, max(W[:][0]) + 1, 400)
    y = np.linspace(min(W[:][1]) - 1, max(W[:][1]) + 1, 400)
    X, Y = np.meshgrid(x, y)
    Z = f([X, Y])
    levels=sorted([f(point) for point in W])
    contour = ax.contour(X, Y, Z, sorted(levels), colors='k')
    ax.clabel(contour, inline=True, fontsize=8)

    ax.scatter(W[:][0], W[:][1], c='b', marker='o')

    for i in range(len(W) - 1):
        ax.annotate("", xy=(W[i + 1][0], W[i + 1][1]), xytext=(W[i][0], W[i][1]),
                    arrowprops=dict(arrowstyle="->", color='r'))

    ax.set_xlim(min(W[:][0]) - 1, max(W[:][0]) + 1)
    ax.set_ylim(min(W[:][1]) - 1, max(W[:][1]) + 1)

    # Показать график
    plt.show()





    

graphics(F1, grad_F1, hessian_F1, x0_1)
