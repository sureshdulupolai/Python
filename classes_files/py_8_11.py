# store the data about shares held by a user as tuple
# conataining the following information about shares

# share name 
# date of purchase 
# cost price
# no of shares 
# the selling price

# write a program to determine

# - total cost of the portfolio
# - total amount gained or lost
# - percentage profit gained or incurred(lost)

shrOne = ('Tata', '04/08/19', 40, 3, 51)
shrTwo = ('Tesla', '09/11/19', 45, 4, 55)
shrThree = ('SpaceX', '17/05/20', 35, 2, 30)
shrFour = ('Amazon', '26/05/21', 51, 7, 62)
shrFive = ('Blue Origin', '07/07/20', 42, 5, 45)

x = (shrOne, shrTwo, shrThree, shrFour, shrFive)
print(x)

print()
a1 = 0
for i,l in enumerate(x):
    m = 1
    for j,k in enumerate(l):
        if j >= 3:
            m *= k
    a1 += m
print('Total Cost Of Portfolio : {}'.format(a1))

print()
c1 = 0; c2 = 0
for a1,a2 in enumerate(x):
    t = a2[2]; s = a2[4]; d1 = 1; d2 = 1
    if t < s:
        for b1, b2 in enumerate(a2):
            if b1 >= 3:
                d1 *= b2
        c1 += d1
    else:
        for b1, b2 in enumerate(a2):
            if b1 >= 3:
                d2 *= b2
        c2 += d2
print('Profit Amount : {}'.format(c1))
print('Loss Amount : {}'.format(c2))


# new = (c1 / a1 * 100)
print()
h1 = 0
for i,l in enumerate(x):
    m = 1
    for j,k in enumerate(l):
        if j >= 3:
            m *= k
    h1 += m
c1 = 0; c2 = 0
for a1,a2 in enumerate(x):
    t = a2[2]; s = a2[4]; d1 = 1; d2 = 1
    if t < s:
        for b1, b2 in enumerate(a2):
            if b1 >= 3:
                d1 *= b2
        c1 += d1
        new = (c1 / h1 * 100)
    else:
        for b1, b2 in enumerate(a2):
            if b1 >= 3:
                d2 *= b2
        c2 += d2
print('Profit Amount : {}'.format(c1))
print('Loss Amount : {}'.format(c2))
print(round(new, 2))
