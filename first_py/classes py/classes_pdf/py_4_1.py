# split (Convert data into list form)
# array and tuple are immutable (Can't change the value)
# ------------------------------------------- 
# different type of split use
# by default it value is (" ")
s = "I am a Superman"
t = s.split()
# now changes found in s
print(s)
print(t)

# now we can point (".") a full stop
s = "I am a Superman"
t = s.split(".")
print(t)

# 
u = "I am a Legend".split(" ")
print(u)

# 
print("I am the hero".split(" "))

# # 
# print(input("Enter a statment : ").split(" "))

# --------------------------------
# join function 
# what ever use inside in (" ") it wil print after every character except last character
s = "Hello"
t = ".".join(s)
print(t)

# --------------------------
msg_1 = "He said, Let us Python"
print(msg_1)

msg_2 = "He said, 'Let us Python'"
print(msg_2)

msg_3 = 'He said, "Let us Python"'
print(msg_3)

msg_4 = "He said, \"Let us Python\""
print(msg_4)

msg_5 = 'He said, \'Let us Python\''
print(msg_5)

# 3 inverted coma use for space character in source code
msg_6 = """

    Well This is Python!
        for You!!!

"""
print(msg_6)

msg_7 = '''

    Well This is Python!
        for You!!!

'''
print(msg_7)

# -5 -4 -3 -2 -1                                index position 
#  H  e  l  l  o                                 
#  0  1  2  3  4                                index position 

strg = "Hello"
# start, end, steps 
# use only one this if positive aur negative
# searching a perticular point
print(strg[1])
print(strg[1:3])
print(strg[1:4])
print(strg[1:5])
print(strg[1:])
print(strg[:3])
print(strg[:])
# by default value is 1 for step
print(strg[1:4:1])
# reverce
print(strg[4:1:-1])
print(strg[4:1:-2])
print()
print(strg[1:3:3])
print(strg[-4:-2])
print(strg[1:-2])
# print all from 2 index
print(strg[2:100])
# do not print because, 100 index value is does not exist in variable strg
# print(strg[100])

# --------------------------------
# string is immutable
stg_1 = "Pyhton"
stg_1 = "Cython"

# cant change a value in string
# stg_1[1] = 'g'

# ---------------------------------
# string replication
print('s ' * 10)

# --------------------------------
# string concatenation
print('I' + ' ' + 'Love' + ' ' + 'Pyhton')

# -------------------------------------
# search operator
print('e' in 'hello')
print('el' in 'hello')
print('ll' in 'hello')
print('llo' in 'hello')
print('lol' in 'hello')

# -------------------------------------
# built-in function
# calculation according to ascii value (\x65 start for capital letter) (\x91 start for small letter)  
stg_2 = "Jython"
print(len(stg_2))
print(min(stg_2))
print(max(stg_2))