def listReverse():
    num = [1, 2, 8, 4, 5, 6, 7]
    print(num)
    n = len(num) - 1
    for i in range(n//2+1):
        temp = num[i]
        num[i] = num[n - i]
        num[n - i] = temp
    print(num)

lst = [
    { "name" : "Alice", "department" : "IT", "salary" : 70000},
    { "name" : "Bob", "department" : "HR", "salary" : 50000},
    { "name" : "Charlie", "department" : "IT", "salary" : 80000},
    { "name" : "David", "department" : "Finance", "salary" : 60000},
    { "name" : "Eve", "department" : "HR", "salary" : 55000},
    { "name" : "Frank", "department" : "Finance", "salary" : 75000}
]

def dctOneData(lst):
    if isinstance(lst, list):
        for j in lst:
            if isinstance(j, dict):
                lst2 = []
                for i in range(len(lst)):
                    var1 = lst[i]['department']; v1 = lst[i]['salary']; v2 = lst[i]
                    for a1 in lst:
                        for a2 in a1.values():
                            if ((a2 == var1) and (v1 < a1['salary'])): v1 = a1["salary"]; v2 = a1 
                            else:continue
                    if v2 not in lst2: lst2 += [v2] 
                    else:continue
                return lst2
    else:
        return ("List Not Carring Any Dictionary, \nOr Dict is Not Carry Index like 'name', 'department', 'salary' \nOr List Carry <int, str, bool, float, tuple, list, set> \nCheck if this type of data present inside list then it does'n work")
    
# lst5 = ['hi', {'hi':'hello'}]
# var = dctOneData(lst)
# print(var)


# arr1 = [2, 1, 4, 6, 3]
# arr2 = [1, 7, 8, 3, 2]

# arr3 = []
# for i in range(len(arr1)):
#     lst = []
#     for j in range(len(arr2)):
#         if arr1[i] not in arr2:
#             arr3 += [arr1[i]]
#             # break

#         if arr2[j] not in arr1:
#             arr3 += [arr2[j]]
#             # break
# print(arr3)

# ----------------------------------------------------------------
# lst = [10, 20, 4, 45, 99]
# b1 = len(set(lst))
# if b1 == 1 or b1 == 0:
#     if b1 == 1:
#         print("Null")
#     else:
#         print('List is Empty')
# else:
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             if lst[i] > lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#     print(lst[1])


# ----------------------------------------------------------------
lst = [4, 3, 2, 4, 1, 3, 2] 
lst2 = []
if ((len(lst) / 2 ) == len(set(lst))) or len(lst) == 0:
    print("Null")
else:
    for i in lst:
        v1 = i
        count = 0
        for j in lst:
            if v1 == j:
                count += 1
            else:
                continue

        if count == 1:
            lst2 += [v1]
        else:
            continue
print(lst2)