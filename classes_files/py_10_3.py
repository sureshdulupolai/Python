# looping in dictionaries 

courses = {'DAA':'CS', 'AOA':'ME', 'SVY':'ME'}
print(courses)

for key in courses.keys():
    print(key)

for values in courses.values():
    print(values)

for items in courses.items():       # packed form
    print(items)

for key,values in courses.items():     # unpacked = () + () = None
    print(key, values)

for ind, (key, values) in enumerate(courses.items()):       # enumerate > (ind, (key, value)) > ind key value
    print(ind, key, values)

# example - dict to tuple with using .items()
# ----------------------------------------------------------------
tpl = ()
for item in courses.items():
    tpl += (item, )
print(tpl)

