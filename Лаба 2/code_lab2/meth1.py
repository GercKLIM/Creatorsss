import math as m
import numpy as np

# Функция 1
def F1(x, y):
    F = 6 * x**2 - 4 * x * y + 3 * y**2 + 4 * m.sqrt(5) * (x + 2 * y) + 22
    return F

def alt_F1(kappa)

def Grad_F1(x, y):
    dF_x = 12 * x - 4 * y + 4 * m.sqrt(5)
    dF_y = -1 * 4 * x + 6 * y + 4 * m.sqrt(5) * 2
    return [dF_x, dF_y]

def Norm(Grad_F, x, y):
    return m.sqrt(Grad_F(x, y)[0]**2 + Grad_F(x, y)[1]**2)

def goldsection(f, a, b, e):
    gold = (1 + m.sqrt(5)) / 2 # Золотое сечение

    while abs(b - a) > e:
        x1 = b - (b-a) / gold
        x2 = a + (b-a) / gold
        if f(x1) >= f(x2):
            a = x1
        else: 
            b = x2

    x = (a + b) / 2
    return x

# Параметры точности
Eps1 = 0.01
Eps2 = 0.00001

# Начальные точки
x0 = (-2, -4)


def main(F, Grad_F, x0, Eps):
    k = 1
    x_k = [x0]
    kappa_k = 5
    omega_k = Grad_F(x_k[k][0], x_k[k][1])
    while Norm(Grad_F, x_k[k][0], x_k[k][1]) > Eps:
        kappa_k = goldsection(F[x_k[k][0] + kappa * omega_k[k][0]. F[x_k[k][1] + kappa * omega_k[k][1]])
    


main(F1, Grad_F1, x0, Eps1)