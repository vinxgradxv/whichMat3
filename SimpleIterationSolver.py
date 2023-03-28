import numpy

from Result import Result
from output_manager import *


class SimpleIterationSolver:

    def get_alpha(self, function, l, r):
        mx = None
        for i in numpy.arange(l, r, 0.01):
            if mx is None or mx < abs(function.calc_function_first_dep(i)):
                mx = abs(function.calc_function_first_dep(i))
        return -1 / mx

    def solve(self, function):
        print_iteration_headers()
        print_separator(6*15)
        l = function.a
        r = function.b
        alpha = self.get_alpha(function, l, r)
        index = 0
        mn = None
        last_x = (l + r) / 2
        for i in numpy.arange(l, r, 0.01):
            if mn is None or abs(function.calc_function_for_iteration_dep(i, alpha)) < 1 and abs(function.calc_function_for_iteration_dep(i, alpha)) < mn:
                mn = abs(function.calc_function_for_iteration_dep(i, alpha))
                last_x = i

        if mn is None or mn >= 1:
            return Result.NO_SOLUTION

        while True:
            last_phi_x = function.calc_function_for_iteration(last_x, alpha)
            phi_x = function.calc_function_for_iteration(last_phi_x, alpha)
            fx = function.calc_function(last_phi_x)
            delta = abs(last_x - last_phi_x)
            print_iteration_row(index, last_x, last_phi_x, phi_x, fx, delta)
            if delta < function.accuracy:
                return Result.SUCCESS
            last_x = last_phi_x
            last_phi_x = phi_x
            index += 1