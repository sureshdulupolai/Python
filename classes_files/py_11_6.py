def func(arrone):
    print(arrone)

# given one arguments for one parameter
func([10, 20, 30])

# given 3 positional argument, when one parameter is defined
# func(*[10, 20, 30])

def funcOne(arrtwo):
    print(*arrtwo)

funcOne([10, 20, 30])

# variable-length positional argument
# ----------------------------------------------------------------------------
def print_it(*args):        # pack all data
    print(args)             # print all pack args
    print(*args)            # unpack all args again and print all unpack args

print()
print_it(10, 20, 30, 40, 50)
print()
print_it([10, 20, 30, 40, 50, 60])
print()
print_it(*[10, 20, 30])
print()
print_it([10, 20], [30, 40], [50, 60])
print()
print_it({10, 20}, {30, 40}, {50, 60})
print()
print_it({10:20}, {30:40})

