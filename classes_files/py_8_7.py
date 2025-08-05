# using buil-in functions on tuple 

t = (12, 15, 13, 23, 22, 16, 17)

# len(t)
# max(t)
# min(t)
# sum(t)
# any(all)
# all(t)
# sorted(t)
# sorted(t, reverse=True)       -- creating new object that why it's work in tuple, tuple is immutable that why .sort() method also not work in tuple because sort() method chnage inside tuple only and it cant possible in tuple



# doesn't Work
# -----------------------------------------
# method are ment to update the element within an array. sein tuple is immutable.
# The element within a tuple cannot be change or or not ment to be changed. 
# also the above method not associated with the tuple datatype of the class.
# hence, the given method don't work with tuples and can work only with mutable array data type like list.
# .append()  
# .insert()
# .remove()
# .pop()
# .sort()

# ----------------------------------------
# tuple methods

tpl = (17, 15, 13, 23, 22, 45, 74, 22)
print(tpl.count(23))
print(tpl.index(22))

for i,j  in enumerate(tpl):
    if j == 22:
        print(i)        # print(j,i)



