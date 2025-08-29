tpl_One = ((1,2,3),
           (4,5,6),
           (7,8,9))
for i in tpl_One:
    print(i)

print()
s = []
for i in range(len(tpl_One)):
    for j in range(2, -1, -1):
        if j <= (len(tpl_One) - 1):
            s += ([tpl_One[i][j]])
u = []
for p in range(len(tpl_One)):
    y = p
    v = []
    for t,q in enumerate(s):
        if t == y:
            v += [q]
            y += 3
    u += v
h1 = 0
f1 = []
for i1 in range(len(tpl_One)):
    d1 = []
    for s1 in range(len(tpl_One)):
        d1 += [u[h1]]
        h1 += 1
    f1 += [d1]
for o1 in f1:
    print(tuple(o1))
        
