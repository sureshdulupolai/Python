# looping in sets

s = {12, 15, 13, 23, 22, 16, 17}
print(s)

# note :
# iteration is done over the accessing order of a set
# the index position return is not from the set, but the enumerate function
for ind, ele in enumerate(s):
    print(ind, ele)


# example :
# --------------------------------------------------------------------------
t = []
for i,j in enumerate(s):
    d = ()
    for ind in range(1):
        d += (i, j)
    t += [d]
print(t)

