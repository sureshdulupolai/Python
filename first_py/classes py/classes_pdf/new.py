# count = 5
# while count >= 0:
#     print(count)
#     count = count - 1

# lst = [52, 25, 35, 67, 80, 43, 78]
# a = 0
# b = 7
# while a < b:
#     print(lst[a])
#     a += 1  

# lst = [52, 25, 35, 67, 80, 43, 78]
# a = 0
# b = 7
# while a < b:
#     if a % 2 == 0:
#         print(lst[a])
#     a += 1 

# --------------------------------
lst = [52, 25, 35, 67, 80, 43, 78]
a = 0
b = 6
while b >= a:
    print(lst[b])
    b -= 2

count = len(lst) - 1
while a >= 0:
    if a % 2 ==0:
        print(lst[a])
    a -= 1

count = len(lst) - 1
while a >= 0:
    if a % 2 != 0:
        a -= 1
        continue
    print(lst[a])
    a -= 1
# ----------------------------------------

