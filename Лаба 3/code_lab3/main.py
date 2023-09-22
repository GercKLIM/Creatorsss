import openpyxl
import numpy as np
from method1 import *
from method2 import *
from method3 import *

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

# Начальные точки
x0_1 = np.array([0.0, 0.0])
x0_2 = np.array([10.0, 10.0])

# ЗАДАЧА:
# Найти минимум функций F1 и F2


wb = openpyxl.load_workbook('results/res1.xlsx')
sheet = wb.active


def main(F, grad_F, x0):
    # 1) Метод сопряженных градиентов

    #print(method1(F2, grad_F2, x0_1, Eps1))

    x, iter = method1(F, grad_F, x0, Eps1)
    sheet['B4'] = "(" + str("{:.2f}".format(x[1])) + ", " + str("{:.2f}".format(x[1])) + ")"
    sheet['B5'] = str("{:.2f}".format(F1(x)))
    sheet['B6'] = iter
    sheet['B7'] = iter * 3

    x, iter = method1(F, grad_F, x0, Eps2)
    sheet['C4'] = "(" + str("{:.5f}".format(x[1])) + ", " + str("{:.5f}".format(x[1])) + ")"
    sheet['C5'] = str("{:.5f}".format(F1(x)))
    sheet['C6'] = iter
    sheet['C7'] = iter * 3

    # 2) Метод Флетчера-Ривса

    x, iter = method2(F, grad_F, x0, Eps1)
    sheet['D4'] = "(" + str("{:.2f}".format(x[1])) + ", " + str("{:.2f}".format(x[1])) + ")"
    sheet['D5'] = str("{:.2f}".format(F1(x)))
    sheet['D6'] = iter
    sheet['D7'] = iter * 4

    x, iter = method2(F, grad_F, x0, Eps2)
    sheet['E4'] = "(" + str("{:.5f}".format(x[1])) + ", " + str("{:.5f}".format(x[1])) + ")"
    sheet['E5'] = str("{:.5f}".format(F1(x)))
    sheet['E6'] = iter
    sheet['E7'] = iter * 4

    # 3) Метод Полака-Рибьера
    x, iter = method3(F, grad_F, x0, Eps1)
    sheet['F4'] = "(" + str("{:.2f}".format(x[1])) + ", " + str("{:.2f}".format(x[1])) + ")"
    sheet['F5'] = str("{:.2f}".format(F1(x)))
    sheet['F6'] = iter
    sheet['F7'] = iter * 7
    x, iter = method3(F, grad_F, x0, Eps2)
    sheet['G4'] = "(" + str("{:.5f}".format(x[1])) + ", " + str("{:.5f}".format(x[1])) + ")"
    sheet['G5'] = str("{:.5f}".format(F1(x)))
    sheet['G6'] = iter
    sheet['G7'] = iter * 7

main(F1, grad_F1, x0_1)
wb.save('results/res1.xlsx')        
