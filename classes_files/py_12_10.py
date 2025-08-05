# lambda with map(), 
# filter() is like if statment is "True" then return value, else the value is false then skip the value
# reduce()

# using lambda with map()
lst1 = [5, 10, 15, 20, 25]
m = map(lambda n : n * n, lst1)
print(list(m))

# using lambda with filter()
f = filter(lambda n : n % 5 == 0, lst1)
print(list(f))

# using lambda with reduce()
from functools import reduce
lst2 = [1, 2, 3, 4, 5]
s = reduce(lambda x, y: x + y, lst2)
p = reduce(lambda x, y: x * y, lst2)
print(s)
print(p)
print(s,p)