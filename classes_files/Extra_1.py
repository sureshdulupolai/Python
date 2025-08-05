# inSet = 'i love python programming'; loveOne = inSet[2:6]; lenOne = len(inSet)
# userInput = input('Enter Your Code : '); lenTwo = len(userInput)
# for i,j in enumerate(userInput):
#     if j == ' ':
#         loveTwo = userInput[i+1:i+5]
#         break
# if (lenOne == lenTwo):
#     if (loveOne in loveTwo):
#         print('Your PassWord Is Correct : Done')
#     else:
#         print('You Have Enter Wrong Password')
# else:
#     print('Length is Not Matching')


lst = [1, 2, [3, 4], 5, [6, 7], 8]
# lst_1 = [1, 2, [9, 16], 5, [36, 49], 8]

lst_1 = []
for i in lst:
    lst_2 = []; j = type(i)
    if (list == j):
        for q in i:
            lst_2 += [q * q]
        lst_1 += [lst_2]
    else:
        lst_1 += [i]
print(lst_1)
        

# 
lst = [1, 2, [3, 4], 5, [6, 7], 8]
lst_1 = []
for i in lst:
    if isinstance(i, list):
        lst_2 = []
        for j in i:
            lst_2 += [j * j]
        lst_1 += [lst_2]
    
    elif isinstance(i, int):
        lst_1 += [i]
print(lst_1)

print()
record = (
    ('abc', 24, 1.23), ('def', 25, 1.24),
    ('ghi', 26, 1.25), ('jkl', 27, 1.26)
)

print(record)
d = 0; t = []
for i in record:
    a = list(i); s = []
    for j,k in enumerate(a):
        if j == 1:
            s += [k + 226 + d]; d += 9
        else: 
            s += [k]
    t += [tuple(s)]
print(tuple(t))

# method two if there is any data type (int) then multiply with 10
print()
out = ()
for tpl in record:
    inn = ()
    for ele in tpl:
        if isinstance(ele, int):
            inn += (ele * 10,)
        else:
            inn += (ele,)
    out += ((inn), )
print(out)

