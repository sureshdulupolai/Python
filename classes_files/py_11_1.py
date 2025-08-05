# functions

def func_one():
    print("This is Line 1 of func_one")
    print("This is Line 2 of func_one")
    print("This is Line 3 of func_one")

# calling a function

# -------------------------------------------------------------------------------
# print(func_one())     # print all from function and last line print "None"
# print("hi",func_one())
# -------------------------------------------------------------------------------

func_one()
print()
func_one()

# for loop function

for i in range(0, 3):
    print()
    func_one()