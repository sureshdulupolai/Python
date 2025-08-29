# age is less then 18 you cant get a voter card
# age is 18 aur age is greater then 18 then you can get a voter card 
# for negative number print -- give a valid age
# elif (age < 18 and age > 0)

name = input("Enter Your Name :")
age = int(input("Enter Your Age : "))

if age > 18:
    print("You Can Get a Voter Card Now")

elif age < 18 and age > 0:
    print("You can get a voter card, because you are under asge for apply a voter card")
else:
    print("Enter Age is Not Your Actual Age")