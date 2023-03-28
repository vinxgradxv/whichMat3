from Function import Function
from System import System
from output_manager import print_graph, print_system


def is_terminal():
    while True:
        try:
            print("Если хотите ввести данные в консоль, введите - 1")
            print("Если хотите прочитать данные из файла, введите - 2")
            res = int(input())
            if res != 1 and res != 2:
                raise Exception()
            return res == 1
        except:
            print("Ошибка ввода, попробуйте еще раз")


def is_system():
    while True:
        print("Если хотите решить систему нелинейных уравнений, введите - 1")
        print("Если хотите решить нелинейное уравнение, введите - 2")
        res = input()
        if res == "1" or res == "2":
            break
        print("Ошибка ввода, попробуйте еще раз")
    return res == "1"


def get_solver_type():
    while True:
        try:
            print("1) Метод половинного деления")
            print("2) Метод Ньютона")
            print("3) Метод простых итераций")
            print("Введите желаемый способ решения уравнения: ")
            type = int(input())
            if type < 1 or type > 3:
                raise Exception()
            return type
        except:
            print("При вводе данных произошла ошибка, попробуйте снова")


def get_function_from_console():
    while True:
        try:
            print("1) k1 * x^3 + k2 * x^2 + k3 * x + k4 = 0")
            print("2) k1 * sin(x)^2 + k2 * x^2 + k3 = 0")
            print("3) k1 * e^{-x} + k2 * sin(x)^2 = 0")
            print("4) k1 * x^3 + k3 * x + k4 = 0")
            print("Введите номер уравнения, которое вы бы хотели решить:")
            tp = int(input())
            coefficients = get_coefficients_from_console(tp)
            graph_func = Function(tp, None, None, None, coefficients[0], coefficients[1], coefficients[2], coefficients[3])
            print_graph(-100, 100, graph_func)
            print("Введите промежуток, на котором вы бы хотели найти корень")
            a, b = map(float, input().split())
            graph_func = Function(tp, None, a, b, coefficients[0], coefficients[1], coefficients[2], coefficients[3])
            print_graph(a - 3, b + 3, graph_func)
            print("Введите желаемую погрешность")
            accuracy = float(input())
            return Function(tp, accuracy, a, b, coefficients[0], coefficients[1], coefficients[2], coefficients[3])
        except:
            print("При вводе данных произошла ошибка, попробуйте снова")


def get_coefficients_from_console(tp):
    results = []
    if tp == 1:
        print("Введите коэффиценты k1, k2, k3, k4:")
        results = [int(a) for a in input().split()]
    elif tp == 2 or tp == 4:
        print("Введите коэффиценты k1, k2, k3:")
        results = [int(a) for a in input().split()]
    elif tp == 3:
        print("Введите коэффиценты k1, k2:")
        results = [int(a) for a in input().split()]
    return results


def get_system_from_console():
    while True:
        try:
            print("1) x + 3*lg(x) - y^2 = 0\n2*x^2 - x*y - 5*y + 1 = 0")
            print("2) 0.1x^2 + x + 0.2y^2 -0.3 = 0\n0.2x^2 + y + 0.1xy -0.7 = 0")
            print("Выберете систему для решения")
            tp = int(input())
            if tp < 1 or tp > 2:
                raise Exception()
            graph_system = System(tp, None, None, None, None)
            print_system(-100, 100, graph_system)
            print("Введите приближенные значения x и y")
            first_x, first_y = map(float, input().split())
            print("Введите желаемую погрешность")
            accuracy = float(input())
            system = System(tp, first_x, first_y, None, accuracy)
            print_system(first_x - 10, first_x + 10, system)
            return system
        except:
            print("При вводе данных произошла ошибка, попробуйте снова")


