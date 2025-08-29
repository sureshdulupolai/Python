# #[10, 20, 30]
# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# ind = 0
# lst1 = []
# for i in range(0, 3):
#     lst1 += [lst[ind]]
#     ind = ind + 1
# print(lst1)

# #[10, 20, 30]
# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# ind = 0
# outer = []
# for j in range(0,3):
#     lst1 = []
#     for i in range(0, 3):
#         lst1 += [lst[ind]]
#         ind = ind + 1
#     outer += [lst1]
# print(outer)

# #[10, 20, 30]
# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# ind = 0
# outer = []
# for j in range(0,3):
#     lst1 = []
#     for i in range(0, 3):
#         lst1 += [lst[ind]]
#         ind = ind + 1
#     outer += [lst1]
# print(outer)

# question : lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# output need:
# [[10, 20, 30],[70,80,90]]
# [[10 + 70],[20 + 80],[30,90]]
# [[80],[100],[120]]
# solution:
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
ind = 0
outer = []
for j in range(0,3):
    lst1 = []
    for i in range(0, 3):
        if ind < len(lst):
            if (lst[ind] != 1 and lst[ind] != 40 and lst[ind] != 50 and lst[ind] != 60):
                lst1 += [lst[ind]]
                ind += 1
            else:
                ind += 1
        else:
            lst1 += [1]
            ind += 1
    outer += [lst1]
l = (sorted(outer)[1:])
print(l)
l1 = l[0]; l2 = l[1]; u = []; t = 0; s = []
for k in l1:
    u += [sum(l1[t:t+1] + l2[t:t+1])]
    t += 1
# print(u)
h = []; b = 0
for m in range(0,3):
    g = []
    for d in range(0,1):
        g += [u[b]]
        b += 1
    h += [g]
print(h)
print()
print([l1[0] + l2[0]] == h[0]) # True [10 + 70] == [80] --> [80] == [80]
print(l1[1] + l2[1] == h[1]) # false 10 + 70 == [80] --> 80 != [80]  --> int and list not match
