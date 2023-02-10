import numpy
import math
import matplotlib.pyplot as plt

list_X = [2, 6, 10, 14, 18, 22]
list_Y = [3.1, 6.7, 9.5, 11.9, 14.0, 15.5]


def determinant(matr):
    return matr[0][0]*matr[1][1]*matr[2][2] + matr[0][1]*matr[1][2]*matr[2][0] + matr[0][2]*matr[1][0]*matr[2][1] - matr[0][2]*matr[1][1]*matr[2][0] - matr[0][0]*matr[1][2]*matr[2][1] - matr[0][1]*matr[1][0]*matr[2][2]


def sum_mult(_list, power):
    sum = 0
    for val in _list:
        sum+= val**power
    return sum


def sum_mult_lists(list1: list, list2: list):
    sum = 0
    for i in range(len(list1)):
        sum += list1[i] * list2[i]
    return sum


def sum_mult_lists_pow2(list1: list, list2: list):
    sum = 0
    for i in range(len(list1)):
        sum += list1[i] * list1[i] * list2[i]
    return sum


def sum_sqrt(_list: list):
    return sum(list(map(lambda x: x**2, _list)))


def linear_func(list_X: list, list_Y: list):
    a = (len(list_X) * sum_mult_lists(list_X, list_Y) - sum(list_X) * sum(list_Y)) / (len(list_X) * sum_sqrt(list_X) - (sum(list_X))**2)
    b = (1.0/len(list_X)) * sum(list_Y) - a * (1.0/len(list_X)) * sum(list_X)

    return (round(a,2), round(b,2))


def power_func(list_X: list, list_Y: list):
    list_lnX = list(map(lambda x: math.log(x, math.exp(1)), list_X))
    list_lnY = list(map(lambda x: math.log(x, math.exp(1)), list_Y))

    ln_ab = linear_func(list_lnX, list_lnY)

    a = ln_ab[0]
    b = math.exp(ln_ab[1])

    return (round(a,2), round(b,2))


def exp_func(list_X: list, list_Y: list):
    list_lnY = list(map(lambda x: math.log(x, math.exp(1)), list_Y))

    ab = linear_func(list_X, list_lnY)

    a = ab[0]
    b = math.exp(ab[1])

    return (round(a,2), round(b,2))


def quadr_fun(list_X: list, list_Y: list):
    A = [0]*5
    B = [0]*3
    X = [0]*3

    for i in range(5):
        if i == 0:
            A[i] = len(list_X)
        else:
            A[i] = sum_mult(list_X, i)

    B[0] = sum_mult_lists_pow2(list_X, list_Y)
    B[1] = sum_mult_lists(list_X, list_Y)
    B[2] = sum(list_Y)

    delt = [
        [A[4],A[3],A[2]],
        [A[3],A[2],A[1]],
        [A[2],A[1],A[0]]
    ]

    delt1 = [
        [B[0], A[3], A[2]],
        [B[1], A[2], A[1]],
        [B[2], A[1], A[0]]
    ]
    delt2 = [
        [A[4], B[0], A[2]],
        [A[3], B[1], A[1]],
        [A[2], B[2], A[0]]
    ]
    delt3 = [
        [A[4], A[3], B[0]],
        [A[3], A[2], B[1]],
        [A[2], A[1], B[2]]
    ]

    print(determinant(delt))
    print(determinant(delt1))
    print(determinant(delt2))
    print(determinant(delt3))

    X[0] = determinant(delt1) / determinant(delt)
    X[1] = determinant(delt2) / determinant(delt)
    X[2] = determinant(delt3) / determinant(delt)

    return (round(X[0],2), round(X[1],2), round(X[2],2))


def S_linear(coef, list_X, list_Y):
    sum = 0
    for i in range(len(list_X)):
        sum += ((coef[0] * list_X[i] + coef[1]) - list_Y[i]) ** 2
    return sum


def S_pow(coef, list_X, list_Y):
    sum = 0
    for i in range(len(list_X)):
        sum +=  (coef[1] * (list_X[i] ** coef[0]) - list_Y[i]) ** 2
    return sum


def S_exp(coef, list_X, list_Y):
    sum = 0
    for i in range(len(list_X)):
        sum +=  (coef[1] * math.exp(coef[0] * list_X[i]) - list_Y[i]) ** 2
    return sum


def S_quadr(coef, list_X, list_Y):
    sum = 0
    for i in range(len(list_X)):
        sum +=  (coef[0] * (list_X[i] ** 2) + coef[1] * list_X[i] + coef[2] - list_Y[i]) ** 2
    return sum


linear_coef = linear_func(list_X, list_Y)
linear_y = [linear_coef[0] * x + linear_coef[1] for x in list_X]

power_coef = power_func(list_X, list_Y)
power_y = [power_coef[1] * (x ** power_coef[0]) for x in list_X]

exp_coef = exp_func(list_X, list_Y)
exp_y = [exp_coef[1] * math.exp(exp_coef[0] * x) for x in list_X]

quadr_coef = quadr_fun(list_X, list_Y)
quadr_y = [quadr_coef[0] * x * x + quadr_coef[1] * x + quadr_coef[0] for x in list_X]

linear = f"Линейная функция: a = {linear_coef[0]}, b = {linear_coef[1]} " \
         f"S(a,b) = {round(S_linear(linear_coef, list_X, list_Y),2)}"
power = f"Степенная функция: a = {power_coef[0]}, b = {power_coef[1]} " \
        f"S(a,b) = {round(S_pow(power_coef, list_X, list_Y),2)}"
exp = f"Показательная функция: a = {exp_coef[0]}, b = {exp_coef[1]} " \
        f"S(a,b) = {round(S_exp(exp_coef, list_X, list_Y),2)}"
quadr = f"Квадратичная функция: a = {quadr_coef[0]}, b = {quadr_coef[1]}, c = {quadr_coef[2]} " \
        f"S(a,b) = {round(S_quadr(quadr_coef, list_X, list_Y),2)}"

print("Лучшая функция:")

S_list = [S_linear(linear_coef, list_X, list_Y), S_pow(power_coef, list_X, list_Y),S_exp(exp_coef, list_X, list_Y),S_quadr(quadr_coef, list_X, list_Y)]

if S_list.index(min(S_list)) == 0:
    print('Лмнейная')
if S_list.index(min(S_list)) == 1:
    print('Степенная')
if S_list.index(min(S_list)) == 2:
    print('Показательная')
if S_list.index(min(S_list)) == 3:
    print('Квадратичная')

print(linear)
print(power)
print(exp)
print(quadr)

plt.scatter(list_X, list_Y)
plt.plot(list_X, linear_y, color = 'black', label = 'Линейная')
plt.plot(list_X, power_y, color = 'red', label = 'Степенная')
plt.plot(list_X, exp_y, color = 'green', label = 'Экспоненциальная')
plt.plot(list_X, quadr_y, color = 'blue', label = 'Квадратичная')
plt.legend()
plt.show()




