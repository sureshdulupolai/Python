def func():
    a = 45

    b = 6.28

    print(a, b, s)
    # print(id(s))

a = 20
b = 3.14
s = "python"


func()
print(a, b, s)
# print(id(s))


print()
# ---------------------------------------------
def func():
    a = 45

    global b    # now ( b ) become global variable inside function, if you will use this then all ( b ) in global update with this data
    b = 6.28

    print(a, b, s)
    # print(id(s))

a = 20
b = 3.14
s = "python"


func()
print(a, b, s)
# print(id(s))