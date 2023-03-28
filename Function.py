import math


class Function:
    def __init__(self, tp, accuracy, a, b, k1, k2, k3, k4):
        self.tp = tp
        self.accuracy = accuracy
        self.a = a
        self.b = b
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4

    def calc_first_function(self, x):
        return self.k1 * x * x * x + self.k2 * x * x + self.k3 * x + self.k4

    def calc_second_function(self, x):
        return self.k1 * math.sin(x) * math.sin(x) + self.k2 * x * x + self.k3

    def calc_third_function(self, x):
        return self.k1 * math.pow(math.e, -x) + self.k2 * math.sin(x) * math.sin(x)

    def calc_fourth_function(self, x):
        return self.k1 * x * x * x + self.k2 * x + self.k3

    def calc_function(self, x):
        if self.tp == 1:
            return self.calc_first_function(x)
        elif self.tp == 2:
            return self.calc_second_function(x)
        elif self.tp == 3:
            return self.calc_third_function(x)
        elif self.tp == 4:
            return self.calc_fourth_function(x)

    def calc_first_function_first_dep(self, x):
        return self.k1 * 3 * x * x + self.k2 * 2 * x + self.k3

    def calc_second_function_first_dep(self, x):
        return self.k1 * 2 * math.sin(x) * math.cos(x) + self.k2 * 2 * x

    def calc_third_function_first_dep(self, x):
        -self.k1 * math.pow(math.e, -x) + self.k2 * 2 * math.sin(x) * math.cos(x)

    def calc_fourth_function_first_dep(self, x):
        return self.k1 * 3 * x * x + self.k2

    def calc_function_first_dep(self, x):
        if self.tp == 1:
            return self.calc_first_function_first_dep(x)
        elif self.tp == 2:
            return self.calc_second_function_first_dep(x)
        elif self.tp == 3:
            return self.calc_third_function_first_dep(x)
        elif self.tp == 4:
            return self.calc_fourth_function_first_dep(x)

    def calc_first_function_second_dep(self, x):
        return self.k1 * 3 * 2 * x + self.k2 * 2

    def calc_second_function_second_dep(self, x):
        return self.k1 * 2 * (math.cos(x) * math.cos(x) - math.sin(x) * math.sin(x)) + self.k2 * 2

    def calc_third_function_second_dep(self, x):
        return self.k1 * math.pow(math.e, -x) + self.k2 * 2 * (math.cos(x) * math.cos(x) - math.sin(x) * math.sin(x))

    def calc_fourth_function_second_dep(self, x):
        return self.k1 * 3 * 2

    def calc_function_second_dep(self, x):
        if self.tp == 1:
            return self.calc_first_function_second_dep(x)
        elif self.tp == 2:
            return self.calc_second_function_second_dep(x)
        elif self.tp == 3:
            return self.calc_third_function_second_dep(x)
        elif self.tp == 4:
            return self.calc_fourth_function_second_dep(x)

    def calc_function_for_iteration(self, x, alpha):
        return x + alpha * self.calc_function(x)

    def calc_function_for_iteration_dep(self, x, alpha):
        return 1 + alpha * self.calc_function_first_dep(x)