from simplex import *

fact = Factory()
simplex = fact.create_simplex(3,3, True)
simplex.insert(0, [1,-2,-3,0])
simplex.insert(1, [3,4,9,81])
simplex.insert(2, [5,6,7,27])
simplex.insert(3, [1,2,3,47])
simplex.execute()

for i in simplex.algorithms:
    print(i)
    print('=====================')

# execute(x)
#print(x.get_algorithm())
# x.alter_line(0, np.subtract(x.matrix[0], x.matrix[1]))
#x.alter_line(1, x.matrix[1] / 2)
#print()
#y = select_pivot(x)
#print(y)

