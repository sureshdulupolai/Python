# List Methods
# A Function Inside Class is Called as Methods
# every datatype is a class in python ( str, int, float, bool, byte, list, set, dic, tuple & etc)

# What is class in list ? 
# list is class in python because its is a datatype (Container datatype).

# orginal list 
lst = [12, 15, 13, 13, 23, 22, 16, 17]
print(lst)

# add new item at the end of the list only 
lst.append(22)
print(lst)

# delete item 13 from the list
lst.remove(13)
print(lst)

# reports error since 30 is not in the list
# lst.remove(30)
# print(lst)

# removes the last item from the list
lst.pop()
print(lst)

# removes the data positioned at index number 3
lst.pop(3)
print(lst)

# pop the number from list and insert in different variable 
d = lst.pop(3)
print(lst)
print(d)

# insert 21 at index position 3
lst.insert(3, 21)
print(lst)

# return the number of times 21 is present in the list
c = lst.count(13)
print(c)

# return the index position of 22
# print(lst.index(22))

# ------------------------------------------------------
# not learn 
# my_list = [1, 2, 3]
# my_list.extend([4, 5])
# print(my_list)  # Output: [1, 2, 3, 4, 5]
# ------------------------------------------------------

# --------------------------------------------
# example :-

# code - 1
lst1 = [10, 20, 30, 30, 40, 50, 30, 60]
for i in range(lst1.count(30)):
    lst1.remove(30)
print(lst1)

# code - 1
# Creating deep copy, runing deep copy and removing from orginal list (Deep Copy Create for Index Positon changing When One element is removing) 
lst1 = [10, 20, 30, 30, 40, 50, 30, 60]
lst1 = lst + []
for num in lst1:
    if num == 30:
        lst.remove(30)
print(lst)

# code - 1
lst1 = [10, 20, 30, 30, 40, 50, 30, 60]
lst2 = []
for i in lst:
    if i != 30:
        lst2.append(i)
print(lst2)

# code - 2
lst_one = [10, 20, 30]
lst_two = [40, 50, 60]
# output
# lst_three = [50, 70, 90]

# answer :- effecient
lst_three = []
for i in range(0, len(lst_one)):
    lst_three.append(lst_one[i] + lst_two[i])
print(lst_three)

# code - 3
lst_one = [10, 20, 30]
lst_two = [40, 50, 60]
lst_three = []
for i in range(0, len(lst_one)):
    lst_three += [lst_one[i] + lst_two[i]]
print(lst_three)