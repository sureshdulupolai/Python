# Accept the gender from the user as char and print the respective greeting message
# "Good Morning Sir" (On the basis of gender)

value_one = input("Enter Your Gender : ").lower()
if value_one == "male":
    print("Good Morning Sir")
elif value_one =="female":
    print("Good Morning Ma'am")
else:
    print("You Are Not Conform About Your Gender I think so")