# a number is said to be a prime number 
# if the number is divisible by itself 
# and if the number is not divisible by it's multiples

c = 10
for i in range(2,c):
    if c % i == 0:
        print("not a prime No")
        break
else:
    print("prime number")
        
# 
n = 5 
d = 2
while d < n -1:
    if n % d == 0:
        print("{} is not a prime number".format(n))
        break
    d += 1
else:
    print("{} is a prime no".format(n))

