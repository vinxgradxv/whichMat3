import math

from Result import Result
from output_manager import *


class BinarySolver:
    def solve(self, function):
        l = function.a
        r = function.b
        print_binary_headers()
        print_separator(80)
        index = 0
        while True:
            x = (l + r) / 2
            fa = function.calc_function(l)
            fb = function.calc_function(r)
            fx = function.calc_function(x)
            delta = abs(l - r)
            print_binary_row(index, l, r, x, fa, fb, fx, delta)

            if fa*fx < 0 and fx * fb < 0:
                return Result.MULTIPLE_SOLUTIONS
            elif fa * fx > 0 and fx * fb > 0:
                return Result.NO_SOLUTION
            elif fa * fx < 0:
                r = x
            elif fx * fb < 0:
                l = x
            elif abs(function.calc_function(x) < function.accuracy):
                return Result.SUCCESS
            if delta < function.accuracy:
                return Result.SUCCESS
            index += 1

