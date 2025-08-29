# accessing the tuple elements 
# tuple is immutable 
# ------------------------------------------------

# same as list

tpl = (10, 20, 30, 40, 50)
print(tpl[2])
print(tpl[2:4])

# dont change value with indexing
# tpl[2] = 300 

# to chnage value 
print(list(tpl))

tpl = (10, 20, 30, 40, 50)
print(id(tpl))

tpl = tpl + (60,)
print(tpl)
print(id(tpl))

# tuple is immutable 
# tpl[2:4] = [200, 300]

# --------------------------------------------------------
msg = ('fail', 'in', 'love', 'with', 'python')
print(msg)              # tuple -> string

s = ([1, 2, 3, 4], [4, 5], 'python')
print(s)

# s[0] = [10, 20, 30, 40]
s[0][0] = 100
print(s)

t = s[1]
t[0] = 40
print(s)

# s[2] = 'python'
# s[2][1] = 'j'

# -------------------------------------------------------------
# try the following operations on tuple that were done on list
# concatenation 
# merging
# conversion
# aliasing or shallow copy
# cloning or deep copy
# searching 
# identity
# comparision
# emptiness

# concatenation 
tpl1 = (10, 20, 30, 40, 50)
tpl2 = tpl1 + (60, 70, 80)
print(tpl1)
print(id(tpl1))
print(id(tpl2))

# merging
tp1 = (100, 200, 300)
tpl2 = (101, 201, 301)
# not add something in tuple, nut this is pointing something
tpl3 = tpl1 + tpl2
print(tpl3)

# conversion
print(tuple())
t1 = (10, 20, 30)
t2 = tuple() + t1
# not create new object in tuple, but in list it create new object
print(id(t1))
print(id(t2))

t1 = (10, 20, 30)
t2 = tuple((10, 20)) + t1
print(id(t1))
print(id(t2))
print(tuple("10 20".split(' ')))
print(tuple('africa'))
print(tuple((10,20)))

# id will change in list
a = [10, 20, 30]        # 123
b = a + []              # b : #123456  = a : #123 + [] #456
print(id(list()))
print(id(list()))

# id will not change in tuple
a = (10, 20, 30)        # 123
b = a + ()              # b : #123  = a : #123 + () #456, because it by default when tuple is null then it take id of tuple carry one element 
print(id(tuple()))
print(id(tuple()))

#
print(type(tuple()))
print(type(()))

# () tuple with zero length
# (10,) tuple with one length
# ((), ) tuple with one length

# for tuple with one lenght or more it will create a new object while concatenating
# for tuple with zero length it will only 


lst1 = [101, 102, 103]      #123
lst2 = [201, 202, 203]      #456

# shallow copy - copy address of lst1 in lst3, but actually it is not copy any thing inside lst3 but pointing to address of lst1
lst3 = lst1                 #123

# deep copy
lst4 = lst1 + lst2          #112 = #123 + #456

# concatenation
lst5 = lst1 + [501, 502, 503]           #113 = #123 + #687

# lst = lst1 + [701, 702, 703] same as this
lst1 = lst1 + [601, 602, 603]
print(lst1)
# direction changing to pointing to a address
print(id(lst1))
print(lst3)
print(id(lst3))

# tuple : 
tpl1 = (301, 302, 303)      #789
tpl2 = (401, 402, 403)      #101

tpl3 = tpl1 + tpl2 
print(id(tpl1))
print(id(tpl2))
print(id(tpl3))

# 
tpl4 = tpl1 + (801, 802, 803)
print(id(tpl4))

# when you concatenate with an empty tuple 
# it doess not create a new object 
tpl5 = tpl1 + ()
print(tpl1)
print(tpl)
print(id(tpl1))
print(id(tpl5))

# concatenating a tuple with a tuple with single or more elements
# or with an empty tuple element will create a new object
tpl6 = tpl1 + ((), )
print(tpl1)
print(tpl6)
print(id(tpl1))
print(id(tpl6))

