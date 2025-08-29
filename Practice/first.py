lst = []
def userDataInDict(p):
    for i in range(p):
        while True:
            userName = input("Enter Your Name: ").lower().split()
            if len(userName) > 0:
                if all(word.isalpha() for word in userName):
                    print("Your Name {} Added To Our App".format(userName))
                    lst.append(userName)
                    print()
                    break
                else:
                    print("Correct Your Name First {}, you have enter no aur special symbol that why i can't add your name".format(userName))
            else:
                print("Enter Correctly You Are Name, Check Your Name You Have enter : {}".format(userName))
    return lst
    
userDataInDict(
    int(input("Enter How Many Name Do You Need To Admit In : "))
)

for i in lst:
    print(*i, end=' ')
