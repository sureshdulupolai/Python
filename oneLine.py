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