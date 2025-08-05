# list : mutable, ordered 
# accessed using : index position
# mutated using : index position and methods

# tuple : immutable, ordered 
# accessed using : index position
# mutated using : None

# set : mutable, unordered 
# accessed using : None
# mutated using : Methods

# dictionary : mutable, ordered 
# accessed using : keys
# mutated using : keys and mthods

# ----------------------------------------------------------------------------

d1 = {'A101':'krish', 'A102':'Kalim', 'A103':'Alex'}
for ele, ind in enumerate(d1.keys()):
    print(ele+1, ind)

for ele, ind in enumerate(d1.values()):
    print(ele+1, ind)

for ele, ind in enumerate(d1.items()):
    print(ele+1, ind)

# accessing the elements in dictionary
print(d1['A101'])

# using tuple as a key is permitted 
# using a list as a key can make value change
# when a key has to be fixed 
# this is why only immutable datatypes can be used as keys
d2 = {(10, 20): 'Amol', 'A102':'Anil', 'B103':'Ravi'}
