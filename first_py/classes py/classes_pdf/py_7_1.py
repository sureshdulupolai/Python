# what is list ? 

num_one = [10, 20, 30, 40, 50]
print(num_one)
print(num_one[2])

print()
# list replication 
# a list can take duplicate elements
num_two = [10] * 5
print(num_two)
# all element pointing to same address
print(id(num_two[0]))
print(id(num_two[4]))

print()
# same datatype and multiple data type can store inside of list
# -------------------------------------------------------------
# a list can contain same data type
names = ['John', 'Peter', 'Steven']
# can take multiple data type
x =  ['Python',3.26, 3+2j, True, b'x/41', 65]

print()
# a list can take duplicate values 
ages =  [25, 26, 25, 27, 26]
num = [10] * 5                          # is not 50, but [10, 10, 10, 10, 10]

lst_one = ['I', 'am', 'here']
print(lst_one[0] + ' ' + lst_one[1] + ' ' + 'Everywhere')

# list slicing
lst_two = [10, 20, 30, 40, 50]

# it does not alter the orginal list
# but, creates a new object
print(lst_two[:3])
print(lst_two[3:])
print(lst_two[2:4])
print(lst_two[4:2:-1])

var_list = lst_two[0:4]
print(var_list)

l1 = [100, 200, 300, 400, 500]
l2 = [101, 201, 301, 401, 501]

# list concatenation 
l3 = l1[:2] + l2[2:]
print(l3)

