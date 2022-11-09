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
        self.num_lines = self.num_rest + 1 + (0 if not self.fo_min else 1)
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
        if not self.fo_min:
            matrix[0] = np.negative(matrix[0])
        matrix[0][-1] = line[-1]

    def define_initial_algorithm(self, matrix_problem) -> None:
        print(f'xf = {self.xf}')
        print(f'n_xf = {self.n_xf}')
        print(f'a = {self.a}')
        matrix = self.get_algorithm()
        self.define_fo_line(matrix_problem[0, :], matrix)

        for i, line in enumerate(matrix[1:], 1):
            line[:self.num_var] = matrix_problem[i][:-1]
            line[-1] = matrix_problem[i][-1]
            if i in self.xf:
                line[self.num_var + i - 1] = 1
            if i in self.n_xf:
                line[self.num_var + i - 1] = -1
            if i in self.a:
                line[self.num_var + len(self.xf) + len(self.n_xf) + i - 1] = 1
            matrix[i] = line
