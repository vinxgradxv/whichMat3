from Result import Result
import numpy
from output_manager import *


class NewtonSolver:
    def solve(self, function):
        l = function.a
        r = function.b
        last_x = None
        print_newton_headers()
        print_separator(60)
        first_dep = function.calc_function_first_dep(l)
        second_dep = function.calc_function_second_dep(l)
        for i in numpy.arange(l, r, 0.01):
            if function.calc_function_first_dep(i) * first_dep <= 0 or function.calc_function_second_dep(i) * second_dep <= 0:
                return Result.NO_SOLUTION

        if function.calc_function(l) * function.calc_function(r) > 0:
            return Result.NO_SOLUTION
        if function.calc_function(l) * function.calc_function_second_dep(l) > 0:
            last_x = l
        elif function.calc_function(r) * function.calc_function_second_dep(r) > 0:
            last_x = r
        else:
            return Result.NO_SOLUTION
        x = None
        index = 0
        while True:
            f_last_x = function.calc_function(last_x)
            f_last_dep_x = function.calc_function_first_dep(last_x)
            x = last_x - f_last_x / f_last_dep_x
            delta = abs(last_x - x)
            print_newton_row(index, last_x, f_last_x, f_last_dep_x, x, delta)
            if delta < function.accuracy:
                return Result.SUCCESS
            last_x = x
            index += 1


