# map()
# -----------------------------------------------
import math

lst = [5, 10, 15, 20, 25]

#
m1 = map(math.radians, lst)
print(m1)           # return object -> use list
print(list(m1))

#
print()
m2 = map(math.factorial, lst)
print(list(m2))

# method 1 
print()
def maps_one(lst):
    import math
    d = []
    for i in lst:
        d += [math.radians(i)]
    return d

lst1 = [5, 10, 15, 20, 25]
print(maps_one(lst1))

# method 2 - sir
print()
def maps_two(func, arr):
    t = []
    for j in arr:
        t += [round(func(j),2)]
    return t

lst2 = [5, 10, 15, 20, 25]
print(maps_two(math.radians, lst2))

# cube
print()
def cube(n):
    return n * n * n

def maps_two(func, arr):
    t = []
    for j in arr:
        t += [round(func(j),2)]
    return t

lst2 = [5, 10, 15, 20, 25]
print(maps_two(cube, lst2))         # argument pass inside functon => map(cube)