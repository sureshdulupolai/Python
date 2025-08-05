# --------------------------------------------------------------
def cal_sum_prod(x, y, z):
    ss = x + y + z
    pp = x * y * z
    return ss, pp 

tpl = cal_sum_prod(10, 20, 30)
print(tpl)

s, p = cal_sum_prod(10, 20, 30)
print(tpl)