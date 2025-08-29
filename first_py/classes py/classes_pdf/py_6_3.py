s = "Mumbai"
tpl = (10, 20, 30, 40, 50, 60)

c = 0
while c < 6:
    print(s[c])
    c += 1

# sum of all ascii value of Mumbai 
c = 0
total = 0
while c < 6:
    a = ord(s[c])
    total += a
    c += 1
print(total)

lst = ['desert','dessert','to','too','lose','loose']
c = 0 
# len(list) = 6
while c < len(lst):
    d = (lst[c])
    # print(d)
    e = 0
    while e < len(d):
        print(d[e])
        e += 1
    c += 1
    print()

