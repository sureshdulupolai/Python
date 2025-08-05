# set method 

s = {12, 15, 13, 23, 22, 16, 17}
t = {'A', 'B', 'C'}
u = set()

print(s)
print(t)
print(u)

print()
# --------------------------
# adding an element to the given set
s.add('hello')
print(s)

# merging - adding the element of one set to another set
s.update(t)
print(s, 'debug 1')

# cloning or deep copy
u = s.copy()
print(u)

print()
# removing an element from the given set
s.remove(15)
print(s)
print(u) # not change because, hex is different create new variable with same data

# tryping to remove on element which is not present in the set will give an error, while using remove
# s.remove(101)
# print(s)

# tryping to remove on element which is not present in the set will 'not' give an error, while using discard
s.discard(101)
print(s)

# removes any random element from the set
s.pop()
print(s)

# clears all the elements of the set
s.clear()
print(s)