def func():
    a = 45

    global b        # now b is global variable
    b = 6.28

    print(locals())     # b will not print, because ( b ) is now global and question need local variable
    print()

    print(globals())
    print()

a = 20
b = 3.14
c = "Python"
print(locals())
print()

print(globals())
print()

func()