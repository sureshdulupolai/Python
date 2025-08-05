# map(), filter(), reduce(), together

import math
lst = [5, 10, 15, 20, 25]
lst_radius = map(math.radians, lst)
lst_rad_2d = map(lambda x : round(x, 2), lst_radius)
print(list(lst_rad_2d))

print()
# one line 
lst_rad_2d = map(lambda m: round(m,2), map(math.radians, lst))
print(list(lst_rad_2d))

def func(n):
    return n > 1000

lst = [10, 20, 30, 40, 50]
lstSquare = map(lambda n : n * n, lst)
lstFilter = filter(func, lstSquare)
print(list(lstFilter))