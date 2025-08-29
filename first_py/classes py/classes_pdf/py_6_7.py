lst_1 = [10, 20, 30, 40, 50]
lst_2 = [10, 20, 3, 40, 50]
for i in lst_2:
    if i % 10 != 0:
        print("{} not Divisible by 10".format(i))
        break
else:
    print("divisible by 10")
