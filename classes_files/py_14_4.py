# outer function
def display():
    a = 500
    print("This is the start of outer function!")

    # inner function
    def show():
        print("This is the inner function!")
        print(a)

        def go():
            print(a)

        go()
    show()
    print("This is the end of the outer function!")

display()