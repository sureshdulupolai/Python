# declare a variable, we have declare "i"
# inside range(1. starting position, 2. ending position, increment & decrement)
# inside range(5) = by default it's consider as end position and here statring position will be 0 and increment position will be 1
# inside range(1,5) = inside range it will consider as statring position and ending position and here increment value by default will be 1
# end position need one step more exp: (0, 5) = print(0,1,2,3,4) only dont go to check for five

# printing 0 to 4 
for i in range(0, 5, 1):
    print(i)

print()
# printing 4 to 0
for i in range(5, 0, -1):
    print(i)

print()
# printing table of two
for i in range(1, 11, 1):
    print("2 * ",i,"=",i*2)
    # print("{} x {} = {}".format(2, i, 2*i))

print()
# 
for char in "Leopard":
    print(char)

print()
for animal in ['cat', 'dog', 'tiger', 'lion', 'leopard']:
    print(animal)

print()
# printing a string inside string one by one {list}
for animal in ['cat', 'dog', 'tiger', 'lion', 'leopard']:
    for char in animal:
        print(char)
    print()

# table from 2,3,4
for i in range(2, 5, 1):
    for j in range(1,11,1):
        print("{} x {} = {}".format(i, j, i*j))
    print()

print()
# 
for animal in ('cat', 'dog', 'tiger', 'lion', 'leopard'):
    print(animal)
