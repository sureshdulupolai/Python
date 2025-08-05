# #         1
# #       2   2
# #     3       3
# #   4           4
# # 5               5

# # for i in range(1, 6):
# #     for j in range(1, 6-i):
# #         print('- ', end='')
# #     print('{} '.format(i),end='')
# #     for p in range(i):
# #         for q in range(p):
# #             print('- ',end='')
# #     if i >= 2:
# #         print('{}'.format(i),end='')
# #     print()


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lst1 = [[3, 5, 7], [2, 4, 9], [1, 6, 8]]

t1 = []
for g1 in range(1):
    b = 1
    s = []
    for a1 in range(0,len(lst)):
        t = []
        for a2 in range((len(lst) - a1 - 1) ,-1,-1):
            t = lst[a1][a2]
            break
        s += [t]
    b = 2
    b3 = []
    for b1 in range(len(lst)):
        b4 = []
        for b2 in range((len(lst) - b1 - b), -2, -1):
            b4 = lst[b1][b2]
            break
        b3 += [b4]
    b = 3
    c1 = []
    for c2 in range(len(lst)):
        c3 = []
        for c4 in range((len(lst) - c2 - b), -3, -1):
            c3 = lst[c2][c4]
            break
        c1 += [c3]
    t1 += [s] + [b3] + [c1]
print(t1)


# lst = [[1, 2], [3, [4, 5]], 6, [[7, 8], 9 ]]

# l1 = []
# for l2 in lst:
#     if type(l2) != list:
#         l1.append(l2)
#     if isinstance(l2, list):
#         for l3 in l2:
#             if type(l3) != list:
#                 l1.append(l3)
#             if isinstance(l3, list):
#                 for l4 in l3:
#                     if type(l4) != list:
#                         l1.append(l4)
# # print(l1)

# lst = [1, 2, 3, 4, 5, 6]
# # lst1 = [6, 1, 5, 2, 4, 3]

# i = 0; l3 = []; j = (int(len(lst) / 2 ) - 1); t = len(lst) - 1
# for l1 in range(t, j, -1):
#     l3.append(lst[l1])
#     for l2 in range(1):
#         l3.append(lst[i]); i += 1
# # print(l3)


# # s = []; t = []; f = []
# # for l1 in lst:
# #     l2 = lst[0]
# #     if l2 < l1:
# #         s += [l1]
# #     else:
# #         t += [l1]
# # f = s + t
# # print(f)


# lst = [0, 1, 0, 13, 12]
# # lst1 = [1, 12, 13, 0, 0]

# for l1 in range(len(lst)):
#     for l2 in range(len(lst)):
#         if lst[l1] < lst[l2]:
#             lst[l1], lst[l2] = lst[l2], lst[l1]
# c = 0
# for j in lst:
#     if j == 0:
#         c += 1
# for b2,b2 in enumerate(lst[:]):
#     if b2 == 0:
#         lst[lst.index(0):lst.index(0) + 1] = []
# for b1 in range(0, c):
#     lst.append(0)
# print(lst)



# lst = [9,12, 3, 5, 14, 10, 10]
# for l1 in range(len(lst)):
#     for l2 in range(len(lst)):
#         if lst[l1] < lst[l2]:
#             lst[l1], lst[l2] = lst[l2], lst[l1]
# print(lst)

# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # lst1 = [[1, 2, 3], [6, 9, 8], [7, 4, 5]]

# # s = [ lst[0][0], lst[0][1], lst[0][2] ], [ lst[1][2], lst[2][2], lst[2][1] ] , [ lst[2][0], lst[1][0], lst[1][1] ]
# # print(s)

# s = []
# d = []
# f = []
# t = []
# for i, j in enumerate(lst):
#     if i == 0:
#         s.append(j)
#     if i == 1:
#         for q in (len(j) - 1, len(j) - 1, -1):
#             d.append(j[q])
#             break
#     if i == 2:
#         for a1 in range(len(j) - 1, 0, -1):
#             d.append(j[a1])
# t += [*s] + [d]
# print(t)
# s1 = 0
# for p1,p5 in enumerate(lst):
#     p4 = t[p1]
#     for p6,p2 in enumerate(p5):
#         print(p2 in p4)
        


# a = []
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(1):
#     for j in range(0, 3):
#         a.append(lst[j])
#     for s in range(3, 6):
#         if s == 5:
#             a.append(lst[s])
#     for t in range(len(lst) - 1, len(lst) - 3, -1):
#         a.append(lst[t])
# # print(a)
# for p1 in lst:
#     if p1 not in a:
#         a.append(p1)
# print(a)