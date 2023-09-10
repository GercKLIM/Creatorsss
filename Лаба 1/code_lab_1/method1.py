def dichotomy_method(func, a, b, epsilon):
    while (b - a) > epsilon:
        midpoint = (a + b) / 2
        x1 = midpoint - epsilon / 2
        x2 = midpoint + epsilon / 2
        if func(x1) < func(x2):
            b = x2
        else:
            a = x1
    return (a + b) / 2

# Функция, для которой мы ищем минимум (x^2)
def f(x):
    return x**2

# Задаем начальный интервал [a, b] и точность epsilon
a = -10
b = 10
epsilon = 0.001

# Вызываем метод дихотомии для поиска минимума
minimum = dichotomy_method(f, a, b, epsilon)

print(minimum, f(minimum))
