# communication with function

# parameters (x, y, z)
def cal_sum(x, y, z):
    return x + y + z

# argument (10, 20, 30)
print(cal_sum(10, 20, 30))

var_one = cal_sum(15, 25, 35)
print(var_one)

def cal_sum_2(x, y):
    return x + y

var_thr = cal_sum(14, 15, 16) + cal_sum_2(17, 18)
print(var_thr)      # 80

# user enter
var_four = cal_sum(
    int(input("Enter The First 1st Number: ")),
    int(input("Enter The First 2nd Number: ")),
    int(input("Enter The First 3rd Number: "))
)

print(var_four)

# global variable as argument
a = 10; b = 20; c = 30
var_five = cal_sum(a, b, c)
print(var_five)


# ---------------------------------------------------------

def One_func(x,y):
    return x + y

def One_func(x, y, z):
    return x + y + z

# print(One_func(10, 20))           # not work in python
print(One_func(10, 20, 30))         # work in python, because declare in 39 again