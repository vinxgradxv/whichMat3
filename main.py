# This is a sample Python script.
from BinarySolver import BinarySolver
from IterationSystemSolver import IterationSystemSolver
from NewtonSolver import NewtonSolver
from Result import Result
from SimpleIterationSolver import SimpleIterationSolver
from input_manager import is_terminal, is_system, get_solver_type, get_function_from_console, get_system_from_console, \
    get_solver_type_from_file, get_function_from_file, is_system_from_file, get_system_from_file

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

binary_solver = BinarySolver()
newton_solver = NewtonSolver()
simple_iteration_solver = SimpleIterationSolver()
iteration_system_solver = IterationSystemSolver()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    is_terminal = is_terminal()
    if is_terminal:
        if is_system():
            current_system = get_system_from_console()
            print("Метод простых итераций")
            result = iteration_system_solver.solve(current_system)
            if result != Result.SUCCESS:
                print("Во время решения уравнения было выясненно, что решить уравнение данным методом невозможно!")
        else:
            tp = get_solver_type()
            current_func = get_function_from_console()
            if tp == 1:
                print("Метод половинного деления")
                result = binary_solver.solve(current_func)
                if result != Result.SUCCESS:
                    print("Во время решения уравнения было выясненно, что решить уравнение данным методом невозможно!")
            if tp == 2:
                print("Метод Ньютона")
                result = newton_solver.solve(current_func)
                if result != Result.SUCCESS:
                    print("Во время решения уравнения было выясненно, что решить уравнение данным методом невозможно!")
            if tp == 3:
                print("Метод простых итераций")
                result = simple_iteration_solver.solve(current_func)
                if result != Result.SUCCESS:
                    print("Во время решения уравнения было выясненно, что решить уравнение данным методом невозможно!")
    else:
        f = open("test1.txt", "r")
        is_syst = is_system_from_file(f)
        if is_syst:
            print("Метод простых итераций")
            current_system = get_system_from_file(f)
            result = iteration_system_solver.solve(current_system)
            if result != Result.SUCCESS:
                print("Во время решения уравнения было выясненно, что решить уравнение данным методом невозможно!")
        elif not is_syst:
            tp = get_solver_type_from_file(f)
            current_func = get_function_from_file(f)
            if tp == 1:
                print("Метод половинного деления")
                result = binary_solver.solve(current_func)
                if result != Result.SUCCESS:
                    print("Во время решения уравнения было выясненно, что решить уравнение данным методом невозможно!")
            if tp == 2:
                print("Метод Ньютона")
                result = newton_solver.solve(current_func)
                if result != Result.SUCCESS:
                    print("Во время решения уравнения было выясненно, что решить уравнение данным методом невозможно!")
            if tp == 3:
                print("Метод простых итераций")
                result = simple_iteration_solver.solve(current_func)
                if result != Result.SUCCESS:
                    print("Во время решения уравнения было выясненно, что решить уравнение данным методом невозможно!")

