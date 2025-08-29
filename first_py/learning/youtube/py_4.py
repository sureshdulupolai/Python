# accept a year and check if it a leap year or not
var_one = int(input("Enter a year to check leap yr aur not : "))
if (var_one % 4 == 0 and var_one % 100 != 0) or (var_one % 400 == 0):
    print("This is a \"Leap Year \"")

else: 
    print('This is \"Not a Leap Year\"')