import numpy as np

from simplex2 import *

# fact = Factory()
# simplex = fact.create_simplex(3, 4, False,2,2)
# simplex.insert(0, [1, 2, 3, 4, 0])
# simplex.insert(1, [5, 9, 2, 3, 21], 0)
# simplex.insert(2, [3, 0, 2, 0, 75], 2)
# simplex.insert(3, [5, 3, 0, 0, 145], 3)
# simplex.execute()
# for i in simplex.algorithms:
#     print(i)
#     print('=====================')

matrix = np.zeros([4, 4], dtype=float)
matrix[0] = [0, 3, 4, 0]
matrix[1] = [1, 1, 5, 13]
matrix[2] = [3, 4, 2, 9]
matrix[3] = [2, 6, 7, 18]
simplex = Simplex(matrix)
print(simplex.algorithms[0])
