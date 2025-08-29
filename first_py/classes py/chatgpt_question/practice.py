# num = input("Enter a Number :")
# convert string char to integer for if part
# int_num = int(num)
# 
# num_2 = ' '.join(num)
# num_3 = num_2.split(" ")
# index value inside another variable & without another variable
# num_index_0 = int(num_3[0])
# num_index_1 = int(num_3[1])
# num_index_2 = int(num_3[2])
# first = int(num_3[0]) ** 3
# second = int(num_3[1]) ** 3
# third = int(num_3[2]) ** 3
# total = first + second + third

# if total == int_num:
#     print("The Number {} is Armstrong number".format(num))

# else:
#     print("The Number {} is Not a Armstrong number".format(num))

# a = 5
# b = 1
# while a >= 1:
#     b *= a
#     a -=1
# print(b)  

# a = 5
# b = 1
# c = 1
# while c <= a:
#     b *= c
#     c += 1
# print(b)

# count = 0
# a, b = 0, 1
# while count < 10:
#     print(a)
#     a, b = b, a + b
#     count += 1

# num = 13
# count = 2
# is_prime = True
# while count < num:
#     if num % count == 0:
#         is_prime = False
#         break
#     count += 1
# print(is_prime)

# num = 121
# original_num = num
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(original_num == reversed_num)

# s = "hello"
# reversed_str = ""
# i = len(s) - 1
# while i >= 0:
#     reversed_str += s[i]
#     i -= 1
# print(reversed_str)

# s = "hello"
# c = len(s) - 1 
# while 0 <= c:
#     print(s[c],end="")
#     c -= 1

# num = 28
# count = 1
# divisors_sum = 0
# while count < num:
#     if num % count == 0:
#         divisors_sum += count
#         print(divisors_sum)
#     count += 1
# print(divisors_sum == num)

# # Using nested for loops to generate 30 more multiplication questions
# counter = 0  # Counter to track the number of questions
# for i in range(2, 12):  # Outer loop: Start with 2 and go up to 11 (total of 10 numbers)
#     for j in range(1, 11):  # Inner loop: Multiply each number from 1 to 10
#         if counter <= 30:  # Ensure we only print 30 questions
#             print(f"{i} x {j} = {i * j}")
#             counter += 1  # Increment counter for each question
#         else:
#             break  # Stop once 30 questions have been printed
#     if counter >= 30:  # If 30 questions are printed, stop the outer loop
#         break

# c = int(input("Enter Till Wich Table You Need"))
# d = int(input("Enter {} x ? You Need : ".format(c)))
# f = 0
# for i in range(1,c):
#     for j in range(1,11):
#         if i == 5 and j == d:
#             f += 1
#             break
#         if f == 0:
#             print("{} x {} = {}".format(i, j, i*j))
#     if f == 1:
#         break
#     print()

# s = 'suresh'
# c = 5
# while c < len(s) - 1:
#     print(s[c])
#     c -= 1
# print(a)

# Youtube Question
# a3b4c2 -------> aaabbbbcc

# solved by own
# var_one = 'a2b4c2d3'
# c = 0
# b = 1
# six = ""
# while c <= len(var_one):
#     var_two = var_one[c]
#     var_three = int(var_one[b])
#     var_four = (var_two * var_three)
#     six += var_four
#     c += 2
#     b += 2
# print(six)

# sir help needed
# Youtube Solution 
# st = 'a2b3c6'
# ot = ''
# for char in st:
#     if char.isalpha():
#         var=char
#     else:
#         num=int(char)
#         ot += (var*num)
# print(ot)

