# tuple variations
# ------------------------------------

print()
# -----------------------------------
a = (1, 3, 5, 9)
b = (2, 4, 6, 8, 10)
c = (a, b)
print(c[0][0], c[1][2])

print()
# ------------------------------------
record = (
    ('abc', 24, 1.23), ('def', 25, 1.24),
    ('ghi', 26, 1.25), ('jkl', 27, 1.26)
)

# 120, 140, 160, 180 change 1 element inside list

print(record[1][2])     # 1.24


print()
# -------------------------------------
for ele in record:
    print(ele)

# -------------------------------------
for ele in record:
    print(*ele)         # unpack

print()
# -------------------------------------
# records also have three element = (a, b, c) = ele
# like above case 
# a, i, f = by default it inside tuple only ()
for a, b, c in record:
    print(a,b,c)        # print(a,c) = 0 and 2 element of tuple inside tuple element

print()
# --------------------------------------
x = (1, 2, 3, 4)
y = (10, 20, x, 30)
print(y)


print()
# --------------------------------------
# unpack ( x ) 
x = (1, 2, 3, 4)
y = (10, 20, *x, 30)
print(y)

print()
# --------------------------------------
# 24 = not change because 24 is inside tuple and tuple is immutable 
# ('abc', 24, 1.24) = this all will change because 
lst = [('abc', 24, 1.24),('def', 25, 1.24)]
tpl = (['abc', 24, 1.24],['def', 25, 1.24])

# import random
# lst = []
# for i in range(10):
#     lst += [random.randint(1,10)]
# print(list(set(lst)))


import random 
c = []
f = 100
for i in range(f):
    h = random.randint(1, 10)
    if h not in c:
        c.append(h)
    if len(c) == 10:
        f = 0
print(c)

# wright way
import random 
lst = []
while len(lst) < 10:
    x = random.randint(1, 10)
    if x in lst:
        continue
    else:
        lst += [x]          # lst.append not creating new object. creating object destroy object every time but append imuatating lst and inserting value inside that
print(lst)
