Gun = ['Refile', 'ShotGun', 'Ar Gun', 'SMG Gun', 'Fist', 'Other', 'Glow Wall']
print(Gun)

print()
Gun.remove('Refile')
print(Gun)

print()
Gun.insert(0, 'Mini Gun')
print(Gun)

print()
Gun.append("Sniper")
print(Gun)

print()
n = len(Gun)
for i in range(n):
    for j in range(0, n-i-1):
        if Gun[j] > Gun[j+1]:
            Gun[j], Gun[j+1] = Gun[j+1], Gun[j]
print(Gun)

print()
# Gun = ['Ar Gun', 'Fist', 'Glow Wall', 'Mini Gun', 'Other', 'SMG Gun', 'ShotGun']
Ar_Gun = ['Scar', 'Ak', 'Woodpeker', 'Svd', 'Famas']
Fist = ['Katana', 'Punch', 'Bat', 'Knife']
Glow_Wall = ['Boom', 'Flash', 'Smoke']
Mini_Gun = ['Mini Ug', 'USP', 'G18', 'Desert']
Other = ['Not Use Gun', 'XBoo']
SMG_Gun = ['Ump', 'Mp40', 'P90', 'Mp5', 'Vector', 'Thomson']
ShotGun = ['M1014', 'M1887', 'Mag7']
Sniper = ['Awm', 'Kar98', 'M82b']

Gun_2 = [Ar_Gun, Fist, Glow_Wall, Mini_Gun, Other, SMG_Gun, ShotGun, Sniper]

st_1 = []
for i in range(0, len(Gun_2)):
    lst_1 = []
    j = Gun_2[i]
    for k in j:
        lst_1 += [k]
    st_1 += [[Gun[i]] + ["-"] + lst_1]
print(st_1)

print()
s = []
for i in st_1:
    s += (i[2:])
print(s)

print()
n = len(s)
for i in range(n):
    for j in range(0, n-i-1):
        if s[j] > s[j+1]:
            s[j], s[j+1] = s[j+1], s[j]
print(s)


