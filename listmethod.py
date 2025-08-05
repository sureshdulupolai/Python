def appendData(var1, var2):
    i = []
    i = var1 + [var2]
    return i

def removeData(var1, var2):
    var3 = var1 + []
    var4 = []
    for i in var3:
        if var2 == i:
            continue
        else:
            var4 += [i]
    return var4

def insertData(var1, var2, var3):
    var4 = []
    if len(var1) <= var2:
        for i in var1:
            var4 += [i]
        var4 += [var3]
    else:
        for ind, ele in enumerate(var1):
            if var2 == ind:
                var4 += [var3]
            else:
                var4 += [ele]
    return var4

def popData(var1):
    var2 = []
    for i in range(len(var1) - 1):
        var2 += [var1[i]]
    return var2

def oddNo(var1):
    var3 = []
    for ele in var1:
        if ele % 2 != 0:
            var3 += [ele]
    return var3

def evenNo(var1):
    var3 = []
    for ele in var1:
        if ele % 2 == 0:
            var3 += [ele]
    return var3

def tpl(var1):
    tpl = ()
    for i in var1:
        tpl += (i, )
    return tpl

# not work because concatinate doesn't work in python
# def st(var1):
#     sets = set()
#     for i in var1:
#         sets = {i}
#     return sets

def dictionaryIndex(var1, var2 = 0):
    dt = {}
    for i,j in enumerate(var1):
        dt[i + var2] = j
    return dt

def listDictionary(var1):
    var2 = {}
    for i in var1:
        for k, j in enumerate(i):
            var2[j] = i[k + 1]
            break
    return var2

def length(var1):
    k = 0
    for i in var1:
        k += 1
    return k

def convertSign(*var1):
    var2 = []
    for i in var1:
        if isinstance(i, int):
            var = (i - (i * 2))
            return var
        elif isinstance(i, (list, tuple, set)):
            for p in i:
                var3 = convertSign(p)
                var2 += [var3]
            return var2
    
def search(var1, var2):
    for i in var1:
        if isinstance(i, int):
            if i == var2:
                var3 = ('Already Exist')
                return var3
            
        elif isinstance(i, (list, tuple, set)):
            var = search(i, var2)
            return var
        
