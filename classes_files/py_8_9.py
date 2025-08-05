# sorting a 'list of tuple'
# or tuple of lists

import operator
lst = [('abc', 24, 1.34), ('def', 25, 1.24)]
tpl = (['abc', 24, 1.34], ['def', 25, 1.24])

# compare one by one element if both are true, until you get true or false either less than and greater then value
print(sorted(lst))
print(sorted(tpl))

# not check every element only check element no 2
print(sorted(lst, key=operator.itemgetter(2)))
print(sorted(tpl, key=operator.itemgetter(2)))