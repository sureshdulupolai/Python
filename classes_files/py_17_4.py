try:
    var = int('abc')
    print(var)

except ValueError:
    print("This is a valueError!")

except:
    print("OtherException!")