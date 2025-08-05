# ----------------------------------------------------------
c = {'CS101':'OPP', 'CS102':'DS', 'CS201':'CPP'}
d = {'ME126':'HPE', 'ME102':'TOM', 'ME234':'AEM'}

# ----------------------------------------------------------
print(c.get('CS102'))   # 'DS'
print(c.get('CS302'))   # None
print(c.get('CS302', 'Absent'))     # if not exist, then print 'Absent'

# update
# ------------------------------------------------------------
c.update(d)
print(c)

# copy - creates a new object
# ------------------------------------------------------------
e = c.copy()
print(e)

# aliasing or shallow copy

f = c
print(f)

# removes the element from the dictionary - last item remove
# -------------------------------------------------------------
print(c.popitem())
print(c)

# reversing a dictionary
# ------------------------------------------------------------
dct_one = {1:10, 2:20, 3:30, 4:40, 5:50}

var1 = sorted(dct_one.items(), reverse=True)
print(dict(var1))

lst = list(dct_one.items())
a2 = tuple()
for a1 in range(len(lst) - 1, -1, -1):
    a2 += (lst[a1],)
print(dict(a2))

dct_two = {}
for count in range(0, len(dct_one)):
    item = dct_one.popitem()
    dct_two[item[0]] = item[1]      # adding value inside dict key:value -> key = 'value';
print(dct_two)

# remove the specified element from the dictionary
# --------------------------------------------------------
print(c.pop('CS102'))
print(c)
# print(c.pop())    # error

# clears all the elements of the dictionary
# -------------------------------------------------------
c.clear()
print(c)

# deletes the entire dictionary object
# -------------------------------------------------------
del(c)
# print(c)  # deleted dictionary 'c'

# example:
# remove the items wheres a ceratin value is occuring more than once
d = {'x':10, 'y':10, 'z':30, 'u':10, 'v':20, 'w':40}
print(d)
# e = d.copy()
a1 = list(d.items())
print(a1)
for a2 in range(len(a1)):
    for a3 in range(a2 + 1, len(a1)):
        if a1[a2][1] == a1[a3][1]:
            d.pop(a1[a3][0])
print(d)