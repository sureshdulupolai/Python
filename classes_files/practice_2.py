lst = ['aman', 'suresh', 'kalim', 'akash', 'pritam', 'ashish', 'rohan', 'roshan', 'shubhankar', 'rohit',
'adarsh', 'harsh', 'faizan', 'asim', 'raj', 'sourab', 'susil', 'santosh', 'abhishek', 'nizam','rahul',
'gursish', 'piyush', 'ravi', 'prasant', 'hemang', 'sagar', 'prasad','om']
print(len(lst))

# Search inside all word
# userInput = input('Enter a One Word To check Name Details : ').lower(); c = 0
# userInput1 = userInput[0]
# for a1 in lst:
#     if userInput1 in a1:
#         print(a1)
#         c += 1
# print()
# print('Total Member With Letter "{}" is "{}"'.format(userInput1, c))

# from first letter
# UserInput = input('Enter First Letter To Search Name Details : ').lower(); d = 0
# UserInput1 = UserInput[0]
# for b1 in lst:
#     if b1[0] == UserInput1:
#         print(b1)
#         d += 1
# print('Total Member With Letter "{}" is "{}"'.format(UserInput1, d))

# Search With Full Word
# userInput = input('Enter a String : ').lower()
# for c1 in lst:
#     if userInput == c1:
#         print(c1)

# ---------------------------------------------------------------------------------
# 1. **Find the length of the list `lst`.**
#    - **Question:** What is the total number of names in the list `lst`?


# count = 0
# for a1 in lst:
#     count += 1
# print(count)


# 2. **Search for a name in the list.**
#    - **Question:** Is the name 'akash' present in the list `lst`?


# count = 0
# for a1 in lst:
#     if a1 == 'akash':
#         count += 1
# print(count)


# 3. **Access a specific name by its index.**
#    - **Question:** What is the name at index 3 in the list `lst`?


# user = int(input('Enter To Check Perticular Index Value : '))
# for a1 in lst:
#     if a1 == lst[user]:
#         print(a1)


# 4. **Check if the list contains a name starting with a specific letter.**
#    - **Question:** Does the list `lst` contain any names that start with the letter 'A'?


# for a1 in lst:
#     if 'a' in a1:
#         print(a1)


# 5. **Count the number of names with a specific letter in them.**
#    - **Question:** How many names in the list `lst` contain the letter 'r'?


# for a1 in lst:
#     if 'r' in a1:
#         print(a1) 


# 6. **Extract a sublist.**
#    - **Question:** What is the sublist of `lst` that contains the first 5 names?


# for a1 in lst:
#     for a2 in range(0, 5):
#         if len(a1) >= 5:
#             if a1[a2]:
#                 print(a1[a2], end='')
#         else:
#             print(a1, end='')
#             break
#     print()
        

# 7. **Sort the list in alphabetical order.**
#    - **Question:** What is the list `lst` sorted in alphabetical order?


# print(lst)
# for a1,b1 in enumerate(lst):
#     for a2,b2 in enumerate(lst):
#         if b2 > b1:
#             lst[a1], lst[a2] = lst[a2], lst[a1]
#         else:
#             pass
# print(lst)
            

# 8. **Find the name with the longest length.**
#    - **Question:** Which name in the list `lst` has the longest length?


# a2 = lst[0]
# for a1 in lst:
#     if len(a2) < len(a1):
#         a2 = a1
# print(a2)



# 9. **Check for duplicates in the list.**
#    - **Question:** Are there any duplicate names in the list `lst`? - ture aur false


# s = []
# count = 0
# for a1 in lst:
#     if a1 not in s:
#         s.append(a1)
#     else:
#         count += 1
# if count >= 1:
#     print('Duplicate Inside Lst')
# else:
#     print('No Duplicate Inside Lst')


# 10. **Find the index of a name in the list.**
#     - **Question:** At which index does the name 'rohit' appear in the list `lst`?


# count = 0
# for a1 in lst:
#     if a1 == 'rohit':
#         break
#     else:
#         count += 1
# print(count)


# 11. **Add a new name to the list.**
#     - **Question:** If the name 'john' is added to the list `lst`, what will the new list look like?


# userName = input('Enter a Name : ')
# lst = lst + [userName]
# print(lst)


# 12. **Remove a specific name from the list.**
#     - **Question:** What will the list `lst` look like after removing the name 'kalim'?

# ---------------------------------
# for a1,a2 in enumerate(lst):
#     if a2 == 'kalim':
#         lst[a1] = [ ]
# print(lst)
# ------------------------------


# a2 =[]
# for a1 in lst:
#     if a1 == 'kalim':
#         continue
#     else:
#         a2 = a2 + [a1]
# print(a2)


# 13. **Reverse the list.**
#     - **Question:** What is the list `lst` after reversing the order of its elements?


# a2 = []
# for a1 in range(len(lst) - 1, -1, -1):
#     a2.append(lst[a1])
# print(a2)


# 14. **Find all names that have more than 5 characters.**
#     - **Question:** Which names in the list `lst` have more than 5 characters?


# for a1 in lst:
#     if len(a1) > 5:
#         print(a1)


# 15. **Find the first name that contains a specific substring.**
#     - **Question:** What is the first name in the list `lst` that contains the substring 'ro'?


# for a1 in lst:
#     if 'ro' in a1:
#         print(a1)


# --------------------------------------------------------------------------------------

# 1. **Get the count of employees.**
#    - **Question:** How many employees are listed in the company database?


# count = 0
# for a1 in lst:
#     count += 1
# print('There are {} Employee inside database'.format(count))


# 2. **Check if a specific employee is in the database.**
#    - **Question:** Is 'rahul' listed as an employee in the company database?


# count = 0
# for a1 in lst:
#     if a1 == 'rahul':
#         count += 1
# if count >= 1:
#     print('Yes {} is present in database'.format('rahul'))
# else:
#     print('{} Not present in database'.format('rahul'))


# 3. **Find the employee at a given position.**
#    - **Question:** Who is the employee at position 5 in the company employee list?

# user = 5
# print(lst[user])


# 4. **List employees who have a specific role.**
#    - **Question:** Which employees in the database have names that start with the letter 'A'?


# for a1 in lst:
#     a2 = a1[0]
#     if a2 == 's':
#         print(a1)


# 5. **Find all employees whose name contains a certain substring.**
#    - **Question:** Which employees in the list have the substring 'ash' in their names?


# for a1 in lst:
#     if 'ash' in a1:
#         print(a1)


# 6. **Check if a name appears multiple times.**
#    - **Question:** Is 'santosh' a duplicate in the company’s employee list?


# count = 0
# for a1 in lst:
#     if a1 == 'santosh':
#         count += 1
# if count > 1:
#     print('{}, Duplicate Inside List'.format('santosh'))
# else:
#     print('{}, Name have No Duplicate Inside List'.format('santosh'))


# 7. **Find the employee with the longest name.**
#    - **Question:** Who has the longest name among the employees in the list?


# a2 = lst[0]
# for a1 in lst:
#     if len(a2) < len(a1):
#         a2 = a1
# print(a2)


# 8. **Sort the employee list alphabetically.**
#    - **Question:** What is the company’s employee list in alphabetical order?


# for a1,b1 in enumerate(lst):
#     for a2,b2 in enumerate(lst):
#         if b1 < b2:
#             lst[a1], lst[a2] = lst[a2], lst[a1]
# print(lst)


# 9. **Add a new employee to the list.**
#    - **Question:** How will the employee list look after adding a new hire, 'neha'?


# user = 'neha'
# lst += [user]
# print(lst)


# 10. **Remove an employee from the list.**
#     - **Question:** What is the updated employee list after removing 'harsh'?


# a2 = []
# for a1 in lst:
#     if a1 == 'harsh':
#         continue
#     else:
#         a2 += [a1]
# print(a2)


# 11. **Get the list of employees whose names start with a specific letter.**
#     - **Question:** Which employees’ names start with 'R' in the company database?


# for a1 in lst:
#     if a1[0] == 'r':
#         print(a1)


# 12. **Get the number of employees with a certain characteristic.**
#     - **Question:** How many employees have names with more than 5 characters?


# a2 = lst[0]
# for a1 in lst:
#     if len(a2) < len(a1):
#         a2 = a1
# print(a2)


# 13. **Find employees who are present in a specific department.**
#     - **Question:** Which employees are in the 'IT' department, based on their name being part of the department code?

# a3 = 0
# for a1,a2 in enumerate(lst):
#     if a1 % 2 == 0:
#         print(a3, a2)
#         a3 += 1

# 14. **Check if an employee exists in multiple departments.**
#     - **Question:** Is 'rohit' listed in multiple teams within the company?


# c1 = 0
# for a1 in lst:
#     if a1 in 'rohit':
#         c1 += 1
#     else:
#         continue
# if c1 > 0:
#     print('Yes')
# else:
#     print('No')
    

# 15. **Retrieve the list of employees from a certain city or region.**
#     - **Question:** How can we get a list of employees who are based in the 'Delhi' office, based on their names?


# a3 = []
# for a1 in range(0, 2):
#     user = input('Enter a String : ')
#     for a2 in lst:
#         if a2 == user:
#             a3 += [user]
#         else:
#             continue
# print(a3)


# 16. **Find the first employee with a name that contains a specific letter.**
#     - **Question:** Which employee is the first to have the letter 's' in their name?


# for a1 in lst:
#     if a1[0] is 's':
#         print(a1)


# 17. **Get the index of a particular employee in the list.**
#     - **Question:** What is the index of the employee 'roshan' in the employee database?


# for a1,a2 in enumerate(lst):
#     if a2 == 'roshan':
#         print(a1)
#     else:
#         continue


# 18. **Check for an employee’s status (active/inactive).**
#     - **Question:** Is 'pritam' currently an active employee, or has their contract expired?


# c1 = 0
# for a1 in lst:
#     if a1 == 'pritam':
#         c1 += 1
#     else:
#         continue
# if c1 > 0:
#     print('Active')
# else:
#     print('Inactive')


# 19. **Count employees who have been with the company for over 5 years.**
#     - **Question:** How many employees have names that are associated with a 5+ year tenure at the company?


# count = 0
# for a2 in range(0, 3):
#     user = input('Enter a Name : ')
#     for a1 in lst:
#         if a1 == user:
#             count += 1
#         else:
#             continue
# print('There are {} Employees Over 5 Year'.format(count))


# 20. **Check if the list of employees contains any seasonal workers or contractors.**
#     - **Question:** Does the list contain any employees who are seasonal or temporary workers based on their names?


# count = 0
# for a2 in range(0, 3):
#     user = input('Enter a Name : ')
#     for a1 in lst:
#         if a1 == user:
#             count += 1
#         else:
#             continue
# print('There are {} Employee seasonal workers or contractors in Our Company.'.format(count))


# -------------------------------------------------------------------------------