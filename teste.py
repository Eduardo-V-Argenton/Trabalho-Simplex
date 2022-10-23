from simple import *
from simplex import Simplex

num_var = 2
num_rest = 2
x = Simplex(num_rest, num_var)
x.insert(0, [5,2,5])
x.insert(1, [2,1,6])
x.insert(2, [10,12,60])
execute(x)
print(x.get_algorithm())
# x.alter_line(0, np.subtract(x.matrix[0], x.matrix[1]))
#x.alter_line(1, x.matrix[1] / 2)
#print()
#y = select_pivot(x)
#print(y)