# arithmatic operators

print(5 + 2)            #addition operator
print(5 - 2)            # subtraction
print(5 * 2)            # multiplaction
print(5 / 2)            # division > quotient 
print(5 // 2)           # dividion > quotient , discarding (remove decimal no from diviion answer)
print(5 % 2)            # remainder
print(5 ** 2)           # exponential


# 
a = 10
a = a + 10
a += 10
a -= 10
a *= 10
a /= 10
a //= 10
a **= 10
a %= 10

# PEMDAS
# Associativity > left > to right
SUM = 5 * 2 + 3 - 4 / 6 % 3 // 5 ** 2
SUM = 5 * 2 + 3 - 4 / 6 % 3 // 25    # E
SUM = 10 + 3 - 4 / 6 % 3 // 25       # D
SUM = 10 + 3 - 0.7 % 3 // 25         # M
SUM = 10 + 3 - 0.7 // 25             # D
SUM = 10 + 3 - 0                     # D
SUM = 13 - 0                         # A
SUM = 13.0                           # S

print(5 * 2 + 3 - 4 / 6 % 3 // 5 ** 2)

# right to left,  because 2 depend on three and three depend on 5 
# 5**3 = A
# A ** 2 = B
print(2**3**5)

# left to right ( + ), # right to left inside bracket
print(2**3**2 + 4**1**2)



