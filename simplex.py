import numpy as np

class Simplex:

    def __init__(self, num_rest, num_var):
        self.num_rest = num_rest
        self.num_var = num_var
        self.num_lines = self.num_rest + 1
        self.num_coloumns = self.num_var + self.num_rest + 2
        self.algorithms = []
        self.generate_matrix()
        matrix = self.get_algorithm()
        matrix[0,0] = 1
        for num_line, line in enumerate(matrix):
            if(num_line == 0):
                continue
            line[num_var + num_line] = 1
        
    

    def generate_matrix(self):
        self.algorithms.append(np.zeros([self.num_lines, self.num_coloumns], dtype=float))


    def insert(self,line, values):
        matrix = self.get_algorithm()
        if(line == 0):
            values = np.negative(values)
            values[-1] = - values[-1]
        matrix[line][1:self.num_var + 1] = values[:-1]
        matrix[line][-1] = values[-1]
    

    def insert_line(self, line, new_line):
        matrix = self.get_algorithm()
        matrix[line] = new_line


    def get_algorithm(self, index = -1):
        return self.algorithms[index]
        