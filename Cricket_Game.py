import random
def hit(a):
    if a == 1:
        print("{} Run".format(1)); return 1
    elif a == 2:
        print("{} Run".format(2)); return 2
    elif a == 3:
        print("{} Run".format(3)); return 3
    elif a == 4:
        print("{} Run".format(4)); return 4
    elif a == 5:
        print("{} Run".format(5)); return 5
    elif a == 6:
        print("{} Run".format(6)); return 6
    elif a == 7:
        print("{} + 1 Run".format("Wide Ball")); print(); ball(); return 1
    elif a == 8:
        print("{}".format("Dot Ball")); return 0
    elif a == 9:
        print("{} + 0 Run, Extra 1 Ball".format("No ball")); print(); ball(); return 0
    elif a == 10:
        print("{}".format("0 Run LegBy")); return 0

def ball():
    global lst
    userBall = input("Enter Your Ball Speed : "); a = random.randint(1, 10); var1 = hit(a); lst += [var1]

def ComputerSideBat():
    b = 7; computerHit = 0
    for i in range(1, b):
        ball(); print()
    print("\n---: Printing 1 Over Runs :---")
    for ind, ele in enumerate(lst):
        if ind <= 9:
            print("""         {} Ball - {} Run""".format((ind + 1), ele))
        else:
            print("""        {} Ball - {} Run""".format((ind + 1), ele))
        computerHit += ele
    print("Total Run Hit By Computer is '{}'".format(computerHit))
    return computerHit

# -------------------------------------------------------------------------------

def batHit(a):
    if a == 2:
        var1 = 2
    elif a == 3:
        var1 = 3
    elif a == 4:
        var1 = 4
    elif a == 5:
        var1 = 5
    return var1

def conditions(a):
    if a == False:
        return "Wicket"
    if a == 2:
        return "Wide Ball"
    if a == 3:
        return "Normal"
    if a == 4:
        return "Bouncer"
    if a == 5:
        return "Yourker"

def bat():
    a2 = random.randint(1, 5)
    if a2 != 1:
        var1 = batHit(a2)
        return var1
    else:
        return False

def dotBallMoveOne(userEnterValueBatOne, dsValue):
    global lst1
    print("Your Move - {} , Ball On {}".format(userEnterValueBatOne, conditions(dsValue)))
    if userEnterValueBatOne == "3" or userEnterValueBatOne in "dot":
        print("But You Are Safe And Run : 0")

    elif userEnterValueBatOne == "4" or userEnterValueBatOne in "softplay":
        run1 = random.randint(1, 2)
        print("This Ball Run : {}".format(run1))
        lst1 += [run1]

def dotBallMoveTwo(userEnterValueBatOne, dsValue):
    global lst1
    if userEnterValueBatOne == "3" or userEnterValueBatOne in "dot":
        print('Your Move is : {}, On "{}" Ball'.format(userEnterValueBatOne, conditions(dsValue)))
        print("This Ball Run : {}".format(0))
        lst1 += [0]
    
    elif userEnterValueBatOne == "4" or userEnterValueBatOne in "softplay":
        run1 = random.randint(1, 4)
        print('Your Move is : {}, On "{}" Ball'.format(userEnterValueBatOne, conditions(dsValue)))
        print("This Ball Run : {}".format(run1))
        lst1 += [run1]


def moves():
    print("Your Move - {}, on {}!".format(userEnterValueBatOne, conditions(dsValue)))

def wicketMove(dsvalue):
    if (dsValue == 4 or dsValue == 5 or dsValue == False):
        moves(); print("You are Out!"); print()
        global lst1
        lst1 += [0]
        return 0

def dsValue2():
    moves(); print("This Ball Run : 1"); print()
    global lst1
    lst1 += [1]

def dsValue3():
    if userEnterValueBatOne == "1" or userEnterValueBatOne in "superhit":
        a1 = 4; b1 = 6
    else:
        a1 = 2; b1 = 4
    r1 = random.randint(a1,b1); moves(); print("This Ball Run : {}".format(r1)); print()
    global lst1
    lst1 += [r1]

def superHit_Hit(dsvalue):
    if dsValue == 2:
        dsValue2()
    elif dsValue == 3:
        dsValue3()

def youHit(lst1):
    x2 = 0
    for x1 in lst1:
        x2 += x1
    print('You Have Score Total : {}'.format(x2))
    return x2

def scoreBorad(a, b):
    c1 = a - b
    if a > b:
        print("You have Lost The Game! By {} Run's".format(c1))
        print("Opponent Score : {}".format(a))
    elif a == b:
        print("Match Was Tie!")
    elif a < b:
        print("You Win The Game!")
    
# --------------------------------------------------------------------------------       
 
lst = []; lst1 = []
userEnterValue = input("Enter To Choose Bat or Ball: ").lower()
if (userEnterValue == "ball"):
    var1 = ComputerSideBat()
    # -------------------------------------
    # time to bat
    print("\n---: Now Your Time To Bat :---")
    b1 = 1; b3 = 0
    while len(lst1) <= 6:
        userEnterValueBatOne = input("What is Your {} Hit Will be - ( PowerHit, Hit, Dot, Softplay ) : ".format(b1)).lower()
        b1 += 1; dsValue = bat()
        if (userEnterValueBatOne == "1" or userEnterValueBatOne in "powerhit") or (userEnterValueBatOne == "2" or userEnterValueBatOne in "hit"):
            var = wicketMove(dsValue)
            if var == 0:
                break
            superHit_Hit(dsValue)
            
        elif (userEnterValueBatOne == "3" or userEnterValueBatOne in "dot") or (userEnterValueBatOne == "4" or userEnterValueBatOne in "softplay"):
            if dsValue == False:
                dotBallMoveOne(userEnterValueBatOne, dsValue); print()
            else:
                dotBallMoveTwo(userEnterValueBatOne, dsValue); print()

        else:
            print("Choose Your Move Correctly Between ( PowerHit, Hit, Dot, Softplay ), Only!!!")
            print()
    y1 = youHit(lst1)
    scoreBorad(var1, y1)

elif (userEnterValue == "bat"):
    b1 = 1; b3 = 0
    while len(lst1) <= 6:
        userEnterValueBatOne = input("What is Your {} Hit Will be - ( PowerHit, Hit, Dot, Softplay ) : ".format(b1)).lower()
        b1 += 1; dsValue = bat()
        if (userEnterValueBatOne == "1" or userEnterValueBatOne in "powerhit") or (userEnterValueBatOne == "2" or userEnterValueBatOne in "hit"):
            var = wicketMove()
            if var == 0:
                break
            superHit_Hit()
            
        elif (userEnterValueBatOne == "3" or userEnterValueBatOne in "dot") or (userEnterValueBatOne == "4" or userEnterValueBatOne in "softplay"):
            if dsValue == False:
                dotBallMoveOne(); print()
            else:
                dotBallMoveTwo(); print()

        else:
            print("Choose Your Move Correctly Between ( PowerHit, Hit, Dot, Softplay ), Only!!!")
            print()
    print("Now Your Time To Ball")
    var1 = ComputerSideBat()
    y1 = youHit(lst1)
    scoreBorad(var1, y1)

else:
    print('Not match Choose Your Move Correctly Between ( Bat & Ball ), Only!!!')