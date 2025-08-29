# accept an english alphabet from user and check if it is a consonant or a vowel
var_one = input("Enter a Letter to check string first character is vowel aur consonant : ")
var_two = " ".join(var_one).lower()
var_three = var_two[0]
# print(var_two[0])
vowel = 'a','e','i','o','u'
consonant = 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'
if var_three in vowel:
    print("Vowel Letter")
    print("Your Input : {}".format(var_one))

elif var_three in consonant:
    print("Consonant Letter")
    print("Your Input : {}".format(var_one))

else:
    print("Enter Only letter")
    print("Your Input : {}".format(var_one))