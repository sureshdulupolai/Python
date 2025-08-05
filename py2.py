import random

lst = ['Suresh', 'AMan', 'KRiSh', 'sANTOSH', 'PRITAM', 'ashish']
lst1 = ['Suresh', 'Aman', 'Krish', 'Santosh', 'Pritam', 'Ashish']
lst2 = []; lstOfNo = []; NewSet = set()

for Data in range(len(lst)):
    lst[Data] = lst[Data].title()
lst2 += lst

while True:
    randomNo = random.randint(0, (len(lst1) - 1))
    if randomNo not in lstOfNo:
        lstOfNo.append(randomNo)
        lst2.append(lst1[randomNo])

    elif len(lstOfNo) == len(lst1):
        break

for CheckData in lst2:
    NewSet.add(CheckData)

lst2.clear()
for DataIn in NewSet:
    lst2.append(DataIn)

lst2.sort()
print(lst2)