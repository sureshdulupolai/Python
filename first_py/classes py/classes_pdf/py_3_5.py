import math
print(math.pi)
print(round((math.e),3))
print(math.sqrt(9))
print(math.fabs(-3.3))
print(math.factorial(5))
print(math.log(5))
print(math.log10(3))
# 'e' raise to 3
print(math.exp(3))
# cut all decimal value
print(math.trunc(5.4578))
print(math.ceil(3.4))
print(math.ceil(-3.4))
print(math.floor(3.4))
# difference in both ( decimal and fraction part from this value )
print(math.modf(5.54367))
# degrees()
# radians()
# sin(x)
# cos(x)
# tan(x)
# sinh(x)
# cosh(x)
# tanh(x)
# acas(x)
# asin(x)
# atan(x)
# hypot(x)



# example 
# ---------------------------------------------
# using variable
a = int(math.sqrt(9))
print(a)

# find 23 from ( 7.2356 )
import math
num = 7.2356
a = math.modf(num)
b = (round((a[0]), 2))
c = (b * 100)
print(math.trunc(c))

import math
num = 7.2356
num = math.modf(num)
num = num[0]
num = (num * 100)
print(math.trunc(num))

import math
num = 7.2356
tpl = math.modf(num)
one = math.trunc(tpl[0] * 100)
print(one)

# --------------

