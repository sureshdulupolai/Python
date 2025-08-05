a = 10
b = 20
c = 30

var = globals()     # as dictionary form
print(var)

# accessing a value and change the value of accessable value
var['a'] = 50
var['b'] = 70
var['c'] = 90

print(var)      # change in same global variable beacuse, it reffering to same obj of global (shallow copy)
print(a, b, c)
