from Result import Result


class IterationSystemSolver:

    def solve(self, system):
        counter = 0
        while True:
            counter += 1
            print("Шаг " + str(counter))
            system.print_iteration_step(system.first_x, system.first_y)
            new_values = system.solve_changed_system(system.first_x, system.first_y)
            print("Новое значение x = {:.3f}\n".format(new_values[0]))
            print("Новое значение y = {:.3f}\n".format(new_values[1]))
            delta_x = abs(new_values[0] - system.first_x)
            delta_y = abs(new_values[1] - system.first_y)
            print("Дельта x = {:.3f}\n".format(delta_x))
            print("Дельта y = {:.3f}\n".format(delta_y))
            system.first_x = new_values[0]
            system.first_y = new_values[1]

            if delta_x < system.accuracy and delta_y < system.accuracy:
                print("Окончательное значение x = {:.3f}\n".format(new_values[0]))
                print("Окончательное значение y = {:.3f}\n".format(new_values[1]))
                return Result.SUCCESS

