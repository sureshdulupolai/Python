try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = a / b
    print(c)

except:
    print('This is an Exception!')

else:
    print("No Exceptions Encountered!")

# the else block goes to work when no exceptions occur\
# except like "if" condition
# run only one thing