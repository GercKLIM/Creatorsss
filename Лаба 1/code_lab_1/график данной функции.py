import matplotlib.pyplot as plt
import numpy as np
import math as m

def f(x):              # Функция
    R1 = m.sin((x**4 + x**3 - 3 * x - 30**(1/3)) / 2)
    R2 = m.tanh((4 * m.sqrt(3) * x**3 - 2 * x - 6 * m.sqrt(2) + 1) / (-2 * m.sqrt(3) * x**3 + 3 * m.sqrt(2)))
    varF = R1 + R2 + 1.2
    return varF 

x = np.linspace(0, 1, 100)
y_f = []  
for elem in x:
    y_f.append(f(elem))
plt.plot(x, y_f, linewidth=2.0)
plt.show()