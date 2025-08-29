# Create All Without Using Any in-built Function
print()
# len : len(one)
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10,0]
for i,j in enumerate(a):
    i = i
print("Total Len of List : {}".format(i))

print()
# max : max(one)
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10,0]
b = a[0]
for i in a:
    if i > b:
        b = i
    else:
        b = b
print("Max Value Of List : {}".format(b))

print()
# min : min(one)
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10,0]
b = a[0]
for i in a:
    if i < b:
        b = i
    else:
        b = b 
print("Minimum Value Of List : {}".format(b))

print()
# any : any(one)
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10,0]
b = a[0]
for i in a:
    if i != 0:
        print("True : Starting Value Of True Statment : {}".format(i))
        break
else:
    print("False")

print()
# all : all(one)
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10, 0]
b = a[0]
for i in a:
    if i == 0:
        print("False")
        break
else:
    print("True")

print()
# sum : sum(one)
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10,0]
b = 0
for i in a:
    b += i
print("Sum Of List : {}".format(b))

print()
# sorted : sorted(one)
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10,0]

print()
# reversed : reversed(one)
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10,0]
print("Reversed Of List : {}".format(a[::-1]))
# without slicing function:
print()
b = []
for i in range(len(a) - 1,0,-1):
    b += ([a[i]])
print(b)


print()
# list : list(one)
# c = []
# for j in range(0,5):
#     a = int(input("Enter a Value of Integer :"))
#     c.append(a)
# print(c)

# ------------------------------------------------------------
print()
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10, 0]
# find the index of all 12 from the list
p = 0
for q in a:
    if q == 12:
        p += 1
    else: 
        p = p
print(p)

print()
# remove all 12 from the list 
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10, 0]
t = a + []
for s in t:
    if s == 12:
        a.remove(12)
print("Remove a Perticular Element From the list With All Repetation : {}".format(a))

print()
# remove only 3 - 12 from list 
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10, 0]
for s in a:
    if s == 12:
        a.remove(12)
print("Remove All - 1 Element From the List : {}".format(a))

print()
# count of removing elements from the list
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10, 0]
w = a + []
x = 0
for z in w:
    if z == 12:
        a.remove(12)
        x += 1
print("Element Remove From the List : {}".format(x))

print()
# Remove all negative number from the list
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10, 0]
e = a + []
for r in e:
    if r < 0:
        a.remove(r)
print("Removing All Negative Number From The List : {}".format(a))
print()
# add (2, 4, 6, 8, 10) on index 1,3,5,7,9
for h,i in enumerate(a):
    if i % 2 == 0:
        a.append(2)
print("a ; {}".format(a))
print()
# create new variable and point same value and add both list
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10, 0]
b = a
c = sum(a + b)
print(c)
#
a = [12, 35, 56, 90, 12, 12, 47, 12, -1, -10, 0]
b = a
o = []
for k in a:
    o += sum[a[k] + b[k]]
print(o)