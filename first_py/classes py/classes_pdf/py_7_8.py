# List Varieties 
print()
# nested list -> creating new variable and getting answer
a = [1,3,5,9]
b = [2,4,6,8,10]
c = [a, b]      # list inside list c = [[a],[b]]
print(c)
print(c[0])
# printing 5: taken from list a
print(c[0][2], end='')
print(c[1][2])
# inside new list
s = [c[0][2],c[1][2]]
print(s)

print()
# embedded list - list inside list -> list inside list variable
x = [1,2,3,4]
y = [10, 20, x, 30]
print(y)
print(y[2][2])

print()
# unpacking using the ( * ) operator
s = 'hello'
# packed form - not open
l1 = [s]
print(l1)

x = [1,2,3,4]
y = [10, 20, x, 30]
print(y)

# unpacked form - open
l2 = [*s]
print(l2)

x = [1,2,3,4]
y = [10, 20, *x, 30]
print(y)


# example:-
# -----------------------------------------------------------
# excess '3' from the list
c = [[0,1,[2,3],4],5,[6.7]]
print(c[0][2][1])

# output: lst1 = [1,2,3,4,5,6]
# -------------------------------------------------------------
# 1 
lst = [[1,2,3],[4,5,6]]
lst1 = []
for i in lst:
    lst1 += i
print(lst1)

# 2 
lst = [[1,2,3],[4,5,6]]
lst1 = []
for i in lst:
    for j in i:
        lst1 += [j]
print(lst1)

# 3
lst = [[1,2,3],[4,5,6]]
lst1 = []
for i in lst:
    lst1 += [*i]
print(lst1)

# 4
lst = [[1,2,3],[4,5,6]]
lst1 = []
for i in range(0, 2):
    lst1 += lst[i]
print(lst1)

# mehtod 2 & 3:
print(lst[0] + lst[1])
print([*lst[0], *lst[1]])
# ----------------------------------------------------

# perform the following operations on the list of names
#  -------------------------------------------
# create a list of name: anil,  amol, aditya, avi, alka
# insert a name anuj before aditya
# append a name: zulu
# delete avi from the list
# replace anil with anilkumar
# sort all the names in the list
# print reversed sorted list

# 1 - create a list -> anuj before aditya
a = ['anil', 'anmol', 'aditya', 'avi', 'alka']
a.insert(2, 'anuj')
print(a)

# 2 - append zulu
a.append('zulu')
print(a)

# 3 - delete avi
a.remove('avi')
print(a)

# 4 - replace anil to anilkumar
a[0] = 'anilkumar'
print(a)

# 5 - sort all the names in list
a.sort()
print(a)

# 6 - reversed sorted list
a.sort(reverse=True)
print(a)
# or 
x = sorted(a, reverse=True)
print(x)
# ----------------------------------------------------