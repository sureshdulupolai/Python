from database import Check

lst = [
    {'id' : 1, 'name' : 'Pizza', 'price' : 100},
    {'id' : 2, 'name' : 'Pasta', 'price' : 120},
    {'id' : 3, 'name' : 'Sandwich', 'price' : 100},
    {'id' : 4, 'name' : 'Burger', 'price' : 199},
    {'id' : 5, 'name' : 'Veg Roll', 'price' : 80}
]

lst1 = [
    [('id', 7), ('name', 'tandoori'), ('price', 120)],
    [('id', 8), ('name', 'Panner Masala'), ('price', 180)]
]


# obj = Check(lst, 'price', 100)
# table = obj.get()
# print(table)

# for i in table:
#     # print(i['id'])
#     print(i['name'])
#     print(i['price'])
#     print()

# obj = Check(lst)
# obj.select()

# obj = Check(lst, 'price')
# var = obj.sums()
# print(var)

# obj = Check(lst, 'price')
# var = obj.asc()
# print(var)

# obj = Check(lst, 'price')
# var = obj.desc()
# print(var)

# obj = Check(lst, 'price')
# var = obj.dis()
# print(var)

# obj = Check(lst, 'name')
# var = obj.group()
# print(var)

# obj = Check(lst)
# var = obj.truncate()
# print(var)

# obj = Check(lst)
# var = obj.Tabledelete()
# print(var)

obj = Check(lst, lst1, ck=[('int', 'not', 'primary key'), ('varchar', '5', 'not null'), ('int', 'not null')])
var = obj.add()
print(var)