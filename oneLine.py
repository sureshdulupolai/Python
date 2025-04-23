a = [
    x for x in range(0, 10)
]

print(a)

b = [
    a1 for a1 in range(0, -10, -1)
]
print(b)

c = ['animal', 'bird', 'human']

d = [
    a4 for a3,a4 in enumerate(c)
]

print(d)

# ----------------------------------------------
a = 10
b = 15

print(a) if a>b else print(b)

# -----------------------------------------------
# list inside if condition
lst1 = [
    x for x in range(0, 21) if x%2 == 0
]

print(lst1)

# -----------------------------------------------
# even, odd no in list
even, odd = [y for y in range(0, 21) if y%2 == 0], [s for s in range(0, 21) if s%2 == 1]
print(even, ' ', odd)

# ------------------------------------------------

lst2 = [
    a1 for a1 in range(0, 21) if a1%2 == 0
]

print(lst2)