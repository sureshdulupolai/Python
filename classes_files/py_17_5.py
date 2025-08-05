try:
    a = int(input("enter the value of a : "))
    b = int(input("enter the value of b: "))
    c = a / b
    print('c = ',c)

except ZeroDivisionError as zde:           # create new variable as "zde"
    print(zde)
    print(zde.args)             # args = argument
