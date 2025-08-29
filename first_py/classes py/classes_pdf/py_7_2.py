# basic list operations
animals = ['Gurishish', 'Suresh', 'Kalim', 'Hemant', 'Hanosh', 'Piyush']
ages = [25, 26, 25, 27, 26, 28, 25]
print(animals)
print(ages)

# mutating the list elements
animals[2] = 'Rhinoceros'
print(animals)

ages[5] = 31
print(ages)

# multiple change in one line 
ages[2:5] = [10, 20, 30]
print(ages)

# replacing two elements with four elements
ages[1:3] = [40, 50, 60, 70]
print(ages)
print(id(ages))

# replacing three elements with two elements
ages[6:9] = [80,90]
print(ages)
print(id(ages))

# deleting the selected elements from the list
ages[2:5] = []
print(ages)
print(id(ages))

# deleting all the elements in the list
ages[:] = []
print(ages)
print(id(ages))

# deleting the entire list object
del(ages)
# print(ages)          -- error, because it delete (ages) 

