nested = [[1,2],[3,4],[5,6]]
e = []
for i in nested:
    t = 0
    for j in i:
        t += j
    e += [[t]]
print(e)    

print()
nested = [[3, 5, 1], [9, 0], [7, 8]]
a = []
for i,p in enumerate(nested):
    s = []
    t = p[0]
    for j in p:
        if j > t:
            t = j
            s += [t]
    a += [s]
print(a)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
t = []
for i in range(len(matrix)):
    s = []
    for j in range(len(matrix)):
        if i == j:
            s += [matrix[i][j]]
    t += [s]
print(t)

matrix = [[1,2],[3,4]]
t = []
for i in matrix:
    for j in i:
        t += [j]
print(t)

number = [1,2,3,4,5,6]
s = []
for i in number:
    if i % 2 != 0:
        s += [i]
print(s)

number = [-1, 2, -3, 4]
s = []
for i in number:
    if i < 0:
        i = 0
    s += [i]
print(s)

words = ['apple', 'banana', 'apple', 'cherry']
s = []
for i,d in enumerate(words):
    a = 0
    for j,e in enumerate(words):
        if d == e:
            a += 1
    s += [a]
t = []
for i in range(len(words)):
    t += [words[i], s[i]]
print(t)


number = [1,2,2,3,3,4]
s = []
for i in number:
    if i not in s:
        s += [i]
print(s)

number = [1,3,5,3,7,3]
s = []
for i,j in enumerate(number):
    if j not in s: 
        s += [i]
print(s)

version = 'hello world'
t = ''
for i in version:
    if i in 'aeiou':
        s = i.upper()
    else:
        s = i
    t += s
print(t)

words = ['dog','cat']
t = ''
for i in words:
    t += i
print(t)

number = [1,2,3,4]
s = []
for i in number:
    s += [i * i]
print(s)

# number = [1,2,2,3,3,4]
# for i,j in enumerate(number[:]):
#     if i == number[j]:
#         number.pop() 
# print(number)

words = 'hello'
s = []
for i in words:
    s += [ord(i)]
print(s)

s = []
for i in range(1, 50):
    if i % 2 == 0:
        s += [i]
print(s)

letter = 'this is a simple python exercise'.split(' ')
s = 0
for i in letter:
    if len(i) > 3:
        s += 1
print(s)

lst1 = [1,2,3]
lst2 = [3,4,5]
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i] == lst2[j]:
            print(lst1[i])

# print()
# words = ['madam', 'cat', 'level', 'dog']
# for i in words:
#     p = len(i)
#     for j in range(p, -1, -1):
#         print(words[i][j])

lst1 = [1,2,3]
lst2 = [4,5,6]
s = []
for i in range(0,1):
    for j in range(len(lst2)):
        s += [lst1[j],lst2[j]]
print(s)