from listmethod import (
    insertData as inserting, appendData as appending,
    removeData as removing, popData as poping,
    oddNo, evenNo, tpl, dictionaryIndex as dInd,
    listDictionary, length, convertSign, search
)

i = [1, 2, 3]
var = appending(i, 9)
print(var)

i = [1, 4, 2, 3, 4, 5, 4, 4, 4]
var1 = removing(i, 4)
print(var1)

j = [1, 2, 3, 4]
var_one = inserting(j, 5, 10)
print(var_one)

k = [1, 2, 3, 4, 6]
varTwo = poping(k)
print(varTwo)

varOne = [1, 2, 3, 4, 5, 6]
v1 = oddNo(varOne)
print(v1)

varTwo = [1, 2, 3, 4, 5, 6]
v2 = evenNo(varTwo)
print(v2)

varThr = [1, 2, 3, 4, 5]
v3 = tpl(varThr)
print(v3)

# varFour = [10, 11, 12, 13, 14]
# v4 = st(varFour)
# print(v4)

varFive = [10, 20, 30, 40, 50]
v5 = dInd(varFive, 1)
print(v5)

varSix = [(10, 20), (30, 40), (50, 60)]
v6 = listDictionary(varSix)
print(v6)

varSeven = [(10, "Suresh"), ("Krish", 40), (50, 60.20)]
v7 = listDictionary(varSeven)
print(v7)

varEight = [10, 20, 30, 40, 50]
v8 = length(varEight)
print(v8)

varNine = [-30, [-10, 20, -30], 20, [-1, -2, 3], 10], 2
v9 = convertSign(varNine)
print(*v9)

print()
varTen = [30, 20, [10, 20], 30, 40, 50]
v10 = search(varTen, 10)
print(v10)



# -------------------------------------------------
class  Between():
    def userInput(self, a, b):
        self.firstValue = a
        self.secondValue = b

    def add(self):
        a1 = 0
        for i in range(self.firstValue, self.secondValue + 1):
            a1 += i
        return a1
    
    def multiply(self):
        a1 = 1
        for i in range(self.firstValue, self.secondValue + 1):
            a1 *= i
        return a1
# ---------------------------------------------------------

bt1 = Between()
bt1.firstValue = 1
bt1.secondValue = 5
var = bt1.add()
print(var)

bt2 = Between()
bt2.firstValue = 1
bt2.secondValue = 5
var1 = bt2.multiply()
print(var1)


# -------------------------------------------
class listFunc():
    def __init__(self, var1, var2):
        self.varOne = var1
        self.VarTwo = var2

    def add(self):
        var3 = []
        for i in self.varOne:
            var3 += [i + self.VarTwo]
        return var3
    
    def sub(self):
        var3 = []
        for i in self.varOne:
            var3 += [i - self.VarTwo]
        return var3
    
    def multi(self):
        var3 = []
        for i in self.varOne:
            var3 += [i * self.VarTwo]
        return var3

    def div(self):
        var3 = []
        for i in self.varOne:
            var3 += [round(i / self.VarTwo, 3)]
        return var3

lst = [1, 2, 3, 4, 5]
lst2 = appending(lst, 10)
print(lst2)
l1 = listFunc(lst2, 3)
var1 = dInd(l1.div(), 1)
print(var1)
# -----------------------------------------------------------


x = 10
y = id(x)
y = 20
print(x)
print(y)
# print(len(y))



print()
x = 10
y = id(x)
print(y)
y = id(x) + 10
print(y)
s = str(y)
print(s[len(s) - 3: ])