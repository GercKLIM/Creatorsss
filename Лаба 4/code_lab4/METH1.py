import numpy as np

# Определите функцию F(x)
def F(x):
    return 6 * x[0]**2 - 4 * x[0] * x[1] + 3 * x[1]**2 + 4 * np.sqrt(5) * (x[0] + 2 * x[1]) + 22

# Вычислите градиент функции F(x)
def gradient_F(x):
    df_dx0 = 12 * x[0] - 4 * x[1] + 4 * np.sqrt(5)
    df_dx1 = -4 * x[0] + 6 * x[1] + 8 * np.sqrt(5)
    return np.array([df_dx0, df_dx1])

# Вычислите гессиан функции F(x)
def hessian_F(x):
    d2f_dx0x0 = 12
    d2f_dx0x1 = -4
    d2f_dx1x0 = -4
    d2f_dx1x1 = 6
    return np.array([[d2f_dx0x0, d2f_dx0x1], [d2f_dx1x0, d2f_dx1x1]])

# Начальное приближение
x0 = np.array([0.0, 0.0])

# Установка параметров метода
max_iterations = 100
tolerance = 1e-6

# Итерации метода Ньютона
for iteration in range(max_iterations):
    gradient = gradient_F(x0)
    hessian = hessian_F(x0)
    delta_x = -np.linalg.solve(hessian, gradient)
    x0 += delta_x
    
    # Проверка критерия остановки
    if np.linalg.norm(delta_x) < tolerance:
        break

# Результат
minimum_x = x0
minimum_value = F(x0)

print(f"Минимум функции: x = {minimum_x}, F(x) = {minimum_value}")
