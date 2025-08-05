
# workEveryDay = ['Run','Read Book','Execesise','sleep 2hr', 'Study', 'with friend']; completed = []; notCompleted = []
# for i in workEveryDay:
#     s = input('{} Done ? Enter Yes or No : '.format(i)).lower()
#     if s == 'yes':
#         completed.append(i)
#     else:
#         notCompleted.append(i)
# print(); print('You Have Completed {}'.format(completed))
# print(); print('You Need To Complete Work Now : {}'.format(notCompleted))

# name, age, salary = dahej calculator
# 12 + 28 = date of, skip, 
# coin toss = random
# 3a = project, exam, attendence / score
# project head = 10 person day of work
# random password
# random hexca code color to user


# userName = input('Enter Your Name : ')
# userAge = int(input('Enter Your Age : '))
# userSalary = float(input('Enter Your Salary : '))

# Dahej = userSalary * 10
# ChildDahej = userSalary * 20

# if userName.isalpha():
#     if userAge <= 0:
#         print('Enter Correct Age First To Calculate a Dahej, otherWise You Will Get L**da')
#     elif userAge < 18:
#         print('You Dont Need To Work Mr/Ms. {}, You Will Get Dahej According To Your Expectation'.format(userName))
#         print('But I Think You Will Get Dahej {}'.format(ChildDahej))
#     elif userAge >= 18:
#         if userSalary:
#             print('{} You Will Get Dahej {}'.format(userName, Dahej))
#         else:
#             print('Enter Your Salary In Rupees')
# else:
#     print('Enter Your Name Correctly.')


# # Creating a List From 1 To 30
# lst = []
# for i in range(1, 31):
#     lst.append(i)
# # Taking Input From User
# dateOf = int(input('Enter a Date Of This Month : '))
# # Creating a New List To Calculate
# lst1 = []
# if dateOf in lst:
#     for l1 in range(dateOf, 31):
#         lst1.append(l1)
#     for l2 in range(1, dateOf):
#         lst1.append(l2)
# else:
#     print('Enter Correct Number.')
# # count
# print(lst1[27])


# # import random
# s = random.randint(0,1)
# if s == 0:
#     print('Tail')
# else:
#     print('Head')


# # random hex code color to user
# import random
# lst = ['#FF5733 (Vibrant Orange)','#4CAF50 (Green)', '#1E90FF (Dodger Blue)','#FFC0CB (Pink)',
# '#8A2BE2 (Blue Violet)', '#FFD700 (Gold)', '#FFFFFF (White)', '#000000 (Black)', '#FF1493 (Deep Pink)',
# '#800080 (Purple)', '#00CED1 (Dark Turquoise)', '#A52A2A (Brown)', '#008080 (Teal)', '#D3D3D3 (Light Gray)',
# '#F0E68C (Khaki)']
# s = random.randint(0,(len(lst) - 1))
# print('This a Random Color Choice For You : {}'.format(lst[s]))


# lst = ['Piyush', 'Manshi', 'Varsha', 'Kajal', 'Hemant', 'Hanush']
# lst1 = []
# lst2 = []
# for i in lst:
#     t1 = input("{} Done Head For This Weak ? : ".format(i)).lower()
#     if 'y' in t1:
#         lst1.append(i)
#     else:
#         lst2.append(i)
# print()
# print('{} Have Completed The Head Of This Weeek.'.format(lst1))
# print('{} They, Have Not Completed Head For This Week'.format(lst2))
# print()
# leftPerson = len(lst2)
# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thusday', 'Friday', 'Satarday']
# j = 0
# for t3 in range(1, leftPerson + 1):
#     print('"{}" Will Come To Take Gursish Head On in This Week "{}" '.format(lst2[j], days[-t3]))
#     j += 1
# print()
# p = 0
# donePerson = len(lst1)
# for a1 in range(0, donePerson):
#     print('"{}" Will Come To Take Gursish Head On Next Week "{}"'.format(lst1[p],days[a1]))
#     p += 1


# 
# import random
# rate = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
# rdm = random.randint(0, (len(rate) - 1))
# userInput = int(input('Enter a Value \n 100, 150, 200, 250, 300, 350, 400, 450, 500, 550 : '))
# if userInput == rate[rdm]:
#     print('You Have Choose Perfect Rate Of R**d {}'.format(userInput))
# else:
#     print('{} You Have Not Choose Perfect Rate Of R**d, Actual Rate is {}'.format(userInput, rate[rdm]))

import random
lst1 = []; lst2 = []; lst3 = []; lst4 = []; lst5 = []; lst6 = []; mainLst = [lst1, lst2, lst3, lst4, lst5, lst6]; x = 1; y = 100
for i,j in enumerate(mainLst):
    while len(j) <= 29:
        h = random.randint(x , y)
        if h in j:
            pass
        else:
            j.append(h)
    x += 100; y += 100
# for a1 in mainLst:
#     print(a1)
#     print()
inp1 = int(input('Enter a No : '))
inp2 = int(input('Enter a No : '))
inp3 = int(input('Enter a No : '))
inp4 = int(input('Enter a No : '))
inp5 = int(input('Enter a No : '))
inp6 = int(input('Enter a No : '))
c1 = 0; c2 = 0; c3 = 0; c4 = 0; c5 = 0; c6 = 0
for p1,p3 in enumerate(mainLst):
    if p1 == 0:
        for p2 in p3:
            if p2 == inp1:
                p3.remove(inp1)
                c1 += 1
    if p1 == 1:
        for p2 in p3:
            if p2 == inp2:
                p3.remove(inp2)
                c2 += 1
    if p1 == 2:
        for p2 in p3:
            if p2 == inp3:
                p3.remove(inp3)
                c3 += 1
    if p1 == 3:
        for p2 in p3:
            if p2 == inp4:
                p3.remove(inp4)
                c4 += 1
    if p1 == 4:
        for p2 in p3:
            if p2 == inp5:
                p3.remove(inp5)
                c5 += 1
    if p1 == 5:
        for p2 in p3:
            if p2 == inp6:
                p3.remove(inp6)
                c6 += 1
ct = [c1, c2, c3, c4, c5, c6]; ct1 = len(ct)
y1 = 0
for l1 in ct:
    if l1 == 0:
        del ct[l1]
        y1 += 1
print(ct1 - y1)
if len(ct) == 4:
    print('SuccessFull Done The Match')
elif len(ct) > 4:
    print('try again')
elif len(ct) < 4:
    print('Not Closer Try again untill you reach 2 dead')
else:
    print('Error not found')
# to check answer for remove list
# for p in mainLst:
#     print(p)
#     print()