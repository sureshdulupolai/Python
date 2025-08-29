import math
Name = input("Enter Your Name : ")
std = int(input("You Are in Wich \"Class\" or \"std\": "))
User_Enter_1 = int(input("Enter your Fav Number : "))

# less part
New_in_1 = User_Enter_1 + 7
New_in_2 = User_Enter_1 + 3 
New_in_3 = User_Enter_1 - 2

# price 
p_1 = 1000
p_2 = 5000
p_3 = 10000
p_4 = 50000
p_5 = 100000

if std <= 10 and std >= 1:
    print("Welcome To 'Math Quiz'")
    print()
    print("This Game Price Pool : {}".format(p_1))
    print()
    c = int(math.sqrt(New_in_1))
    a = c - 3
    b = c + 5
    d = c + 2
    print("1. What is the square root of : {}".format(New_in_1))
    print("1. {}".format(a))
    print("2. {}".format(b))
    print("3. {}".format(c))
    print("4. {}".format(d))
    e = int(input("Inter Your Option No : "))
    if c == e:
        print("Conratulation You Have Won {}".format(p_1))
        print()
        print("This Game Price Pool : {}".format(p_2))
        print()
        c = int(math.exp(New_in_3))
        a = c - 3
        b = c + 5
        d = c + 2
        print("2. What is Exponential of : {}".format(New_in_3))
        print("1. {}".format(c))
        print("2. {}".format(d))
        print("3. {}".format(a))
        print("4. {}".format(b))
        e = int(input("Inter Your Option No : "))
        if c == e:
            print("Conratulation You Have Won {}".format(p_2))
            print()
            print("This Game Price Pool : {}".format(p_3))
            print()
            c = 5902.5
            a = c - 3
            b = c + 5
            d = c + 2
            print("3. What is the Total of : 25 / 2 + 2356 / 2 * 5")
            print("1. {}".format(a))
            print("2. {}".format(c))
            print("3. {}".format(b))
            print("4. {}".format(d))
            e = float(input("Inter Your Option No : "))
            if c == e:
                print("Conratulation You Have Won {}".format(p_3))
                print()
                print("This Game Price Pool : {}".format(p_4))
                print()
                c = int(math.factorial(New_in_3))
                a = c - 3
                b = c + 5
                d = c + 2
                print("2. What is Exponential of : {}".format(New_in_3))
                print("1. {}".format(b))
                print("2. {}".format(d))
                print("3. {}".format(a))
                print("4. {}".format(c))
                e = int(input("Inter Your Option No : "))
                if c == e:
                    p = p_1 + p_2 + p_3 + p_4
                    print("{} You Have Won the match and Get price total {}".format(Name,p))
                else:
                    print("You Have Loss Match And You Only Get {}".format(p_3))
            else:
                print("You Have Loss Match And You Only Get {}".format(p_2))
        else:
            print("You Have Loss Match And You Only Get {}".format(p_1))
    else:
        print("You Have Choose Wrong Option & You Loss {}".format(p_1))

if std >= 11:
    print("Welcome To 'Math Quiz'")
    print()
    print("This Game Price Pool : {}".format(p_1))
    print()
    c = int(math.sqrt(New_in_1))
    
    print("1. What is the square root of : {}".format(New_in_1))
    print("1. {}".format(a))
    print("2. {}".format(b))
    print("3. {}".format(c))
    print("4. {}".format(d))
    e = int(input("Inter Your Option No : "))
    if c == e:
        print("Conratulation You Have Won {}".format(p_1))
        print()
        print("This Game Price Pool : {}".format(p_2))
        print()
        c = int(math.exp(New_in_3))
        a = c - 3
        b = c + 5
        d = c + 2
        print("2. What is Exponential of : {}".format(New_in_3))
        print("1. {}".format(c))
        print("2. {}".format(d))
        print("3. {}".format(a))
        print("4. {}".format(b))
        e = int(input("Inter Your Option No : "))
        if c == e:
            print("Conratulation You Have Won {}".format(p_2))
            print()
            print("This Game Price Pool : {}".format(p_3))
            print()
            c = 5902.5
            a = c - 3
            b = c + 5
            d = c + 2
            print("3. What is the Total of : 25 / 2 + 2356 / 2 * 5")
            print("1. {}".format(a))
            print("2. {}".format(c))
            print("3. {}".format(b))
            print("4. {}".format(d))
            e = float(input("Inter Your Option No : "))
            if c == e:
                print("Conratulation You Have Won {}".format(p_3))
                print()
                print("This Game Price Pool : {}".format(p_4))
                print()
                c = int(math.factorial(New_in_3))
                a = c - 3
                b = c + 5
                d = c + 2
                print("2. What is Exponential of : {}".format(New_in_3))
                print("1. {}".format(b))
                print("2. {}".format(d))
                print("3. {}".format(a))
                print("4. {}".format(c))
                e = int(input("Inter Your Option No : "))
                if c == e:
                    p = p_1 + p_2 + p_3 + p_4
                    print("{} You Have Won the match and Get price total {}".format(Name,p))
                else:
                    print("You Have Loss Match And You Only Get {}".format(p_3))
            else:
                print("You Have Loss Match And You Only Get {}".format(p_2))
        else:
            print("You Have Loss Match And You Only Get {}".format(p_1))
    else:
        print("You Have Choose Wrong Option & You Loss {}".format(p_1))

else:
    print("Invalid Age Enter")
    print("Enter Positive and Correct Age")