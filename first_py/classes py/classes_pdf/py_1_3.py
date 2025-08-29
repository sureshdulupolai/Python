# type casting 
# changing a datatype to other datatype ( int to char ), ( char to int )

# int
print(int(10.5))            # float to int
print(int("1"))             # str to int | float str cant change in integer formate
print(int(True))            # bool to int
print(int(False))           # bool to int
print(int(b'\x32'))         # (bytes (hex 30 to hex 39) to int ) only ( other number cant create it to int formate because there hex no convert into char formate ) = (b'\x41') = convert("A") it's not a integer

# float
print(float(10))            # int > float
print(float("10.5"))        # str > float
print(float('1'))           # str > float
print(float(b'\x31'))       # bytes > float
print(float(True))          # bool > float
print(float(False))         # bool > float

# string
print(str(1))               # int > str
print(str(1.5))             # float > str
print(str(3+2j))            # complex > str
print(str(b'\x31'))         # bytes > str
print(str(True))            # bool > str
print(str(False))           # bool > str
print("suresh")             # str > str

# boolean
# 0 = false, null = false , complex = 0+0j = 0 + 0 = false
# all other are ture ( int, str, float etc)
print(bool(1))
print(bool(100))
print(bool(-100))
print(bool(0))
print(bool(''))
print(bool(' '))
print(bool('Python'))
print(bool(None))
print(bool(3+2j))
print(bool(0+0j))
print(bool(0+2j))
print(bool(5+0j))
print(bool(-3.456))
print(bool(b'\x30'))
print(bool(int(b'\x30')))

# complex
print(complex(3))
print(complex(3, 2))
print(complex(True, False))
print(complex(int(b'\x30')))
print(complex(int(b'\x30'), int(b'\x31')))


# to identify the data tpye 
print(type(10))

# Formate String
a = 5
b = 6
c = 10
print("The Value Of a {}, b is {} and c is {} ".format(a,b,c))
# a,b,c is in tuple formate 
# we can change value acording to there index value 
# a,b,c = 0,1,2
print("The Value Of a {2}, b is {0} and c is {1} ".format(a,b,c))

# Print Function
# by default value between 2 number is space (1 2 3)
print(1,2,3)
# changing value between 2 number (1.2.3)
print(1,2,3, sep='*')
# by default it's it comes in new line with (end='\n') new line
print(1,2,3)
# same line print the next line
print(1,2,3, end=' ')

#Input Function
c = input("Ente The of c: ")
# int Str > int convert
d = int(c)
e = d + 5
print(e)

f = int(input("Enter the value of f: "))
g = f + 5
print(g)

h = int(True + True) # = 1 + 1 = 2
print(h)
i = True + False = 1 + 0 = 1
j = False + False = 0 + 0 = 0

