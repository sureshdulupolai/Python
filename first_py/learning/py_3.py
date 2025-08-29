# take input from user for 2 person (angry aur no angry)
# if both are angry then you are in trouble
# if both are angry then you are in trouble, one person is angry then it ok you are not in trouble

person_one = input("First Person Angry Or Not Angry :").lower()
person_two = input("Second Person Is Angry Or Not Angry : ").lower()

if (person_one == 'angry') :
    if (person_two == 'angry'):
        print("You Are in Trouble, Because Both Are Angry")
    if (person_two == 'not angry') or (person_two == 'notangry'):
        print("You Are not in Trouble, Because Both Are Not Angry")

if ((person_one == 'not angry') and (person_two == 'angry')):
    print("You Are not in Trouble, Because Both Are Not Angry")

else:
    print("You Have Enter Something Wrong")

