try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = a / b
    print(c)

except:
    print('This is an Exception!')

finally:
    print("No Exceptions Encountered!")


# the finally block goes to work when an exceptions is encountered and even it's not
# in short, the finally block goes to work in all conditons