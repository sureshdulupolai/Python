a = [
    'a', 'b', 'c'
]

b = [
    1, 2, 3
]

def listOfTuple(var1, var2):
    lst = []
    for i in range(len(var1)):
        tpl = ()
        lst += (var1[i], var2[i]),
    return lst

var = listOfTuple(var1 = a, var2 = b)
# print(var)

def listReverse(var1):
    v1 = var1[-1::-1]
    return v1

var = listReverse(var)
# print(var)

# skip a tuple 
def skipTupleofValue(lst, value):
    lst1 = []
    for i in lst:
        if isinstance(i, tuple):
            pass
        else:
            if value == i:
                pass
            else:
                lst1 += [i]
    return lst1

var += [2]
var = skipTupleofValue(lst = var, value = 2)
print(var)