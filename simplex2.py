import numpy as np


class Simplex:

    def __init__(self, matrix_problem, fo_min=False):
        mp_num_line, mp_num_column = matrix_problem.shape
        self.num_var = mp_num_column - 2
        self.num_rest = mp_num_line - 1
        self.fo_min = False
        self.xf = []
        self.n_xf = []
        self.a = []
        self.read_config_column(matrix_problem[:, 0])
        self.num_lines = self.num_rest + 1
        self.num_columns = self.num_rest + len(self.xf) + len(self.n_xf) + len(self.a)
        self.algorithms = []
        self.generate_matrix()
        self.define_initial_algorithm(matrix_problem[:, 1:])

    # 1 --> < || <=
    # 2 --> > || >=
    # 3 --> =

    def read_config_column(self, line) -> None:
        self.fo_min = line[0] == 1
        for i, e in enumerate(line[1:], 1):
            if e == 0:
                break
            elif e == 1:
                self.xf.append(i)
            elif e == 2:
                self.n_xf.append(i)
                self.a.append(i)
            elif e == 3:
                self.a.append(i)
            else:
                raise Exception("Invalid element in config line")

    def generate_matrix(self) -> None:
        self.algorithms.append(np.zeros([self.num_lines, self.num_columns]))

    def get_algorithm(self, index=-1):
        return self.algorithms[index]

    def define_fo_line(self, line, matrix):
        matrix[0][:self.num_var] = line[:-1]
        matrix[0] = np.negative(matrix[0])
        matrix[0][-1] = line[-1]
        for i in range(0, len(self.a)):
            matrix[0][self.num_var + len(self.xf) + len(self.n_xf) + i] = min(
                x for x in matrix[0][:self.num_var]) * 100000 * (-1 if self.fo_min else 1)

    def define_initial_algorithm(self, matrix_problem) -> None:
        matrix = self.get_algorithm()
        self.define_fo_line(matrix_problem[0, :], matrix)

        for i, line in enumerate(matrix[1:], 1):
            line[:self.num_var] = matrix_problem[i][:-1]
            line[-1] = matrix_problem[i][-1]
            matrix[i] = line

        control_column = [0, 0]
        for i, line in enumerate(matrix[1:, self.num_var:-1], 1):
            if i in self.xf:
                line[control_column[0]] = 1
                control_column[0] += 1
            elif i in self.n_xf:
                line[control_column[0]] = -1
                control_column[0] += 1
            if i in self.a:
                line[len(self.n_xf) + len(self.xf) + control_column[1]] = 1
                control_column[1] += 1
            matrix[i, self.num_var:-1] = line

    def execute(self) -> None:
        matrix = self.get_algorithm()
        min_var_fo = min(matrix[0][:self.num_var])
        while min_var_fo < 0:
            pivot_line = self.define_pivot(np.where(matrix[0] == min_var_fo), matrix)
            min_var_fo = min(matrix[0][:self.num_var])
            min_var_fo = 10

    def define_pivot(self, column_index, matrix) -> int:
        pivot_div_val = 0
        pivot_line = 0
        for i in range(1, self.num_lines):
            if matrix[i][column_index] != 0:
                res = matrix[i][-1] / matrix[i][column_index]
                if res < pivot_div_val or pivot_div_val == 0:
                    pivot_div_val = res
                    pivot_line = i
        return pivot_line
