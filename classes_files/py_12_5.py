# lambda functions
# ------------------------------------------------------
# example 1


# method 1 
def func(x):
    return x * x * x

f = func
print(f(
    int(input("Enter a Value: "))
))

# 
var = (lambda n : n * n * n)(5)
print(var)

# example 2 - multiple value

# method 1 
var = (lambda a, b, c: (a * b * c) / (a + b + c))(1, 2, 3)
print(var)

# method 2 
func = (lambda a, b, c: (a * b * c) / (a + b + c))
var = func(
    int(input("Enter Value 1: ")), 
    int(input("Enter value 2: ")),
    int(input("Enter Value 3: "))
)
print(var, 'debug 1')

# method 3 - list compere
func = (lambda a, b, c: (a * b * c) / (a + b + c))
var = func(
    *[int(input("Enter Value {}: ".format(ele + 1))) for ele in range(0, 3)]
)
print(var)

# method 4.1 - return 2 value
func = (lambda a, b, c: ((a * b * c), (a + b + c)))
var = func(
    *[int(input("Enter Value {}: ".format(ele + 1))) for ele in range(0, 3)]
)
print(var)

# method 4.2 - return 2 value
func = (lambda a, b, c: ((a * b * c), (a + b + c)))
var1, var2 = func(
    *[int(input("Enter Value {}: ".format(ele + 1))) for ele in range(0, 3)]
)
print(var1, var2)


# example 3
var = (lambda x : 10)(5)            # return 10
print(var)

# 
var = (lambda x : x + 10)(5)
print(var)

# 
var = (lambda x : (lambda y : y + 20)(x + 10))(5)
print(var)


# example 4
def funx(n):                                # funx(10)
    return n * n

var = (lambda x : funx(x + x))(5)           # (x + x)(5) = funx(5 + 5)
print(var)