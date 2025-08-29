if (0.1 + 0.2 == 0.3):
    print("true")
else:
    print("false")

if (True + 2 == 3):
    print("equal")
else:
    print("!equal")

a = 256
b = 256
print(a is b)

a = 257
b = 257
print(a is b)

# type error 
# different datatype opertion
print(sum('12345'))

#
if (3 > 2) > 1:
    print("Ture")
else:
    print("False")

# output will be --> syntax error
# convert into octal no = 0o1 = 1
if 1 == 01:
    print("True")
else:
    print("False")

#
num = 1
while num < 5:
    print(num, end=" ")
    num += 1
    if num == 3:
        break

# 
a = input("Enter First Number : ") # 10
b = input("Enter Second Number : ") # 20
c =  a + b
# 1020 beacuse input function is by default in string tu number enter it is also a "integer string"
print(c)

# 2, 3
# 1  2    -- index value
num = [1, 2, 3]
print(num[1:100])

