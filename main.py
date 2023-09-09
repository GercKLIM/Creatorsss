import math as m

'''
R1 = m.sin((x**4 + x**3 - 3 * x - 30**(1/3)) / 2)
R2 = m.tanh((4 * m.sqrt(3) * x**3 - 2 * x - 6 * m.sqrt(2) + 1) / (-2 * m.sqrt(3) * x**3 + 3 * m.sqrt(2)))
varF = R1 + R2 + 1.2
'''
# Дано:
def f(x): return x**2  # Функция
l = [-5, 10]           # Интервал
e = 10**-17            # Точность

# Найти минимум функции

# Метод Дихотомии
def method_1(a, b, e):
    while abs(b-a) > e:
        C = (a+b)/2
        x1 = C - e
        x2 = C + e
        if f(x1) > f(x2):
            a = x1
        else:
            b = x2
    X = (a + b) / 2
    F = f(X)
    return [X, F]

# Метод Золотого Сечения
def method_2(a, b, e):
    gold = (1 + m.sqrt(5)) / 2 # Типо золотое сечение
    while abs(b-a) > e:
        x1 = b - (b-a) / gold
        x2 = a + (b-a) / gold
        if f(x1) >= f(x2):
            a = x1
        else: 
            b = x2

    X = (a + b) / 2
    F = f(X)
    return [X, F]

print(method_1(l[0], l[1], e))
print(method_2(l[0], l[1], e))





