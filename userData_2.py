from userData_1 import User

Us = User.removeFeild('username', 'first_name').feildValue('gmail')
print(Us)

# A1 = User.feildValue('gmail').removeFeild('username')

lst = ['akash', 'suresh', ("Heloo", "Meoo"), 'rahul', 'santosh', 'ashish', ('hi', 'hello')]
lst1 = [
    {"username" : 'suresh', "mobile" : 8976},
    {"username" : 'pritam', "mobile" : 8909},
    {"username" : 'akash', "mobile" : 8768}
]
# lst2 = []
A1 = User.ASC()
print(A1)

# A2 = User.feildValue('gmail').ASC()
# print(A2)