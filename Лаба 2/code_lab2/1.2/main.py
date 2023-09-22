import matplotlib.pyplot as plt
import numpy as np

from method_1 import *
from method_2 import *

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

def grad_F2(x):
    grad = np.zeros(2)
    grad[0] = 9.8 * x[0] + 2 * x[0] - 9.8 * x[1] - 2
    grad[1] = -9.8 * x[0] + 9.8 * x[1]
    return grad

# Параметры точности
Eps1 = 0.01
Eps2 = 0.00001
x0 = np.array([10, 10])

'''
# 1. МЕТОД НАИСКОРЕЙШЕГО СПУСКА
print("МЕТОД НАИСКОРЕЙШЕГО СПУСКА")
print("Функция 1 :")
method1(F1, grad_F1, x0, Eps2)
print("Функция 2 :")
method1(F2, grad_F2, x0, Eps2)

print("-" * 10)
# 2. МЕТОД ГРАДИЕНТНОГО СПУСКА С ДРОБЛЕНИЕМ ШАГА
print("МЕТОД ГРАДИЕНТНОГО СПУСКА С ДРОБЛЕНИЕМ ШАГА")
print("Функция 1 :")
method2(F1, grad_F1, x0, Eps2)
print("Функция 2 :")
method2(F2, grad_F2, x0, Eps2)
'''

def graphic(F, grad_F, x0, Eps):
    X = np.arange(-5, 5, 0.05)
    Y = np.arange(-5, 5, 0.05)
    [x, y] = np.meshgrid(X, Y)
    
   
    #f = 6 * x**2 - 4 * x * y + 3 * y**2 + 4 * np.sqrt(5) * (x + 2 * y) + 22 # заданная функция
   
    #f = 4.9 * (x[0]**2 - x[1]**2) + (x[0] - 1)**2
    f = 4.9 * (x**2 - y**2) + (x - 1)**2
    plt.contour(x, y, f, 100) 
    list_out = method1(F1, grad_F1, x0, Eps2)
    W=list_out[0]
    epo=list_out[1]
    plt.plot(W[0, :], W [1, :]) 
    plt.show()

graphic(F2, grad_F2, x0, Eps2)
