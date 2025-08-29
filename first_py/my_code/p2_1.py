print()
# find the smallest number in a list without using min() 
numbers = [4,1,7,3,2]
s = numbers[0]
for i in numbers:
    if i < s:
        s = i
    else:
        s = s
print(s)

print()
# print only the first letter of each word in a list 
words = ['apple', 'banana', 'cherry']
s = []
for i in words:
    j = i
    for q in range(0,1):
        s += [j[q]]
print(s)

print()
# print the index and value of each element in a list
numbers = [10, 20, 30]
for i,j in enumerate(numbers):
    print('index value :{} - Value :{}'.format(i,j))

print()
# create a new list containing only the last character of each string 
words = ['cat', 'dog', 'bird']
s = []
for i in words:
    j = i
    for t in range(0,1):
        s += [(j[len(words) - 1])]
print(s)

print()
# multiply each element in a list by its index
# -------------------------------------------
# numbers = [5,10,15,20]
# for l1,l2 in enumerate(numbers):
#     numbers[l1] = (numbers[l2] * numbers[l1])
# print(numbers)

print()
# sum all the number in a nested list
nested = [[1,2],[3,4],[5,6]]
s = []
for i in nested:
    for j in i:
        t += j
    s += [t]
print(s)

print()
# find the maximum number in each sub-list
# --------------------------------------- 
# nested = [[3, 5, 1], [9, 0], [7, 8]]
# for i in nested:
#     print(i)
#     for j in i:
#         t = i[0]
#         if t > i:
#             t = j
# print(t)
        
print()
# count how many sub-list have an odd number of element
