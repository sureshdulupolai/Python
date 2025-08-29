lst = [10, 20, 30, 30, 40, 50, 30, 60]
for ind, ele in enumerate(lst[:]):
    if ele == 30:
        lst[lst.index(30):lst.index(30)+1] = []
print(lst)

lst_1 = [10, 20, 30, 40, 50, 60]
lst_2 = []
for i in range(0,1):
    lst_2 += lst_1[:3]
print(lst_2)

# [10, 20, 30]
lst_4 = [10, 20, 30, 40, 50, 60]
ind = 0; lst_mat = []
for j in range(0,3):
    lst_mat = lst_mat + [lst_4[ind]]
    ind = ind + 1
print(lst_mat)

# [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# i  = [] -- outer list
# j = [[],[],[]] -- inner list
# ind = excessing the inner element of list [[10, 20, 30],[40,50,60],[70,80,90]
lst_4 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
ind = 0; lst_row = []
for i in range(0,3): 
    lst_col = []
    for j in range(0,3):
        lst_col = lst_col + [lst_4[ind]]
        ind = ind + 1
    lst_row = lst_row + [lst_col]
print(lst_row)

# if extra then 
lst_4 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
ind = 0; lst_row = []
t = 2
p = 6
for i in range(0,t): 
    lst_col = []
    for j in range(0,p):
        if ind < len(lst_4):
            lst_col = lst_col + [lst_4[ind]]
            ind = ind + 1
        else:
            lst_col = lst_col + [0]
    lst_row = lst_row + [lst_col]
print(lst_row)
