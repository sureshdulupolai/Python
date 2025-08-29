
a = int(input("Enter a Hr Point : ")); b = int(input("Enter a Minute Point : ")); c = 0
for i in range(1,13,1):
    for j in range(1,61,1):
        if i == a and j == b:
            c = ("{}:{}".format(i,j)); break; 
if c:
    print(c)
else:
    print("The Number Is Not Exist In \"Indian Clock System\"")

# a = 1
# while a <= 12:
#     b = 1
#     while b <= 60: 
#         print("{}:{}".format(a,b)); b += 1
#     a += 1
