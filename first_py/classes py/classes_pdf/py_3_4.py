# inbuild fuctions
# -----------------------------------------------------------------
# modules ( % )
# negtive sign ko positive kar dena
print(abs(-3))
print(abs(-3.3))
# raise to fuction ( 5 ** 2)
print(pow(5, 2))
# minumum no
print(min(6, 7, 8, 10, 1))
# maximum no 
print(max(10, 5, 6, 22, 1))
# same as division but it gives values = quoteint and reminder 
print(divmod(5, 2))
# ssame as sql decimal(10, 2) 
# round the value wich u written after ( , )
print(round(2.36475897967, 3))
# to find binary value 
print(bin(65))
# to find octa value 
print(oct(65))
# to hexadecimal value
print(hex(65))

print()

# example 
# ---------------------------------------------------------------------------------
# value puting inside a variable
a = pow(5, 2)
b = min(5, 2, 10, 6, 1)
c = 10; d = 20
print(min(c, d))

# -----------------------------------------------------------------------------------
# array is notjing but the collection of elements
# array can go inside in other array and then then inside array also a array element
# array can store data (int, float, string, complex, bytes)

# different types of array
# list
# tuple
# set
# dictionary

# --------------------------------------------------
# value inside one elemnt in array form
e = divmod(5, 1)
print(e)

# indexing 
one = e[0]
print(one)

two = e[1]
print(two)

# -------------------------------------------------------
# multiple argument inside a function
# first input will run after that it calculate max or min function or which function you have.
three = print(max(5, 6, 2, 7+2*3, int(input("Enter a number : "))))
print(three)

print(min(5, 5, 8, 10, 2 + int(input("Enter a value : "))))

# ---------------------------------------
# multiple function inside a function
print(round(pow(20.457546, 2), 3))

# second methon using variable
g = pow(20.32546, 2)
f = round(g, 3)

# -------------------------------------------------
# take input and change data type in assci value 
# and then calculate with 'a' = hexadecimal value
i = min(1, 5, ord('a'), 9)
print(i)

j = max(1, 5, ord('a'), 9)
print(j)



