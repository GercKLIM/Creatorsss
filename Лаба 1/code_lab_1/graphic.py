import matplotlib.pyplot as plt
import numpy as np
import math as m
# Функция

def f(x):              # Функция
    R1 = m.sin((x**4 + x**3 - 3 * x - 30**(1/3)) / 2)
    R2 = m.tanh((4 * m.sqrt(3) * x**3 - 2 * x - 6 * m.sqrt(2) + 1) / (-2 * m.sqrt(3) * x**3 + 3 * m.sqrt(2)))
    varF = R1 + R2 + 1.2
    return varF 

interval = [[0, 1], [0, 0.5005], [0, 0.25075], [0, 0.125875], [0, 0.0634375], [0.031218749999999997, 0.0634375],
            [0.031218749999999997, 0.047828125], [0.031218749999999997, 0.040023437499999995]]




x = np.linspace(0, 1, 100)
y_f = []  
for elem in x:
    y_f.append(f(elem))
plt.plot(x, y_f, linewidth=2.0)

def graphic(interval):
    
    x_f = np.linspace(0, 1, 100)
    y_f = []  
    for elem in x:
        y_f.append(f(elem))
    plt.plot(x, y_f, linewidth=2.0)

    sdvig = -9
    for iter in interval:
        sdvig += 1
        x, y = [iter[0], iter[1]],  [sdvig, sdvig]
        plt.plot(x, y, marker = 'o')

    plt.show()

graphic(interval)