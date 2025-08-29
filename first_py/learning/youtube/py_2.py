# Accept Two Number and print the greatest between them 
var_one = int(input("Enter a First Value : "))
var_two = int(input("Enter a Second Value :"))
if var_one > var_two:
    print("{} is greater From {}".format(var_one,var_two))
elif var_one < var_two:
    print("{1} is greater From {0}".format(var_one,var_two))
else:
    print("Both Are Equal")