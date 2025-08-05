# variable-length keyword arguments
# ---------------------------------------------------------------
# double ** convert into dict
def print_it(**kwargs):
    print(kwargs)
    print(list(kwargs.keys()))
    print(list(kwargs.values()))
    print(list(kwargs.items()))
    print(*list(kwargs.items()))


print_it(a = 10, b = 20, c = 30)

print()
dct = {'x':100, 'y':200, 'z':300}
# print_it(dct)        # not go direct, because this function need arguments like [a = 10, b = 20, c = 30]
print_it(**dct)

# --------------------------------------------------------------------
def func(student="Suresh", age=52):
    print()
    print("{} is the name of the student".format(student))
    print("{} is the age of {}".format(age, student))

func(student="Gurshish")

# --------------------------------------------------------------------
def func(student="Suresh", age=52, **kwargs):
    print()
    print("{} is the name of the student".format(student))
    print("{} is the age of {}".format(age, student))
    print(kwargs)
    # print(**kwargs)       # error

func(student="Gurshish", gender="Other", phone="98865354678")