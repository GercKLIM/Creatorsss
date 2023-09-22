import numpy as np
import matplotlib.pyplot as plt
 
# Функция
def F(x):
    return 6 * x[0]**2 - 4 * x[0] * x[1] + 3 * x[1]**2 + 4 * np.sqrt(5) * (x[0] + 2 * x[1]) + 22

# Градиент функции F
def grad_F(x):
    dF_x = 12 * x[0] - 4 * x[1] + 4 * np.sqrt(5)
    dF_y = -1 * 4 * x[0] + 6 * x[1] + 4 * np.sqrt(5) * 2
    return np.array([dF_x, dF_y])


def goldsection(f,df,d,x,alpham,rho,t):

    flag = True
    a = 0
    b = alpham
    fk = f(x)
    gk = df(x)
 
    phi0 = fk
    dphi0 = np.dot(gk, d)
    alpha = b * 0.5
 
    while flag:
        newfk = f(x + alpha * d)
        phi = newfk
        if (phi - phi0) <= (rho * alpha * dphi0):
            if (phi - phi0) >= ((1 - rho) * alpha * dphi0):
                flag = False
            else:
                a = alpha
                b = b
                if (b < alpham):
                    alpha = (a + b) / 2
                else:
                    alpha = t * alpha
        else:
            a = a
            b = alpha
            alpha = (a + b) / 2
    return alpha

def method1(x0, Eps):
    imax = 10000
    W = np.zeros((2, imax))
    epo=np.zeros((2, imax))

    W[:, 0] = x0
    i = 1
    x = x0
    grad = grad_F(x)
    delta = sum(grad ** 2)
 
    while i < imax and delta > Eps:
        p = -grad_F(x)
        x0 = x
        alpha = goldsection(F, grad_F, p, x, 1, 0.1, 2)
        x = x + alpha * p
        W[:, i] = x
        if i % 5 == 0:
            epo[:,i] =np.array((i,delta))

        grad = grad_F(x)
        delta = sum(grad ** 2)
        i = i + 1
 
    print("Количество итераций:", i)
    print("Вычисленное   решение:")
    print(x, '\n')
    W = W [:, 0: i] # Запись точки итерации
 
    return [W, epo]
 
def main():
    X = np.arange(-5, 5, 0.05)
    Y = np.arange(-5, 5, 0.05)
    [x, y] = np.meshgrid(X, Y)

    f = 6 * x**2 - 4 * x * y + 3 * y**2 + 4 * np.sqrt(5) * (x + 2 * y) + 22 # заданная функция
    Eps = 0.01

    plt.contour(x, y, f, 20) # рисуем 20 контурных линий функции
    x0 = np.array([-1.2, 1])

    list_out = method1(x0, Eps)
    W=list_out[0]
    epo=list_out[1]
    plt.plot(W[0, :], W [1, :]) # Рисуем траекторию схождения точки итерации
    plt.show()

main()

