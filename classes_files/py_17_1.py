# Exceptional Handiling
# ----------------------------------------------

a = int(input("Enter the value in a : "))
b = int(input("Enter the value in b : "))
c = a/b
print(c)
print("End of the 'try-except' block")


# -------------------------------------------
try:
    a = int(input("Enter the value in a : "))
    b = int(input("Enter the value in b : "))
    c = a/b
    print(c)

except ZeroDivisionError:           # ZeroDivisionError - is inbuild class for "Zero Division Error"
    print("The value entered in 'B' is 'Zero'")

print("End of the 'try-except' block")

# logical error
# syntax error
# run time error