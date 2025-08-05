# passing a function as an argument to another function
# ------------------------------------------------------------------------
# a global function is accessible to every local function

# 
def sumx(x, y, g):
    print(x + y)
    g()

#
def func():
    print("Hello")

#
f = func
s = sumx
s(10, 20, f)


# ---------------------------------------------------
print()
# 
def sumx1(x, y):
    print(x + y)
    func1()

#
def func1():
    print("Hello")

#
sm = sumx1
sm(10, 20)
