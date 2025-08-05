# doesn't work
# ----------------------------------------
# merging
# deep copy
# concatenation

# conversion
# --------------------------------------------------------------------

dct_1 = {1:10, 2:20, 3:30}

lst_1 = list(dct_1.keys())
print(lst_1)        # all dict key inside = list

lst_2 = list(dct_1.values())
print(lst_2)        # all dict value inside = list

lst_3 = list(dct_1.items())
print(lst_3)        # all dict key and value pair inside = tuple and all tuple inside list

# tuple is compalsary
lst = [(1, 10), (2, 20), (3, 30)]
dct = dict(lst)
print(dct, 'dict convert')

print()
# aliasing or shallow copy
# -------------------------------------------------------
dct_2 = dct_1
print(id(dct_1))
print(id(dct_2))

# searching 
# ---------------------------------------------------
print(1 in dct_1)   # by default it search .keys()
print(1 in dct_1.keys())
print(10 in dct_1.values())
print((1, 10) in dct_1.items())

# identify 
# -----------------------------------------------------------
print(dct_1 is dct_2)


# address - creating new obj every time with same values (like: list())
# two different objects with same values 
dct_3 = {1:10, 2:20, 3:30}
print(id(dct_1))
print(id(dct_3))

# example 
# --------------------------------------------------------------
dct1 = {'x':10, 'y':20, 'z':30}
dct2 = {'x':40, 'y':50, 'z':60}

dct3 = {}
for ind, (key, value) in enumerate(dct1.items()):
    print(ind, ' ', key, ' ', value)
    dct3[key] = dct1[key] + dct2[key]               # dct3[key] = first it have 'x' = dct[key] + dct[key] , 'x' = 10 + 40, 'x' = 50, {'x':50}
print(dct3, 'debug new dict')

# example 
# --------------------------------------------------------------
dct1 = {'x':10, 'y':20, 'z':30}
dct2 = {'m':40, 'n':50, 'o':60}

lst1 = list(dct1.items())
lst2 = list(dct2.items())

dct3 = {}
for ind, (key, value) in enumerate(lst1):
    dct3["{}+{}".format(key, lst2[ind][0])] = lst1[ind][1] + lst2[ind][1]
    # dct3["{}+{}".format(lst1[ind][0], lst2[ind][0])] = lst1[ind][1] + lst2[ind][1]        # both are same 
print(dct3)