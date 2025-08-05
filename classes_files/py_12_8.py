# filter()
# ------------------------------------------

# 
lst_one = ['A', 'X', 'Y', '3', 'M', '4', 'D']

f1 = filter(str.isalpha, lst_one)
print(list(f1))

# method 1
print()
def filterss(func, arr):
    d = []
    for i in arr:
        if func(i):
            d += [i]
    return d

print(filterss(str.isalpha, lst_one))

# note: 
# both the statements are TRUE
print('A'.isalpha())
print(str.isalpha('A'))             # str is replace with 'A'

# method 2 
def funt(ele):
    if ele.isalpha():
        return True
    else:
        return False

def filterss(func, arr):
    d = []
    for i in arr:
        if func(i):
            d += [i]
    return d

print(filterss(funt, lst_one))

# 
print()
lst_two = [5, 10, 18, 27, 25]

def fun(n):
    if n % 5 == 0:
        return True
    else:
        return False
    
var = filter(fun, lst_two)
print(list(var))