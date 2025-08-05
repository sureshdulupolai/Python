try:
    import math
    Math.pow(5, 2)      # # Name error 

except (ZeroDivisionError, TypeError, ValueError):
    pass

except:
    print("This might be a NameError")


# NameError - Wrong Syntax / Undeclared Vairable
# TypeError - When a Variable is Not Defined
# ZeroDivisionError - When a Number is Divided By Zero
# ValueError - When Type Conversion is Not Possible