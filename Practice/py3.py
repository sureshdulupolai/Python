let = (
    { 'id' : 1, 'name' : 'suresh polai', 'age' : 18 }, 
    { 'id' : 2, 'name' : 'akash sahu', 'age' : 18 },
    { 'id' : 3, 'name' : 'pritam updhayay', 'age' : 19 },
    { 'id' : 4, 'name' : 'ashish moriya', 'age' : 20 },
    { 'id' : 5, 'name' : 'rohit sahu', 'age' : 19 },
    { 'id' : 6, 'name' : 'rohan sahu', 'age' : 18 },
    { 'id' : 7, 'name' : 'susant', 'age' : 21 },
)

# for i in let:
#     if i['age'] > 18:
#         print(i)

# print()
# for j in let:
#     a1 = j['name'].split(' ')[1]
#     if a1 == 'sahu':
#         print(j)

# print(let)
# print()
# for i in let:
#     i['age'] = str( i['age'] )
# print(let)


# user_inp = input('Enter Name : ').lower()
# user_len = len(user_inp)
# for i in let:
#     a1 = i['name'].split(' ')[0][:user_len]
#     if user_inp in a1:
#         print()
#         for j,k in i.items():
#             print("{} : {}".format(j, k))
#     else:
#         continue


# count_data = 0; count_no_data = 0; count_full_name = 0; count = 0
# for i in let:
#     a1 = i['name'].split(' '); a2 = len(a1)
#     if a2 == 2:
#         count_data += 1; count += 1
#     elif a2 == 1:
#         count_no_data += 1; count += 1
#     else:
#         count_full_name += 1; count += 1
# print("{} - Data are present in Database of User.".format(count_data))
# print("{} - No Full Data are present in Database of User.".format(count_no_data))
# print("{} - Full name data present inside 'Database'.".format(count_full_name))
# print("{} - Total Data present in database'".format(count))

# import copy
# data = copy.deepcopy(let)
# print(id(let))
# print(id(data))

# let1 = ()
# for i in let:
#     if i['id'] == 2:
#         continue
#     else:
#         let1 += (i,)
# print(let1)


# for i in data:
#     if i['name'] == 'susant':
#         i['id'] = 9
# print(let)
# print(data)
# print(let)

# def copy():
#     for i in let:
#         global let1
#         let1 += (i, )

# while True:
#     user_take = input("Do you need to insert data [y/n] : ")
#     let1 = ()
#     if user_take in 'no':
#         copy()
#         print(let1)
#         break
#     elif user_take in 'yes':
#         if len(let1) == 0:
#             copy()
#         else:
#             pass
#         a1 = let1[len(let1) - 1]['id']
#         user_id = a1 + 1
#         user_name = input('Enter client name : ')
#         user_age = int(input('Enter client age : '))
#         user_data = {'id': user_id, 'name' : user_name, 'age' : user_age}
#         let1 += (user_data, )
#         print(let1)

#     else:
#         print("wrong value passed")




class find():
    
    def __init__(self, a1, a2 = ''):
        self.nameOne = a1
        self.nameTwo = a2
        for i in range(len(self.nameOne) - 1, -1, -1):
            self.nameTwo += (self.nameOne[i])


    def palindrome(self):
        if self.nameOne == self.nameTwo:
            print('This is Palindrome')
        else:
            print('This Not a Paldirome')
    
    def reverse(self):
        print(self.nameTwo)



a1 = find('nitin')
a1.palindrome()
a1.reverse()

# def one():
#     v2 = 0
#     context = {
#     'name' : let,
#     }
#     print(context['name']['id'])
#     # return context

# # one()
# # v1 = one()
# print(v1)