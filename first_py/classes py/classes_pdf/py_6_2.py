# initialization 
# condition
# incrementing & decrementing

print("Start")

count = 0  # statting from 

while count < 5:   # condition of end 
    print(count)
    count = count + 1     # increment & decrement

print('End')

# -----------------------------------------
# while & else 
# after while become false, it will come to else direct

print("Start")

count = 0 
while count < 5:
    print(count)
    count = count + 1

else:
    print(count)

# -----------------------------------------
# break : the while loop abruptly stopping the execution of the while loop
# when the while loop is stopped abruptly, the else block will not go to work
# the else block of the while loop goes to work only when the codition of the while loop becomes false naturally
# else statment cant work, while stop in true condition 

print("Start")

count = 0 
while count < 5:
    # print(count)         -- to print 0,1,2 and 3 also, after printing this it will break the while loop in true contition
    if count == 3:
        break
    print(count)
    count = count + 1

# else:                     -- not work
#     print(count)

# -----------------------------------------
# continue :
count = 0
while count < 5:
    if count == 3:
        # 3 + 1 = 4 will be the increment the value 
        # if we dont write this line then 3 run and check again and again
        # because after continue it will
        count = count + 1
        continue
    print(count)
    count = count + 1

else:
    print(count)

