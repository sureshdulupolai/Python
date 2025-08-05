# higher order function
d1 = {'Oil': 230, 'Clip': 150, 'Stud': 175, 'Nut':35}
print(d1)


print()
d2 = list(d1.items())       # [('Oil', 230), ('Clip', 150), ('Stud', 175), ('Nut', 35)]
print(d2)

# key is not a dictionary (key) - key is a built-in keyword
print()             # with respect to key
d3 = sorted(d1.items(), key=lambda kv : kv[0])
print(d3)

print()             # with respect to value
d4 = sorted(d1.items(), key=lambda kv : kv[1])
print(d4)