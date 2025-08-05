# updating set operations - change in same set only

a = {1, 2, 3, 4, 5}
b = {2, 4, 5}
print(a, 'debug a old')
print(b)

print()
# update a set is (immutable)
a = a | b
print(a, 'debug a new')
print(b)

print()
# --------------------
a = a & b
print(a)
print(b)

print()
# ------------------
a = a - b
print(a)
print(b)

print()
# --------------
a = a ^ b
print(a)
print(b)

print()
# set to list
set_one = {1, 2, 3}
lst_one = [*set_one]
print(lst_one)