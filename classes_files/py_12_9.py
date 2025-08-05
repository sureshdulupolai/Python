# reduce()
# -------------------------------------------------------------

from functools import reduce
lst = [1, 2, 3, 4, 5]

def getsum(x, y):
    return x + y

s = reduce(getsum, lst)
print(s)

# 1 + 2 
# 3 + 3
# 6 + 4 
# 10 + 5
# return 15

def getProd(x, y):
    return x * y

p = reduce(getProd, lst)
print(p)


print()
def red(ele):
    total = 0
    for i in ele:
        total += i
    return total

var = red(lst)
print(var)

# 
def red1(ele):
    total = 1
    for i in ele:
        total *= i
    return total

var2 = red1(lst)
print(var2)