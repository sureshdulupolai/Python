# dictionaries (tuple and string) only be a name variable of dict.
# ---------------------------------------------------------

print()
# empty dictionary
d1 = {}
d2 = dict()
print(type(d1))
print(type(d2))

print()
# key : value pair
d3 = {'A101' : 'Amol', 'A102' : 'Anil', 'B103' : 'Ravi'}
print(d3)

# different keys can have the same values
d4 = {10 : 'A', 20 : 'A', 30 : 'Z'}

# if two keys are same them, the latest value is updated for the particular key
d5 = {10 : 'A', 20 : 'B', 10 : 'Z'}
print(d5)

# if the key:value pair is repeated, then only one pair gets stored
# or in other words, for a certain key the same value is updated again
d6 = {10 : 'A', 20 : 'B', 10 : 'A'}
print(d6)

