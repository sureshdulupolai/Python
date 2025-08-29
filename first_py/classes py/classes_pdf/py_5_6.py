# # use 'else' in default condition
x = int(input("Enter the value of x : "))
if x == 30:
    print("x is 30")

else:
    print("x is not 30")

# ---------------------------
x = int(input("enter value for x : "))
y = int(input("enter value for y : "))

if x == 30:
    if y == 40:
        print("A")
    else:
        print("B")

else:
    if y == 50:
        print("c")
    else:
        print("D")

# 
g = input("enter you are m aur f : ").strip().upper()
a = int(input("enter your age : "))
m = input("enter the marital status of the person as 'Married' or 'Unmarried': ").strip().capitalize()

if g == "M":
    if (a > 0 and a < 21):
        if m == 'Married':
           print("Tax is 8%")
        
        if m == 'Unmarried':
           print("Tax is 10%")
        
        else:
            print('Invalid Marital Status entered')
   
    elif a >= 21:
        if m == 'Married':
           print("Tax is 10%")
        
        if m == 'Unmarried':
           print("Tax is 12%")
        
        else:
            print('Invalid Marital Status entered')
    
    else:
        print('Invalid Negative Age')

if g == "F":
    if (a > 0 and a < 21):
        if m == 'Married':
           print("Tax is 6%")
        
        if m == 'Unmarried':
           print("Tax is 8%")
        
        else:
            print('Invalid Marital Status entered')
   
    elif a >= 21:
        if m == 'Married':
           print("Tax is 9%")
        
        if m == 'Unmarried':
           print("Tax is 11%")
        
        else:
            print('Invalid Marital Status entered')
    
    else:
        print('Invalid Negative Age')
else:
    print("The Possible Value Are 'M' and 'F'")

