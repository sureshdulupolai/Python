# we dont write global and local inside one fuction
# but you can write function inside function
# -------------------------------------------------
# outer function
def display():
    a = 500
    print("This is a start of the outer function!")

    # inner function
    def show():
        print("This is the inner function")

        global a
        print(a)

        # nonlocal a
        # print(a)

        a = 300
        print(a)

    show()
    print("This is the end of the outer function!")

a = 700
display()

# ------------------------------------------------------
# This all are packages all are runing in background to run python, if you will add you packages or ( import your file ), then it will add in this which is showing in below:-

# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000209E7209E00>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\user\\Desktop\\suresh\\py\\py_14_7.py', '__cached__': None, 'a': 50, 'b': 70, 'c': 90, 'var': {...}}