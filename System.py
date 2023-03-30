import math
import numpy as np

class System:
    def __init__(self, tp, first_x, first_y, first_z, accuracy):
        self.tp = tp
        self.first_x = first_x
        self.first_y = first_y
        self.first_z = first_z
        self.accuracy = accuracy

    def get_system_string(self, tp):
        if tp == 1:
            return "x + 3*cos(x) - y^2 = 0\n2*x^2 - x*y - 5*y + 1 = 0"
        else:
            return "\"0.1x^2 + x + 0.2y^2 -0.3 = 0\\n0.2x^2 + y + 0.1xy -0.7 = 0\""

    def calc_system(self, index, x, y):
        if self.tp == 1:
            return self.calc_system_first_type(index, x, y)
        else:
            return self.calc_system_second_type(index, x, y)

    def calc_system_first_type(self, index, x, y):
        try:
            if index == 1:
                return x + 3 * np.cos(x) - y * y
            else:
                return 2 * x * x - x * y - 5 * y + 1
        except:
            print()


    def calc_system_second_type(self, index, x, y):
        if index == 1:
            return 0.1 * x * x + x + 0.2 * y * y - 0.3
        else:
            return 0.2 * x * x + y + 0.1 * x * y - 0.7

    def get_changed_system_string(self, tp):
        if tp == 1:
            return "x = - 3*cos(x) + y^2\ny = (2*x^2 - x*y + 1) / 5"
        else:
            return "x = -0.1x^2 - 0.2y^2 + 0.3\ny = -0.2x^2 - 0.1xy + 0.7"

    def solve_changed_system(self, x, y):
        if self.tp == 1:
            new_x = -3 * np.cos(x) + y * y
            new_y = (2 * x * x + x * y * 1) / 5
            return [new_x, new_y]
        else:
            new_x = -0.1*x*x-0.2*y*y+0.3
            new_y = -0.2*x*x-0.1*x*y+0.7
            return [new_x, new_y]

    def print_iteration_step(self, x, y):
        if self.tp == 1:
            print("x = - 3*cos({:.3f}) + {:.3f}^2\ny = (2{:.3f}x^2 - {:.3f} * {:.3f} + 1) / 5\n".format(x, y, x, x, y))
        else:
            print("x = -0.1 * {:.3f}^2 - 0.2 * {:.3f}^2 + 0.3\ny = -0.2 * {:.3f}^2 - 0.1 * {:.3f} * {:.3f} + 0.7\n".format(x, y, x, x, y))

    def calculate_function_for_graph(self, index, x):
        if self.tp == 1:
            return self.calculate_function_for_graph_first_type(index, x)
        else:
            return self.calculate_function_for_graph_second_type(index, x)

    def calculate_function_for_graph_first_type(self, index, x):
        if index == 1:
            return math.sqrt(x + 3 * math.log(x, 10))
        elif x != -5:
            return (2 * x * x + 1) / (x + 5)

    def calculate_function_for_graph_second_type(self, index, x):
        if index == 1:
            return np.sqrt((-0.1 * x * x - x + 0.3)/0.2)
        else:
            return (-0.2 * x * x + 0.7) / (1 + 0.1 * x)

