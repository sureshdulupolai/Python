# topic : py_14_1 to -- is also know as "Scope Of a Variable" and "File Handaling"
# -------------------------------------------
def fun_one():
    a = 45
    print(a)

    def fun_two():
        a = 90
        print(a)

    fun_two()
    print(a)    # 45

fun_one()


# -------------------------------------------
# if a is not in gloabal space, or outside of function
# the ( gloabl ) function do not work
# to change aur update all function inside value must be use ( nonlocal )
# but it will not update global variable
# nonlocal access only one step up

def fun_one():
    a = 45
    print(a)

    def fun_two():
        nonlocal a
        a = 90
        print(a)

    fun_two()
    print(a)    # 90

fun_one()

print()
# --------------------------------------------
def fun_one():  # not this
    a = 45
    print(a)

    def fun_two():  # this will update
        # nonlocal a
        a = 90
        print(a)

        def fun_thr():
            nonlocal a
            a = 80
            print(a)

        fun_thr()
        print(a)    
    fun_two()
    print(a)    # 90

fun_one()

print()
# ------------------------------------
def fun_one():
    a = 45
    print(a)

    def fun_two():
        global a
        a = 90
        print(a)

    fun_two()
    print(a)    # 90

a = 10
print(a)
fun_one()
print(a)