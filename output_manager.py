import matplotlib.pyplot as plt
import numpy as np
from sympy import *


def print_binary_headers():
    print("         №         a         b         x      F(a)      F(b)      F(x)     |a-b|")


def print_newton_headers():
    print("         №       x_n    f(x_n)   f'(x_n)   x_{n+1}     delta")


def print_iteration_headers():
    print("              №            x_i        x_{i+1}   phi(x_{i+1})     f(x_{i+1})          delta")


def print_binary_row(index, a, b, x, fa, fb, fx, delta):
    params = [a, b, x, fa, fb, fx, delta]
    result = ""
    how_many_spaces = 10 - len(str(index))
    spaces = ""
    for j in range(how_many_spaces):
        spaces += " "
    result += spaces + str(index)

    for i in range(len(params)):
        how_many_spaces = 10 - len("{:.3f}".format(params[i]))
        spaces = ""
        for j in range(how_many_spaces):
            spaces += " "
        result += spaces + "{:.3f}".format(params[i])
    print(result)


def print_newton_row(index, last_x, f_last_x, f_last_dep_x, x, delta):
    params = [last_x, f_last_x, f_last_dep_x, x, delta]
    result = ""
    how_many_spaces = 10 - len(str(index))
    spaces = ""
    for j in range(how_many_spaces):
        spaces += " "
    result += spaces + str(index)

    for i in range(len(params)):
        how_many_spaces = 10 - len("{:.3f}".format(params[i]))
        spaces = ""
        for j in range(how_many_spaces):
            spaces += " "
        result += spaces + "{:.3f}".format(params[i])
    print(result)


def print_iteration_row(index, last_x, last_phi_x, phi_x, fx, delta):
    params = [last_x, last_phi_x, phi_x, fx, delta]
    result = ""
    how_many_spaces = 15 - len(str(index))
    spaces = ""
    for j in range(how_many_spaces):
        spaces += " "
    result += spaces + str(index)

    for i in range(len(params)):
        how_many_spaces = 15 - len("{:.3f}".format(params[i]))
        spaces = ""
        for j in range(how_many_spaces):
            spaces += " "
        result += spaces + "{:.3f}".format(params[i])
    print(result)


def print_separator(ln):
    print("-" * ln)


def print_graph(l, r, function):
    x = np.arange(l, r + 0.01, 0.01)
    plt.plot(x, function.calc_function(x))
    plt.grid(True)
    plt.show()


def print_system(l, r, ly, ry, system):
    x = np.arange(l, r + 0.01, 0.01)
    y = np.arange(ly, ry + 0.01, 0.01)
    X, Y = np.meshgrid(x, y)
    f = y
    g = system.calc_system(1, X, Y)
    plt.contour(X, Y, (f-g), [0])
    f = y
    g = system.calc_system(2, X, Y)
    plt.contour(X, Y, (f-g), [0])
    plt.grid(True)
    plt.show()






