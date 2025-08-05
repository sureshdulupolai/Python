# built-in functions on dictionaries
# --------------------------------------------------

d1 = {'CS101':'OOP', 'CS102':'D5', 'CS201':'CCP'}
d2 = {'CS101':0, 'CS102':1, 'CS201':0}

# length
print(len(d1))

# max
print(max(d1.keys()))
print(max(d1.values()))
print(max(d1.items()))      # check only keys, but print (key,value) Pair. if keys are same then check values.

# min
print(min(d1.keys()))
print(min(d1.values()))
print(min(d1.items()))      # check only keys, but print (key,value) Pair. if keys are same then check values.

# sorted 
print(sorted(d1.keys()))
print(sorted(d1.values()))
print(sorted(d1.items()))

# sorted, reverse
print(sorted(d1.keys(), reverse=True))
print(sorted(d1.values(), reverse=True))
print(sorted(d1.items(), reverse=True))

d3 = {1:6, 2:4, 3:5, 4:8}
# output : {2:4, 3:5, 1:6, 4:8} with respect to values
   
lst1 = list(d3.items())
# print(lst1)
for i in range(len(lst1)):
    for j in range(len(lst1)-1):
        if lst1[j][1] > lst1[j+1][1]:
            lst1[j], lst1[j+1] = lst1[j+1], lst1[j]
print(dict(lst1))