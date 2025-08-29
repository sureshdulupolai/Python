w_1 = input("Inside Your Company There is Any Worker, \
Working Currently, 'Yes Or No' : ").lower()
if (w_1 in "yes"):
    worker = (int(input("There Are How Many Worker In your Company : ")) + 1)
    w = 0
    for i in range(1,worker):
        w += int(input("Enter The Amount Of Your Worker {} : ".format(i)))
    print("This is Total Amount Of Workers : {}".format(w))

w_1 = input("Inside Your Company There is Any Worker ?, 'Yes Or No' : ").lower()
if (w_1 in "yes"):
    print()
    a = input("Enter Name Of Post Of Employee : ")
    a_2 = (int(input("There Are How Many {} In your Company : ".format(a))) + 1)
    a_1 = 0
    for i in range(1,a_2):
        a_1 += int(input("Enter The Amount Of Your Worker {} : ".format(i)))
    print("This is Total Amount Of {} : {}".format(a_1,w))

w_1 = input("Inside Your Company There is Any Worker ?, 'Yes Or No' : ").lower()
if (w_1 in "yes"):
    print()
    a = input("Enter Name Of Post Of Employee : ")
    b_2 = (int(input("There Are How Many {} In your Company : ".format(a))) + 1)
    b_1 = 0
    for i in range(1,b_2):
        b_1 += int(input("Enter The Amount Of Your Worker {} : ".format(i)))
    print("This is Total Amount Of {} : {}".format(b_1,w))

else:
    print("Hi")
print()
print("Total of {} + {} + {} : {}".format(w,a_1,b_1,w+a_1+b_1))