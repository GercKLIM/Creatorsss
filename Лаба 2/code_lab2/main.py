import math as m
import numpy as np

# Функция 1
def F1(x, y):
    F = 6 * x**2 - 4 * x * y + 3 * y**2 + 4 * m.sqrt(5) * (x + 2 * y) + 22
    return F

# Функция 2
#def F2(x, y):
#    F = 4.9 * (x**2 - y**2) + (x - 1)**2

# Параметры точности
Eps1 = 0.01
Eps2 = 0.00001

# ЗАДАЧА:
# Найти минимум функций F1 и F2

# 1) Метод наискорейшего спуска

# Градиент F1

def d_F1(x, y):
    dF_x = 12 * x - 4 * y + 4 * m.sqrt(5)
    dF_y = -1 * 4 * x + 6 * y + 4 * m.sqrt(5) * 2
    return [dF_x, dF_y]



def main():
    
     