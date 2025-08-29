# write out a program two numbers input from user check wether both are negative aur positive

user_value_1 = float(input("Enter a value one to check wether both operator same or not : "))
user_value_2 = float(input("Enter a value two to check wether both operator same or not : "))
if ((user_value_1 <= -1) or (user_value_1 >= 0)):
    if user_value_1 <= -1:
        print('First Value Is Negative {}'.format(user_value_1))
    if user_value_1 >= 0:
        print('First Value Is Positive {}'.format(user_value_1))

        if user_value_2 <= -1:
            print("Second Value Is Negative {}".format(int(user_value_2)))
    
        if user_value_2 >= 0:
            print("Second Value Also Positive {}".format(int(user_value_2)))
