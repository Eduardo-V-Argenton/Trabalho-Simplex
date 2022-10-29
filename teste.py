from simplex import *

fact = Factory()
simplex = fact.create_simplex(2,2, True, 2,2)
simplex.insert(0, [3,2,0])
simplex.insert(1, [2,1,10], 3)
simplex.insert(2, [1,5,15], 3)
simplex.insert_extras()
simplex.insert_aux_line()
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

