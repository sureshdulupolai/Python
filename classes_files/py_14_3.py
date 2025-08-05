# ----------------------------------------
a = 20
b = 3.14
s = "Python"

# ------------------------
dict_glob = globals()
print(dict_glob)

print()
lst = ['a', 'b', 's']

# -----------------------------------------
# particular variable excessing, with as key -> dictionary
# string convert into -> global variable of declare
print(globals()['a'])
# print(type(globals()))


# -------------------------------------------
# user input
# var = input("Enter Variable to check values: ")
# print(globals()[var])

print()
# ------------------------------------------
for ele in lst:
    print(globals()[ele])


# ------------------------------------------------------
def fun_one():
    print("inside fun_one")

def fun_two():
    print("inside fun_two")

def fun_thr():
    print("inside fun_thr")

lst = ['fun_one', 'fun_two', 'fun_thr']

f = fun_one
print(f)    # print address of function created 'fun_one'

for ele in lst:
    globals()[ele]()
    # print(globals()[ele]())   -> don't write this, because fun_one, fun_two, fun_thr not return any value. that why is print "None"