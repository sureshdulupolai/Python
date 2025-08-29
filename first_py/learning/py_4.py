# create a input for string character ( One time )
# check wether cat and hat both are present in 'catinahat' 'bazingaa' or not

var_one = "Catinahat"
var_two = var_one.lower()
if ("cat" in var_two) and ("hat" in var_two):
    print("Cat and Hat Present in {}".format(var_one))
else:
    print("Cat and Hat Not Present in, This Statment {}".format(var_one))