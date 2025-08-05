# basic set operations

s = {'gate', 'fate', 'rate'}
print(s)

s.add('late')
print(s)

s = frozenset({'gate', 'fate', 'rate'})
print(s) # any element dont get add by this method, value is fixed inside that

# s.add('late')

# concatenation - doesn't work
# merging - doesn't work
# conversion of data type - work
# aliasing or shallow copy - works
# cloning or deep copy - doesn't work
# searching - work
# identify - work

print()
# example 1 : shallow copy 
# ---------------------------------------------------------

s1 = {10, 20, 30}
s2 = s1
print(s1)
print(s2)

# identify 
# --------------------------------------------------------
print()

s1 = {10, 20, 30}
s2 = {40, 50, 60}
print(s1 is s2) # false


# searching 
# -----------------------------------------------------------
print()

print(40 in s2)

print()
# address : differnet in set, create new variable and hex value
# --------------------------------------------------------------
s3 = {10, 20, 30}
print(id(s1))
print(id(s3))

print()
# ---------------------------------------------------------------
print(s1 == s3) # true

print()
# comparison
# ---------------------------------------------------------------
# note: 
# true > if all the elements of s6 are contained in s5
# only then, s6 is considered to be a subset of s5
# and s5 is the superset of s6

s5 = {10, 30, 40, 50} # superset
s6 = {10, 20, 30} # subset
print(s5 > s6) # false

s5 = {10, 20, 30, 40, 50}
s6 = {10, 20, 30}
print(s5 > s6) # true


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

print()
# example 2 :
s = {12, 12, 14, (15, 16), (17, 18)}
# method 1:
a1 = tuple()
for i in s:
    if isinstance(i, tuple):
        a1 += (*i,)
    else:
        a1 += (i,)
print(a1)

# method 2:
a1 = tuple()
for i in s:
    if isinstance(i, tuple):
        for j in i:
            a1 += (j,)
    else:
        a1 += (i,)
print(a1)

# method 3 : set unpack inside set only
a1 = set()
for i in s:
    if isinstance(i, tuple):
        for j in i:
            a1.add(j)
    else:
        a1.add(i)
print(a1)

