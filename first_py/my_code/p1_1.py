# print all the elements of list 
fruits = ['apple','banana','cherry']
for i in fruits:
    print(i)

print()
for i in range(len(fruits) - 1, -1, -1):
    print(fruits[i])

print()
for i in range(0, len(fruits)):
    if i % 2 == 0:
        print(fruits[i])

print()
for i in range(0, len(fruits)):
    if i % 2 != 0:
        print(fruits[i])

print()
for i in fruits:
    print(i, end=' ')

print()
lst = []
print(lst)
for i in fruits:
    lst += [i]
print(lst)

print()
lst = []
for i in fruits:
    if i != 'banana':
        lst += [i]
print(lst)

print()
# use a for loop to print the number from 1 to 10.
for i in range(1, 11):
    print(i)

print()
for i in range(1,11):
    print(i,end=' ')

print()
# iterate through a list of numbers and print the square of each numbers 
number = [1, 2, 3, 4, 5]
s = []
for i in number:
    s += [i*i]
print(s)

print()
number = [1, 2, 3, 4, 5]
for i in range(len(number)):
    number[i] = number[i] * number[i]
print(number)

print()
# print all the even from the list 
numbers = [10, 15, 20, 25, 30]
for i in numbers:
    if i % 2 == 0:
        print(i)
    
print()
# print all the odd number from list 
numbers = [10, 15, 20, 25, 30]
for i in numbers:
    if i % 2 != 0:
        print(i)

print()
# count how many numbers in a list are greater than 5:
numbers = [1, 7, 3, 10, 5]
s = 0
for i in number:
    if i > 5:
        s += 1
        print(i,end=" ")
print()
print(s)

print()
# create a new list with each element double:
numbers = [1, 2, 3, 4]
lst1 = []
for i in range(0,2):
    lst = []
    for j in number:
        lst += [j]
    lst1 += lst
# print(lst1)
# Sorting them 
for i in range(0, len(lst1)):
    for j in range(0, len(lst1)):
        if lst1[i] < lst1[j]:
            lst1[i], lst1[j] = lst1[j], lst1[i]
print(lst1)

print()
# reverse the elements of a list using a for list:
lst2 = [10, 20, 30, 40]
lst3 = []
for i in range((len(lst2) - 1), -1, -1):
    lst3 += [lst2[i]]
print(lst3)

print()
for i in range(0, len(lst2)):
    for j in range(0, len(lst2)):
        if lst2[i] > lst2[j]:
            lst2[i], lst2[j] = lst2[j], lst2[i]
print(lst2)

print() # time take more to solve
# concatenate all the string in a list into a single string:
words = ['hello', 'world']
q = ''
for i in words:
    q += i
print(q)

print()
# add 5 to each element in list:
numbers1 = [5, 10, 15]
for i in range(len(numbers1)):
    numbers1[i] = numbers1[i] + 5
print(numbers1)

print()
# filter out number less then 10
numbers3 = [5, 10, 15, 2]
s = 0
for i in numbers3:
    if i < 10:
        s += 1
        print(i, end=' ')
print()
print(s)

print()
# print each character of every word in a list :
words1 = ['cat', 'dog']
for i in words1:
    for j in i:
        print(j)
    print()

print()
# generate a list of all possible pairs from two lists:
lst1 = [1,2]
lst2 = ['a', 'b']
s = []
for i in range(0,len(lst1)):
    s += [[lst1[i], lst2[i]]]
print(s)

print()
# print a multiplication table (1 to 3) using nested loops 
for i in range(1, 4):
    for j in range(1, 11):
        print('{} x {} = {}'.format(i, j, i*j))
    print()

print()
# ----------------------------------------------------
# count how many times each elements appears in a list:
numbers4 = [1,2,2,3,3,3]
s = 0
for i in numbers4:
    print(i)

print()
# flatten a list of lists:
nested = [[1,2],[3,4],[5]]
s = []
for i in nested:
    for j in i:
        s += [j]
print(s)

print()
# find the maximum number in a list without using max():
numbers5 = [1,2,3,8,5,7]
s = numbers5[0]
for i in numbers5:
    if i > s:
        s = i
    else:
        s = s
print(s)

print()
# find the sum of all numbers in a list using a for loop
numbers5 = [1,2,3,8,5,7]
for i in numbers5:
    s += i
print(s)

print()
# check if a list contains a specific value using a for loop
numbers6 = [1,2,3,8,5,7,'-']
s = ''
for j in numbers6:
    s = str(j)
    for i in s:
        if i in '!@#$%^&*()_+-/;:/?,.{[]}':
            print('list contain special character: {}'.format(i))

print()
# count how many vowels are in a string using for a loop
p1 = ['a', 'e','s',1]
s = 0
for i in p1:
    i1 = str(i)
    if i1 in 'aeiou':
        s += 1
print(s)

print()
# Remove duplication from a list using a list
lst4 = [1,1,2,2,3,3,3,4]
for i,j in enumerate(lst4[:]):
    if s != j:
        s = j
    else:
        lst4.remove(j)
print(lst4)

print()
# reverse a string using a for loop
string = 'python'
for i in range(len(string) - 1, -1, -1):
    print(string[i],end='')

print()
# convert a list of integer to string
numbers = [1,2,3]
s = []
for i in numbers:
    s += str(i)
print(s)

numbers = [1,2,3]
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])
print(numbers)

print()
# create a list of the first 10 squares using a for loop
lst = []
for i in range(1,11):
    lst += [i*i]
print(lst)

print()
# genrate the factorial of a number using a for loop
s = 5
t = 1
for i in range(s, 0,-1):
    t *= i
print(t)

print()
# print the fibonacci sequenence up to 10 times using a loop
# ------------------------------


print()
# print all prime number in a list 
numbers = [2, 3, 4, 5, 6, 7]
s = []
for i  in numbers:
    if i % 2 == 0:
        s += [i]
print(s)

print()
# create a list of odd number from 1 to 20 using a for loop
lst = []
for i in range(1,21):
    if i % 2 != 0:
        lst += [i]
print(lst)

print()
# filter out the string from a mixed list:
# ------------------------------------------
# itmes = [1,'hello',2,'world']
# for i in itmes:
#     if (i in str):
#         print(i)
#     else:
#         i += 1

print()
# count the number of words in a sentence
sentence = 'python is fun'
s = 0
for i in sentence:
    s += 1
print(s)
