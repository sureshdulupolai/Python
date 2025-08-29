# # decimal ascii value use:
# stg = 'pKthon'
# j = ''
# for i in stg:
#     x = ord(i)
#     if (x >= 97 or x <= 122):
#         j += (chr(ord(i) - 32))
#     # elif (x > 65 or x < 90):
#     else:
#         j += i
# print(j)

# stg = 'pKthon'
# j = ''
# for i in stg:
#     x = ord(i)
#     if (x >= 97 and x <= 122):
#         j += (chr(ord(i) - 32))
#     # elif (x > 65 or x < 90):
#     else:
#         j += i
# print(j)


# stg = 'WelComE ST+'
# c = stg[:]
# for i in stg:
#     x = ord(i)
#     if x > 65 and x < 90:
#         stg += chr(ord(i) + 32)
#     else:
#         stg += i
# stg = stg.split(c)
# print(stg[1])

# p = 7
# q = p - 2
# for i in range(0,p):
#     for j in range(0,p):
#         if i == 1:
#             if (j >= 1 and j <= q):
#                 print("* ",end="")
#             else:
#                 print("  ",end="")
#         if i == 2:
#             if (j == 1 or j == q):
#                 print("* ",end="")
#             else:
#                 print("  ",end="")
#         if i == 3:
#             if (j >= 1 and j <= q):
#                 print("* ",end="")
#             else:
#                 print("  ",end="")
#     print()

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]

j = 0
s = []
for p in range(3):
    n = []
    for i in range(3):
        n += [lst[j]]
        j += 1
    s += [n]
print(s)

# lst = [1,2,3,4,5]
# s = len(lst) - 1
# f = int((len(lst) / 2) + 0.5)
# for i in range(f):
#     lst[i], lst[s - i] = lst[s - i], lst[i]
# print(lst)

# sir wala 
# import math
# lst = [1,2,3,4,5]
# length_lst = len(lst)
# final_index = length_lst - 1
# range_index = math.ceil(length_lst / 2)
# for index in range(range_index):
#     lst[index], lst[final_index - index] = lst[final_index - index], lst[index]
# print(lst)