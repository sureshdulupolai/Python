# identity > is
c = 5 
d = 5
print(c is d)

e = 7
print(d is e)

# both 'x' and 'y' will containing different address
# as list will create new objects
x = [10, 20, 30]
y = [10, 20, 30]
print(x is y)

# here 'z' is pointing toward 'x' and 'x' is pointing to the address of the data [10, 20, 30]
# as list 'z' is not a new object but referencing to 'x'
z = x
print(x is z)

f = float(input("enter value for c:"))
c = (f - 32) * 0.55
print("this is your f: value ",f)
print("this is your c: value ",c)

i = 5/9
print(float(i))

# gross salary will be entered by the user
# hra which is 23% of the gross salary has to be calculated 
# tds which is 1% of the gross salary has to be calculated 
# pf which is 5% of the gross salary has to be calculated 
# basic salary deducting hra, tds, and pf has to calculated form the gross salary 

# step 1: me
gross_salary = float(input("Enter Your salary : "))
c = gross_salary * 0.23
print("HRa: {}".format(c))
d = gross_salary * 0.05
print("Pf: {}" .format(d))
e = gross_salary * 0.01
print("tds : {}".format(e))
f = c + d + e
g = gross_salary - f
print("this is total : {}".format(g))

# step: sir
gs = float(input("Enter The Gross salary : "))
hra = gs * (23/100)
tds = gs * (1/100)
pf = gs * (5/100)
bs = (gs - hra - tds - pf)
print("The Gross salary is : {}".format(gs))
print("The hra : {}".format(hra))
print("The tds : {}".format(tds))
print("The pf : {}".format(pf))
print("The basic salary after all deduction is : {}".format(bs))

# step 3: all input from users
gs = float(input("Enter The Gross salary : "))
hra = gs * (float(input("entre percentage of hra"))/100)
tds = gs * (float(input("entre percentage of tds"))/100)
pf = gs * (float(input("entre percentage of pf"))/100)
bs = (gs - hra - tds - pf)
print("The Gross salary is : {}".format(gs))
print("The hra : {}".format(hra))
print("The tds : {}".format(tds))
print("The pf : {}".format(pf))
print("The basic salary after all deduction is : {}".format(bs))

# calculate the area, parameter and volume of a rectangle 
l = float(int("value of length : "))
b = float(int("value of breath : "))
h = float(int("value of height : "))
print("the area of rectangle is : ",l*b)
print("the parameter of rectangle is : ",2(l+b))
print("the volume of rectangle is : ",l*b*h)