import matplotlib.pyplot as plt
import numpy as np
import math as m

# Метод Дихотомии
def method_1(f, a, b, e):
    iteration = 0 
    interval = [[a, b]]
    delta = e / 10

    while abs(b - a) > e:
        C = (a + b) / 2
        x1 = C - delta
        x2 = C + delta
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1
        interval.append([a, b])
        iteration +=1 

    x = (a + b) / 2
    interval.append([x, x])
    return x, iteration, interval


# Метод Золотого Сечения
def method_2(f, a, b, e):
    iteration = 0
    interval = [[a, b]]
    gold = (1 + m.sqrt(5)) / 2 # Золотое сечение

    while abs(b - a) > e:
        x1 = b - (b-a) / gold
        x2 = a + (b-a) / gold
        if f(x1) >= f(x2):
            a = x1
        else: 
            b = x2
        iteration +=1
        interval.append([a, b])
    
    x = (a + b) / 2
    interval.append([x, x])
    return x, iteration, interval

# Процедура для вывода
def print_info(f, a, b, Eps):
    x_m1, iteration_m1, interval_m1 = method_1(f, a, b, Eps)
    x_m2, iteration_m2, interval_m2 = method_2(f, a, b, Eps)

    print("---------------------------------")
    print("Точность Eps =", Eps)
    print()
    print("Метод Дихотомии:")
    print("x =",x_m1)
    print("f(x) =", f(x_m1))
    print("Количество итераций =", iteration_m1)
    print()
    print("Метод Золотого сечения:")
    print("x =",x_m2)
    print("f(x) =", f(x_m2))
    print("Количество итераций =", iteration_m2)

    graphic(f, x_m1, interval_m1, iteration_m1, "Дихотомии", Eps)
    graphic(f, x_m2, interval_m2, iteration_m2, "Золотого Сечения", Eps)


# Функция для графика
def graphic(f, x_sdvig, interval, iteration, name, Eps):
    
    # Интервалы
    x_f = np.linspace(0, 1, 100)
    y_f = []  
    for elem in x_f:
        y_f.append(f(elem))
    plt.plot(x_f, y_f, linewidth=2.0)

    # График функции
    sdvig = -1 * iteration - 2 + f(x_sdvig)
    for iter in interval:
        sdvig += 1
        x, y = [iter[0], iter[1]],  [sdvig, sdvig]
        plt.plot(x, y, marker = 'o')

    title = 'Метод ' + str(name) + ',  Точность Eps = ' + str(Eps)
    plt.title(title)
    plt.show()


# Дано:
def f(x):              # Функция
    R1 = m.sin((x**4 + x**3 - 3 * x - 30**(1/3)) / 2)
    R2 = m.tanh((4 * m.sqrt(3) * x**3 - 2 * x - 6 * m.sqrt(2) + 1) / (-2 * m.sqrt(3) * x**3 + 3 * m.sqrt(2)))
    varF = R1 + R2 + 1.2
    return varF 
a, b = 0, 1            # Интервал
Eps1 = 0.01            # Точность
Eps2 = 0.000001
Eps3 = 10**-17

# Найти минимум функции

print_info(f, a, b, Eps1)
print_info(f, a, b, Eps2)
print_info(f, a, b, Eps3)
