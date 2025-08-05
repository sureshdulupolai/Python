# global function: func_one()
# local space or local function: func_two()
def func_one():
    print("This is start of function One")
    print("This is just before defining function Two")
    def func_two():
        print()
        print("This is start of function two")
        print("This is function two")
        print("This is end of function two")
        print()
    print("This is just after defining function two")
    func_two()
    print("This is end of function one")

func_one()

print()
print(type(func_one))       # class 'function'