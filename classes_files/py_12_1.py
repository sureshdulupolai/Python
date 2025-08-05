# example 1 
# ---------------------------------------------------------------------------
def refact(n):
    if n == 0:
        return 1
    else:
        p = n * refact(n - 1)
    return p

num = 5
factorial = refact(num)
print(factorial)