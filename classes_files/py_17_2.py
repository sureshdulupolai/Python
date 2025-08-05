# NameError

# example 1
# --------------------------------------------------------------------------
try:
    a = 5
    b = 7
    # "d" is not define then error will show but to handle it use except
    c = a + b + d

except NameError:
    print("You Have Encountered a NameError!!!")


# example 2
# -------------------------------------------------------------------------
# give error in output, because it "except" is loking only for zerodivision error
# and variable is not declare error will execute
try:
    a = 5
    b = 7
    # "d" is not define then error will show but to handle it use except
    c = a + b + d

except ZeroDivisionError:
    print("You Have Encountered a NameError!!!")


# example 3
# --------------------------------------------------------------------------
try:
    a = 5
    b = 7
    # "d" is not define then error will show but to handle it use except
    c = a + b + d

except NameError:
    print("You Have Encountered a NameError!!!")

except ZeroDivisionError:
    print('You Have encountered a ZeroDivisionError!')


# example 4
# --------------------------------------------------------------------------
try:
    a = 5
    b = 7
    # "d" is not define then error will show but to handle it use except
    c = d + a / b

except NameError:
    print("You Have Encountered a NameError!!!")

except ZeroDivisionError:
    print('You Have encountered a ZeroDivisionError!')


# example 5
# in this case, both except is "True", but only run one except at one time
# --------------------------------------------------------------------------
try:
    a = 5
    b = 0       # zerodivision error
    # "d" is not define then error will show but to handle it use except
    c = a / b + d

except NameError:
    print("You Have Encountered a NameError!!!")

except ZeroDivisionError:
    print('You Have encountered a ZeroDivisionError!')