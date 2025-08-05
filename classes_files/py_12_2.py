# ---------------------------------------------
def fun_one(var):
    lst1 = []
    for ele in var:
        lst1 += [ele * 2]
    return lst1

lstOne = [10, 20, 30]
fun_one(lstOne)

# -----------------------------------------------
def fun_Two(var):
    lstTwo = []
    for i in var:
        if isinstance(i, int):
            lstTwo += [i * i]
        elif isinstance(i, list):
            lstFour = fun_Two(i)
            lstTwo += [lstFour]
    return lstTwo

lstTwo = [10, 20, [30, 40], 50, 60, [70, 80], 90]
two = fun_Two(lstTwo)
print(two)

lstTwo = [10, 20, [30, [1, 2, [10, 60], 3], 40], 50, 60, [70, [1, 4], 80], 90]
two = fun_Two(lstTwo)
print(two)
