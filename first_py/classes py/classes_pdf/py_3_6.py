# container types
# is also know as arrays

# list, tuple, set, dictionary

# an index position is the position at which the element is placed
# an elemnt is ( any data ) and ( any data type )

# list > mutable and ordered collection
list_1 = [10, 20, 30]
print(list_1[1])                        # accessing the list element
# mutable means changing values
# chaning value with index value list_1[1] = 20 to list_1[1] = 40
list_1[1] = 40
print(list_1[1])
print(list_1)
# list_1[1] = list_1[2]

# ----------------------------------------------------
# tuple > immutable and ordered collection
tpl_1 = (10, 20, 30, 40, 50)
print(tpl_1[3])
# cant change the value because it is immutable ( element in a tuple cannot changed )
tpl_1[3] = 400
# it will change because it create new value for tuple that element
tpl_1 = (100, 2000, 700)

# ---------------------------------------------
# set > mutable and unordered collection
# set > cannot contain similar values
# a set can be mutated using method of set
# a set cannot take repated values ( use full for cleaning data)
# set_2 = {10, 10, 10, 10, 10} # output = {10} 
set_1 = {10, 20, 30, 40, 50}
print(set_1)
# print(set_1[1])                   # we cant se a values with index because value in different pc with help of hardware of device
# set according to coumputer after seen the output
set_2 = {50, 20, 40, 10, 30}
print(set_2)

# -----------------------------------------------
# dictionary > mutable and unordered collection
# 'a' = key, 10 = value of that key
# keys and values can be of any basic data type
dict_1 = {'a' : 10, 'b' : 20, 'c' : 30}
print(dict_1['a'])               # accsing the values of the element using the key in a key-value pair .i.e. item

# changing value of "value"
dict_2 = {'a' : 1, 'b' : 2.54, 'c' : "python", 'd' : 3+2j, 'e' : true, 'f' : b'\x41'}
print(dict_2)

# changing value of "key"
dict_3 = {1 : 1, 2.54 : 2, "python" : 4, 3+2j : 56, true : "fg", b'\x41' : 67}
print(dict_3)

dict_4 = {1:[10, 20, 30], 2: (10, 20, 30), 3: {10, 20, 30}, 4: {'a': 10, 'b': 20, 'c': 30}, 5:[10, 20, 30]}
print(dict_4)

# 
var_1 = dict[1]
print(id(var_1))

var_2 = dict[5]
print(id(var_2))

# the address of a certain value in basic datatype is same for all the variable
# in the list datatype, since it is mutable, the address for some data created multiple times will be different
# because a list is created or have the possible of it's value being mutable

x = [10, 20, 30]
y = [10, 20, 30]
print(id(x))
print(id(y))

a = (10, 20, 30)
b = (10, 20, 30)
print(id(a))
print(id(b))

# --------------------------------------
# This is a UnMutable Class
# not error ( Tuple Formate )
# in tuple formate key will be fixed
dict_6 = {(10, 20) : 10}
print(dict_6)

dict_6 = {(10, 20) : 10}
print(dict_6)

# This All Are Mutable Class
# error ( List formate )
# because key is not fixed in dict because of that it doesn't work [10, 20]
dict_5 = {[10, 20] : 10}
print(dict_5)

# error ( Dict formate ) = {10 : 200}
# because key is not fixed in dict because of that it doesn't work [10, 20]
dict_7 = {{10: 200} : 10}
print(dict_7)

# error ( Set formate )
# because key is not fixed in dict because of that it doesn't work [10, 20]
dict_8 = {{10, 20} : 10}
print(dict_8)

# ---------------------------------------------------------------- 
# a fuction define inside a class is called as method
# creating new class is creating a user define datatype in pyhton
# all data type is a class

