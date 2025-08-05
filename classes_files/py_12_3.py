# assigning a function to a variable 
# and calling a function using the variable

# example 1 
# --------------------------------------------------------------
def func():
    print("Hello")

def sumf(x, y):
    print(x + y)

# 
f = func            # passing a function as a value to a variable 
f()                 # this is a call to the function

# 
g = sumf            # passing a function as a value to a variable 
g(10, 20)           # this is a call to the function