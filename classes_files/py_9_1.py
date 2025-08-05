# What are sets ?
# --------------------------------------------------------

print()
a = {}
print(type(a))  # class dict by default

print()
a = set()       # empty set
print(type(a))  # class set

print()
b = {20}        # set with one element
print(b)

print()
c = {'Python', 25, 454.65}  # set with multiple items containing different data types
print(c)

print()
d = {10, 20, 30, 40, 50}    # set containing multiple items with similar datatype 
print(d)

print()
e = {10, 10, 10, 10, 10}    # set with duplicate items
print(e)                    # duplicate items are element with sets

print()
# -------------------------------------------------------------------------------------
s = {12, 23, 45, 16, 52}        # insertion order
t = {16, 52, 12, 23, 45}        # insertion order
u = {52, 12, 16, 45, 23}        # insertion order

# all output will same because, input element of s,t,u is same but placed in different order
print(s) # accessing order is the output ofthe set, and it is dependent on the hash value of the system
print(t)
print(u)

print()
# --------------------------------------------------------------------------------------
# a set can only contain immutable items
s1 = {'morning', 'evening'}
s2 = {(12, 13), (15, 25), (17, 34)}
print(s1)
print(s2)

# a set will not take mutable items 
# since the elements inside set should contain a fix hash value 
# a list being mutable, there is always a possibility that the element inside list might change
# s3 = {[12, 13], [15, 23], [17, 34]}
# print(s3)     # error

# note:
# ----------------------------------------------------------------------------------------
# since, set are unordered collections
# sets cannot be accessed or sliced using indexing
# sets cannot be mutated using indexing or slicing
# sets can be mutated using method

