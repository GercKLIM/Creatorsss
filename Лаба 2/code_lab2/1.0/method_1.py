import numpy as np

# Определение градиента функции
def grad_f(x):
    grad = np.zeros(2)
    grad[0] = 2 * x[0] + 2 * x[1] + 4
    grad[1] = 6 * x[1] + 2 * x[0] + 5
    return grad

# Определение метода золотого сечения для одномерной минимизации
def golden_section(f, a, b, Eps):
    delta = (1 + np.sqrt(5)) / 2  # Золотое сечение
    x1 = b - (b - a) / delta
    x2 = a + (b - a) / delta

    while abs(b - a) > Eps:
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1

        x1 = b - (b - a) / delta
        x2 = a + (b - a) / delta

    return (a + b) / 2

# Параметры метода наискорейшего спуска
max_iterations = 100000
#Eps = 0.01

# Начальное значение
#x0 = np.array([0.0, 0.0])


def method1(f, grad_f, x, Eps):
    for i in range(max_iterations):
        gradient = grad_f(x)
        direction = -gradient
        
        # Одномерная минимизация с использованием метода золотого сечения
        alpha = golden_section(lambda alpha: f(x + alpha * direction), 0, 1, Eps)
        
        # Обновление переменной x
        x = x + alpha * direction
        
        if np.linalg.norm(gradient) < Eps:
            break
    
    # Вывод результата
    print("Минимум функции:", f(x))
    print("Вычисленное значение переменной:", x)
    print("Количество итераций:", i)
#method1(f, x0, Eps)

