# dictionary varieties 

d = {(1, 5):'ME126', (3, 2):'ME102', (5, 4):'ME234'}
print(d)

print()
# variety 1
# ----------------------------------------------------
contacts = {
    'Anil':{'DOB':'17/11/98', 'Favourite':'Igloo'},
    'Amol':{'DOB':'14/10/99', 'Favourite':'Tundra'},
    'Ravi':{'DOB':'19/11/97', 'Favourite':'Artic'}
}

print(contacts['Amol']['Favourite'])    # Tundra


# -------------------------------------------------
# example 1

tpl_out = ()
for key, val in contacts.items():
    tpl_out += ((val['DOB'], val['Favourite']), )
print(tpl_out)

# ------------------------------------------------
# varierty 2

animals = {'Tiger':141, 'Lion':152, 'Leopard':110}
birds = {'Eagle':38, 'Crow':3, 'Parrot':2}
combined1 = {}
combined1 = animals | birds
print(combined1)

combined2 = {}
combined2 = combined2 | animals | birds
print(combined2)

combined3 = {**animals, **birds}
print(combined3)    # unpack

combined3 = {*animals, *birds}
print(combined3)

combined3 = {*animals.values(), *birds.values()}
print(combined3)

combined3 = {*animals.items(), *birds.items()}
print(combined3)    # dict {(tuple), (), ()}


print()
print()
# --------------------------------------------------
lst = [12, 13, 14, 15, 16]
d = dict.fromkeys(lst, 25)
print(d)

# without any function
d = {}
for i in lst:
    d[i] = 25
print(d)


print()
# ----------------------------------------------------
lst1 = [10, 20, 30]
lst2 = [100, 200, 300]

d = {}
for i in range(len(lst1)):
    d[lst1[i]] = lst2[i]
print(d)


print()
# --------------------
tpl = (10, 20, 30)
d = {}
for i in range(0 , len(tpl)):
    d[i] = tpl[i]
print(d)

d = {}
for ind, ele in enumerate(tpl):
    d[ind] = ele
print(d)

print()
# zip function 
# -----------------------------------------
lst1 = [10, 20, 30]
lst2 = [100, 200, 300]
d = {}
for i, j in zip(lst1, lst2):
    d[i] = j
print(d)