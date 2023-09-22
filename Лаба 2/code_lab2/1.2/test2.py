import numpy as np

# Определение функции, которую необходимо минимизировать
def F(x):
    return 4.9 * (x[0]**2 - x[1]**2) + (x[0] - 1)**2

# Определение градиента функции
def grad_F(x):
    grad = np.zeros(2)
    grad[0] = 12 * x[0] - 4 * x[1] + 4 * np.sqrt(5)
    grad[1] = -4 * x[0] + 6 * x[1] + 8 * np.sqrt(5)
    return grad

# Параметры метода градиентного спуска
max_iterations = 1000
initial_learning_rate = 1.0
tolerance = 1e-6
beta = 0.5  # Фактор дробления шага

# Начальное значение
x = np.array([0.0, 0.0])

for i in range(max_iterations):
    gradient = grad_F(x)
    learning_rate = initial_learning_rate
    
    while F(x - learning_rate * gradient) > F(x):
        learning_rate *= beta
    
    x_new = x - learning_rate * gradient
    
    if np.linalg.norm(x_new - x) < tolerance:
        break
    
    x = x_new

# Вывод результата
print("Минимум функции:", F(x))
print("Оптимальные значения переменных:", x)
