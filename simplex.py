import numpy as np

class Simplex:

    def __init__(self, num_rest, num_var, fo_min = False):
        self.num_rest = num_rest
        self.num_var = num_var
        self.num_lines = 0
        self.num_coloumns = 0
        self.fo_min = fo_min
        self.algorithms = []
    
    
    def insert_num_coloumns(self):
        self.num_coloumns = self.num_var + self.num_rest + 2
    

    def insert_num_lines(self):
        self.num_lines = self.num_rest + 1


    def insert(self,line, values):
        matrix = self.get_algorithm()
        matrix[line][1:self.num_var + 1] = values[:-1]
        matrix[line][-1] = values[-1]


    def insert_extras(self):
        matrix = self.get_algorithm()
        for i in range(1, self.num_lines):
            matrix[i][self.num_var + i] = 1
        if(self.fo_min):
            matrix[0][0] = -1
        
        else:
            matrix[0] = np.negative(matrix[0])
            matrix[0][0] = 1


    def generate_matrix(self):
        self.algorithms.append(np.zeros([self.num_lines, self.num_coloumns], dtype=float))


    def insert_line(self, line, new_line):
        matrix = self.get_algorithm()
        matrix[line] = new_line


    def get_algorithm(self, index = -1):
        return self.algorithms[index]

    
    def select_pivot(self):
        matrix = self.get_algorithm()
        for elements in matrix[0][1:self.num_var + 1]:
            if(elements < 0):
                break
        else:
            return 0

        pivot_candidates = {}
        for i, element in enumerate(matrix[0]):
            if(element < 0):
                pivot_candidates[i] = element
        if(self.fo_min):
            pivot_coloumn = max(pivot_candidates)
        else:
            pivot_coloumn = min(pivot_candidates)
        pivot_coloumn_values = []
        for i,elements in enumerate(matrix):
            if(i == 0):
                continue
            if(elements[pivot_coloumn] > 0):
                pivot_coloumn_values.append(elements[self.num_coloumns - 1] / elements[pivot_coloumn])
        pivot_line = np.nanargmin(pivot_coloumn_values) + 1
        return {'line': pivot_line, 'coloumn': pivot_coloumn, 'element': matrix[pivot_line][pivot_coloumn]}
    
    
    def execute(self):
        self.insert_extras()
        while True:
            matrix = self.get_algorithm()
            pivot = self.select_pivot()
            if(pivot == 0):
                break
            self.generate_matrix()
            new_pivot_line = matrix[pivot['line']] / pivot['element']
            self.insert_line(pivot['line'], new_pivot_line)
            for i in range(0, self.num_lines):
                if(i == pivot['line']):
                    continue
                new_line = ((- matrix[i][pivot['coloumn']]) * new_pivot_line) + matrix[i]
                self.insert_line(i, new_line)


class SpecialSimplex(Simplex):

    def __init__(self, num_rest, num_var, num_xf, num_a, fo_min = False):
        super().__init__(num_rest, num_var, fo_min)
        self.num_xf = num_xf
        self.num_a = num_a
        self.has_a = []
        self.has_xf = []


    def insert_num_coloumns(self):
        self.num_coloumns = self.num_var + self.num_xf + self.num_a + 2
    

    def insert_num_lines(self):
        self.num_lines = self.num_rest + 2
    
    # 0 -> No esp
    # 1 -> Only xf
    # 2 -> only a
    # 3 -> Both
    def insert(self,line, values, esp_res = 0):
        matrix = self.get_algorithm()
        matrix[line][1:self.num_var + 1] = values[:-1]
        matrix[line][-1] = values[-1]
        if(esp_res == 1):
            self.has_xf.append(line)
        elif(esp_res == 2):
            self.has_a.append(line)
        elif(esp_res == 3):
            self.has_a.append(line)
            self.has_xf.append(line)
        else:
            return -1


    def insert_extras(self):
        matrix = self.get_algorithm()
        for i, line in enumerate(self.has_xf):
            matrix[line][self.num_var + i + 1] = 1
        for i, line in enumerate(self.has_a):
            matrix[line][self.num_var + self.num_xf + i + 1] = 1
        if(self.fo_min):
            matrix[0][0] = -1
        
        else:
            matrix[0] = np.negative(matrix[0])
            matrix[0][0] = 1


class Factory:
    
    def create_simplex(self, num_rest, num_var, fo_min = False, num_xf = 0, num_a = 0):
        if(num_a == 0):
            simplex = Simplex(num_rest, num_var, fo_min)
        else:
            simplex = SpecialSimplex(num_rest, num_var, num_xf, num_a, fo_min)
        simplex.insert_num_coloumns()
        simplex.insert_num_lines()
        simplex.generate_matrix()
        return simplex

    
    
    


