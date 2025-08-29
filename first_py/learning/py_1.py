# Even or Odd Number 
# Input Taking From User 

User_Value = int(input("Enter a Value To Check Where It is Even Or Odd : "))
if User_Value % 2 == 0:
    print("The Given Value is Even : {}".format(User_Value))
else:
    print("The Given Value is Odd : {}".format(User_Value))