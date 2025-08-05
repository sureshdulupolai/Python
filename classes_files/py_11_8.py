def print_it(i, j, *args, x, y, **kwargs):
    print()
    print(i, j, end=" ")
    for var in args:
        print(var, end=" ")
    print(x, y, end=" ")
    for name, value in kwargs.items():
        print(name, value, end=" ")

print_it(10, 20, x = 30, y = 40)
print_it(10, 20, 100, 200, x = 30, y = 40)
print_it(10, 20, 100, 200, x = 30, y = 40, a = 5, b = 6, c = 7)
# print_it(10, 20, 100, 200, x = 30, y = 40, a = 5, b = 6, c = 7, x = 55, y = 100)      same value assign many time [x, y]