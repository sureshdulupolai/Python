# string conversions 
# every time we use any function then it create new object
stg_1 = 'hello'
stg_2 = "HELLO"
stg_3 = "HeLLo"
stg_4 = "Hello World"
stg_5 = 'hello world'
stg_6 = "HELLO WORLD"

# upper() > coverts strings to upper case 
print(stg_1.upper())
print(stg_3.upper())

# lower() > convert strings to lower case 
print(stg_2.lower())
print(stg_3.lower())

# capitalize() > converts "only the first character of the string to uppercase"
print(stg_1.capitalize())

# -------------------------------------------------------------------
# title() > converts the first character of every ward to uppercase
print(stg_5.title())
# inthis case : if all character is capital letter then 
# convert into first letter only capital all other become small letter
print(stg_6.title())
print(stg_3.title())

print()
# ----------------------------------------------------
# swapcase() > swap cases in the string
# big char become small & small char become big
print(stg_3.swapcase())

# ----------------------------------
# example [hello world] to [Hello World]
# stg_5 = 'hello world'
var_one = stg_5.split(' ')
print(var_one)

var_two = var_one[0].capitalize()
print(var_two)

var_three = var_one[1].capitalize()
print(var_three)

var_four = var_two + ' ' + var_three
print(var_four)
