lst = ["krishpolai@gmail.com", "akashsahu@gmail.com", "pritam@gmail.com", "ashish@gmail.com"]
a = input("Enter a Name :").strip().split(" ")
number = int(input("{} Please Enter Your Mobile No : ".format(a[0].title()))).is_integer()
if number.is_integer():
    gmail = input("Enter Your Gmail {} : ".format(a[0])).lower()
else: 
    print("Fill Your No Correct")
if "@gmail.com" in gmail:
    # login
    if gmail in lst:
        print("Successful Connection")
    # signup
    else:
        print("You Are Not Register To Your Website \
You Need To Verify First")
else:
    print(gmail + "@gmail.com")
    # login
    if gmail in lst:
        print("SuccessFull Connection Now")
    # signup
    else:
        print("You Are Not Register To Your Website \
You Need To Verify First !!!")