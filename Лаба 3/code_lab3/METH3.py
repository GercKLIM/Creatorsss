import numpy as np

# Определение функции, которую необходимо минимизировать
def F(x):
    return 6 * x[0]**2 - 4 * x[0] * x[1] + 3 * x[1]**2 + 4 * np.sqrt(5) * (x[0] + 2 * x[1]) + 22

# Определение градиента функции
def grad_F(x):
    grad = np.zeros(2)
    grad[0] = 12 * x[0] - 4 * x[1] + 4 * np.sqrt(5)
    grad[1] = -4 * x[0] + 6 * x[1] + 8 * np.sqrt(5)
    return grad

# Параметры метода Полака-Рибьера с коррекцией шага
max_iterations = 1000
tolerance = 1e-6

# Начальное значение
x = np.array([0.0, 0.0])
d = -grad_F(x)
delta_new = np.dot(d, d)

for i in range(max_iterations):
    gradient = grad_F(x)
    
    alpha = np.dot(d, gradient) / delta_new
    x_new = x + alpha * d
    
    if np.linalg.norm(gradient) < tolerance:
        break
    
    gradient_new = grad_F(x_new)
    beta = np.dot(gradient_new, gradient_new - gradient) / delta_new
    
    # Коррекция шага
    alpha = alpha / (1 - beta)
    x_new = x + alpha * d
    
    gradient_new = grad_F(x_new)
    
    delta_new = np.dot(d, d)
    beta = np.dot(gradient_new, gradient_new - gradient) / delta_new
    d = -gradient_new + beta * d
    x = x_new

# Вывод результата
print("Минимум функции:", F(x))
print("Оптимальные значения переменных:", x)
