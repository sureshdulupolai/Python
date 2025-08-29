# categories of string methods

stg_1 = 'Hello'
stg_2 = '12345'
stg_3 = 'He123'
stg_l = 'pyhton'
stg_u = 'PYTHON'
string_w_1 = '  hello   '
string_w_2 = ' hello '
stg_4 = 'l love pyhton'
stg_5 = ' i love pyhton'
s = '_'

# isalpha() > checks if all the characters in a string are alphabets
print(stg_1.isalpha())
print(stg_2.isalpha())
print(stg_3.isalpha())

# isdigit() > checks if all the characters in a string are digits
print(stg_1.isdigit())
print(stg_2.isdigit())
print(stg_3.isdigit())

# isalnum() > checks if all character in a string are either alphabets or digits
# it does not involve special characters
print(stg_1.isalnum())
print(stg_2.isalnum())
print(stg_3.isalnum())

# islower() > check all the character in the string are lowercase alphabets
# isupper() > check all the character in the string are uppercase alphabets
