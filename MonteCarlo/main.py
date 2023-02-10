import math
import random
import sys
import numpy as np
import matplotlib.pyplot as plt


def triangle_func(x, n=4):
    if 0 <= x < n:
        return 10 * x / n
    elif n <= x < 20:
        return 10 * ((x - 20) / (n - 20))


def integral_func(x, n=4):
    return math.sqrt(11 - n * (math.sin(x) ** 2))


def r_func(p, n = 4):
    return math.sqrt((11 + n) * (math.cos(p) ** 2) + (11 - n) * (math.sin(p) ** 2))


def rand_dots_func(N, a, b, func, n=4):
    count = 0

    rnd_list_X_outsid = []
    rnd_list_Y_otside = []

    rnd_list_X_inside = []
    rnd_list_Y_inside = []

    for i in range(N):
        rnd_x = random.uniform(0, a)
        rnd_y = random.uniform(0, b)
        if rnd_y < func(rnd_x, n):
            count += 1
            rnd_list_X_inside.append(rnd_x)
            rnd_list_Y_inside.append(rnd_y)
        else:
            rnd_list_X_outsid.append(rnd_x)
            rnd_list_Y_otside.append(rnd_y)
    return count, rnd_list_X_inside, rnd_list_Y_inside, rnd_list_X_outsid, rnd_list_Y_otside


def calc_area():
    listX = list(np.arange(0, 20, 0.1))
    listY = [triangle_func(x) for x in listX]
    a = max(listX)
    b = abs(max(listY) - min(listX))
    N = 100
    M, X_in, Y_in, X_out, Y_out = rand_dots_func(N, a, b, triangle_func)
    S = M / N * a * b
    print("Площадь треугольника = " + str(S))

    plt.axhline(y=0, color='black', label = 'y=0')
    plt.axvline(x=0, color='black', label = 'x=0')
    plt.scatter(X_in, Y_in, color='green', label = 'Точки внутри')
    plt.scatter(X_out, Y_out, color='red',label = 'Точки снаружи')
    plt.plot(listX, listY, color='blue', label = 'y=f(x)')
    plt.legend()
    plt.show()


def calc_integral():
    listX = list(np.arange(0, 5, 0.125))
    listY = [integral_func(x) for x in listX]

    a = max(listX)
    b = max(listY)

    N = 200

    M, X_in, Y_in, X_out, Y_out = rand_dots_func(N, a, b, integral_func)

    S = M / N * a * b

    print("Определенный интеграл = " + str(S))

    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')
    plt.scatter(X_in, Y_in, color='green',label = 'Точки внутри')
    plt.scatter(X_out, Y_out, color='red',label = 'Точки снаружи')
    plt.plot(listX, listY, color='blue', label = 'y=f(x)')
    plt.legend()
    plt.show()


def calc_pi():
    R = 4
    N = 200
    list_z = [random.uniform(0, 2 * R) for i in range(2 * N)]
    list_rnd_x_out = []
    list_rnd_y_out = []
    list_rnd_x_in = []
    list_rnd_y_in = []

    M = 0

    for j in range(N):
        if ((list_z[j] - R) ** 2) + ((list_z[j + N] - R) ** 2) < R ** 2:
            M += 1
            list_rnd_x_in.append(list_z[j])
            list_rnd_y_in.append(list_z[j + N])
        else:
            list_rnd_x_out.append(list_z[j])
            list_rnd_y_out.append(list_z[j + N])

    S = M / N * ((2 * R) ** 2)
    pi = S / (R ** 2)
    print("pi = " + str(pi))

    list_x = [R + R * math.cos(p) for p in np.arange(0, 2 * math.pi, 0.05)]
    list_y = [R + R * math.sin(p) for p in np.arange(0, 2 * math.pi, 0.05)]

    plt.scatter(list_rnd_x_out, list_rnd_y_out, color = 'red', label = 'Точки снаружи')
    plt.scatter(list_rnd_x_in, list_rnd_y_in, color = 'green', label = 'Точки внутри')
    plt.plot(list_x, list_y, color='black', label = 'y=f(x)')
    plt.legend()
    plt.show()

def calc_polar():
    list_x = [r_func(phi) * math.cos(phi) for phi in np.arange(0, 2 * math.pi, 0.05)]
    list_y = [r_func(phi) * math.sin(phi) for phi in np.arange(0, 2 * math.pi, 0.05)]

    a = 4
    b = 3

    N = 179

    list_x_in = []
    list_y_in = []
    list_x_out = []
    list_y_out = []

    phiphi = []
    roro = []
    M = 0

    for i in range(N):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        if x > 0:
            phiphi.append(math.atan(y / x))
        elif x < 0:
            phiphi.append(math.atan(y / x) + math.pi)
        elif y > 0:
            phiphi.append(math.pi / 2)
        else:
            phiphi.append(math.pi * 3 / 2)

        roro.append(math.sqrt((x ** 2) + (y ** 2)))

        if roro[i] < r_func(phiphi[i]):
            M += 1
            list_x_in.append(x)
            list_y_in.append(y)
        else:
            list_x_out.append(x)
            list_y_out.append(y)


    S = M / N * a * b * 4

    print("Площадь фигуры = " + str(S))

    plt.scatter(list_x_in,list_y_in, color = 'green', label = 'Точки внутри')
    plt.scatter(list_x_out, list_y_out, color = 'red', label = 'Точки снаружи')
    plt.plot(list_x, list_y, color = 'black')
    plt.legend()
    plt.show()

calc_area()
calc_integral()
calc_pi()
calc_polar()
