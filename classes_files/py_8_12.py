# write a program to create the following 3 list 

# A list of names
# A list of Roll No
# A list of Marks

# generate and print a list of tuples containing
# name, roll no, and marks from the 3 lists

# from this resultant list, genrate 3 tuple
# one containing all names
# another containing all roll no's
# and the third containing all marks

names = ['suresh','kalim','gursish']
roll_no = [101, 102, 103]
marks = [55, 76, 87]

total = [names, roll_no, marks]
# print(total)

print()
s = []
for i in range(0, len(total)):
    t = ()
    for j in range(0, len(total)):
        t += (total[j][i],)
    s += [t]
print(s)

print()
a = []
for i in range(0, len(total)):
    b = []
    for j in range(0, len(total)):
        b += [s[j][i]]
    a += [b]
print(a)