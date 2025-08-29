# using built-in functions on list

lst1 = [10, 20, 30, 40, 50]
lst2 = [60, 0, 70, -80, 90]
lst3 = [0, 0, 0, 0, 0]

# length of list
print(len(lst1))
print(len(lst2))
print(len(lst3))

# maximum value of list
print(max(lst1))
print(max(lst2))
print(max(lst3))

# minimum value of list
print(min(lst1))
print(min(lst2))
print(min(lst3))

# sum of list (10, 20, -30, 40) = 10 + 20 + 40 - 30 = 40 ans
print(sum(lst1))
print(sum(lst2))
print(sum(lst3))

# any > returns 'true', if any one of the element is 'true' (Non-zero)
print(any(lst1))        # true : there many elements that are not 'zero'
print(any(lst2))        # true: there are many elements that are not 'zero', but one values is zero but not effect to all because we use (any) function 
print(any(lst3))        # false: 

# all > return 'True', if all the elements are 'true' (Non-zero)
print(all(lst1))        # true: because is not any value is zero
print(all(lst2))        # false: bacause one value is zero
print(all(lst3))        # false: all the elements are zero

# --------------------------------------------------------------
# example : find max without any function
lst = [10, 20, 80, 30, 40, 50]
c = 0
for i in range(0,len(lst)):
    if lst[i] > c:
        c = lst[i]
print(c)

lst1 = [10, 20, 30, 80, 50, 60]
d = 0
for i in lst1:
    if i > d:
        d = i
print(d)

# write in proper condition (sir)
lst1 = [10, 20, 30, 80, 50, 60]        # [10, 20, 30, 80, 50, 60]
d = 0 #d = lst1[0]                     # 0 
for i in lst1:                         # 10
    if i > d:                          # 10 > 0 = true
        d = i                          # d = true value
    else:
        d = d           # dont to any thing value will remain same
print(d)

# example : find min without any function
lst2 = [100, 20, -30, 80, 50, 60]
if lst:
    e = lst2[0]             # take first value from list with index value and check min of them
    for i in lst2:
        if i < e:
            e = i
        else:
            e = e
else: 
    print("Empty List")

# 'any' : without using any function
lst5 = []
if lst5:
    e = lst5[0]
    for j in lst5:
        if j != 0:
            e = j
    print(bool([e]))
else:
    print("Empty List")

# 'all' : without using any function
lst6 = [10, 20, 30, 40, 50]
for ind, num in enumerate(lst6):
    if not num:
        print("Break at Positon : {}".format(ind))
        break
else:
    print("All The Elements are Non-zero")

# ctrl + shift + p
# >codesnap
