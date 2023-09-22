import math as m
import numpy as np
import matplotlib.pyplot as plt

# Функция 1
def F1():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection="3d")

    x, y = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
    z =  6 * x**2 - 4 * x * y + 3 * y**2 + 4 * np.sqrt(5) * (x + 2 * y) + 22
    ax.plot_surface(x, y, z)
    plt.show()

# Функция 2
def F2():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection="3d")

    x, y = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
    z =  4.9 * (x**2 - y**2) + (x - 1)**2
    ax.plot_surface(x, y, z)
    plt.show()

F1()
F2()