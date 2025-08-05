def cal_sum_one(x = 10, y = 20):
    return x + y 

print(cal_sum_one)
print(cal_sum_one())
print(cal_sum_one(x = 100))
print(cal_sum_one(y = 300))
print(cal_sum_one(25, y = 300))
print(cal_sum_one(25, 35))
print(cal_sum_one(2+5, 3*5))
print(cal_sum_one([10, 20], [30, 40]))
print(cal_sum_one((10, 20), (30, 40)))
print(cal_sum_one(y = 300, x = 50))
# print(cal_sum_one(y = 300, 25))

# -----------------------------------------------------------------------
def cal_prod_one(x, y = 5, z = 7):
    return x * y * z

print(cal_prod_one(5, 6, 7))
print(cal_prod_one(5, z = 6, y = 7))
print(cal_prod_one(2, 4))