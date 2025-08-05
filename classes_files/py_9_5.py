# superset and subset

s = {12, 15, 13, 23, 22, 16, 17}
t = {13, 15, 22}

# a set is said to be a 'subset' of a 'superset' .
# only if all the element of a 'subset' are included in the system in the given 'superset'

print(s.issuperset(t))              # check if 's' is a superset of 't' = true
print(s.issubset(t))                # check if 's' is a subset of 't' = false
print(s.isdisjoint(t))              # check if the two sets are disjoint (connect to each other) = false


a = {1, 2, 3, 4, 5}
b = {2, 4, 5}

print(a > b)
print(a >= b)
print(b < a)
print(b <= a)

