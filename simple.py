import numpy as np

algorithms = []

def select_pivot(matrix):
    for elements in matrix[0]:
        if(elements < 0):
            break
    else:
        return 0
    num_cols = matrix.shape[1]
    pivot_coloumn = np.where(matrix[0] == min(matrix[0][1:-1]))[0][0]
    pivot_coloumn_values = []
    for i,elements in enumerate(matrix):
        if(i == 0):
            continue
        pivot_coloumn_values.append(elements[num_cols - 1] / elements[pivot_coloumn])
    pivot_line = np.nanargmin(pivot_coloumn_values) + 1
    return {'line': pivot_line, 'coloumn': pivot_coloumn, 'element': matrix[pivot_line][pivot_coloumn]}


def execute(simplex):
    while True:
        matrix = simplex.get_algorithm()
        pivot = select_pivot(matrix)
        if(pivot == 0):
            break
        simplex.generate_matrix()
        new_pivot_line = matrix[pivot['line']] / pivot['element']
        simplex.insert_line(pivot['line'], new_pivot_line)
        for i in range(0, simplex.num_lines):
            if(i == pivot['line']):
                continue
            new_line = ((- matrix[i][pivot['coloumn']]) * new_pivot_line) + matrix[i]
            simplex.insert_line(i, new_line)
            
        

        
    
