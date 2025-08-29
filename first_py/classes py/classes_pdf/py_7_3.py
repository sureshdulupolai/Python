# list concatenation 
lst = [12, 15, 13, 23, 22, 16, 17]
print(lst)
print(id(lst))
# adding two list with 'unique' memory addresses will create a new list object
lst = lst + [3, 44, 55]

# adding two list with 'Same' memory addresses will keep the same list object addresses
# only the elements will be added in the given list object address
lst1 = lst + lst
print(lst1)
print(id(lst1))

# the address of the third list object is different from first two list object
# this will create a new list object
lst2 = lst + lst + []
print(lst2)
print(id(lst2)) 

# list merging 
# creating variable name and add them
s = [10, 20, 30]
t = [100, 200, 300]
z = s + t
print(z)

# converting to list using typecasting
# typecasting > changing from one data type to another datatype

# Sting to list
u = list('Africa')
print(u)

# tuple to list
v = list((10,20,30))
print(v)

# set to list
w = list({10, 20, 30})
print(w)

# dic to list
# print only key because by default it value is "keys()"
x = list({10:40, 20:50, 30:60 })
print(x)

x = list({10:40, 20:50, 30:60 }.values())
print(x)

x = list({10:40, 20:50, 30:60 }.items())
print(x)

# list to list
m = list([10,40,100])
print(m)

# aliasing or shallow copy
lst1 = [10, 20, 30, 40, 50]
lst1 = lst2
# both will be same bacause both are pointing to same address
print(id(lst1))
print(id(lst2))

# here a cpmplete new object for [10, 20, 30, 40, 50] is created 
# and same value assigned to lst3
lst3 = [10, 20, 30, 40, 50]
# not have same address while both are pointing to same address 
# in this case new object will get created
# but in above case there not creating a new object, it directly pointing to same address
print(id(lst3))

# note that, the address pointed by  lst1 and lst2 
# is different from the address pointed by lst3 
# even when the data contained in all  three is the same 
# not a like basic datatype, wherein a = 3 and b = 3 would point toward some address

# same changes in both because pointing to same address
lst2[2] = 200
print(lst1)
print(lst2)
# 
lst1[1] = 20
print(lst1)
print(lst2)

# change in 'third list' only beacuse the point different both valuse are same
lst3[1] = 2000
print(lst3)

# cloning or deep copy
# creating a variable, the value cant change when first value will change
# a = [10,20] 
# b = a
# b[1] = 20
# will not done in this because it carry deep copy 
lst4 = lst1 + []
print(id(lst1))
print(id(lst4))

x = []
y = []
z = x
w = x + []
# in id pointing of x and y
print(id(x))
print(id(y))
# x and y will be same
print(id(z))
# different from x,y,z for w
print(id(w))

stg = "Africa"
#print(list(stg))
b = []
for i in stg:
    b += i
print(b)

# ['A']
# ['A','f']
# ['A','f','r']
# ['A','f','r','i']
# ['A','f','r','i','c']
# ['A','f','r','i','c','a']
stg = "Africa"
b = []
for i in stg:
    b += i
    print(b)

# searching (in)
lst = ['a', 'e', 'i', 'o', 'u']
print('a' in lst)       # true
print('z' in lst)       # false 
print('z' not in lst)   # true

# identity: (is)
print(lst1 is lst2)
print(lst1 is lst3)
print(lst1 is lst4)

num1 = 10
num2 = 20
# both are pointing to same address 
# because it is basic datatype 
print(num1 is num2) # true 

s1 = 'Hi'
s2 = 'Hi'
print(s1 is s2) 

# comparison 
a = [1, 2, 4, 4]
b = [1, 2, 5]
print(a < b)    # true: check one by one inside element

a = [1, 2, 5, 4]
b = [1, 2, 5]
print(a < b)    # false: check one by one inside element and 4 extra inside a

stg = 'africa'
for i in stg:
    print((chr(65) + i),[i])

# emptiness 

lst = [1, 2, 3]   # true: list, because there element inside of list
# it will be false when the empty datatype it there ( 0, false, [], (), {}) all this are empty
if lst:
    print('Full List')          # if true then only print this otherwise dont print some thing 

lst = []
if not lst:
    print('Empty List')     # if it is false then it will be convert into true and then print it. in case of empty list otherwise dont print something

# Note:-
# The following values are considered to be false 
# None 
# Number equivalent to zero: 0, 0.0, 0+0j, 0j
# Empty string, list, and tuple: "", [], ()
# Empty Set and Dictionary: {}

# check bool values 
print(bool([]))         # empty list boolean value 
print(bool([0]))        # list with some element boolean value 
print(bool(0))          # bool value of zero