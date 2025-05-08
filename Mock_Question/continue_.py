# 1 to 5, skip 3: continue

for no in range(1, 6):
    if no != 3:
        print(no)
    else:
        continue

# [10, 20, 30] > [100, 200, 300]

lst = [10, 20, 30]
for l1 in range(len(lst)):
    lst[l1] *= 10
print(lst)


# [[2, 4, 6], [3, 5, 7]] > [[4, 8, 12], [6, 10, 14]]

lst1 = [[2, 4, 6], [3, 5, 7]]

for l2 in lst1:
    if isinstance(l2, list):
        for l3 in range(len(l2)):
            l2[l3] *= 2
    else:
        continue

print(lst1)


try:
    userNumber = int(input('Enter a Number Between 1 to 20 : '))
    if (userNumber >= 1) and (userNumber <= 20):
        for Count in range(1, 21):
            if userNumber == Count:
                break
            else:
                print(Count)
    else:
        print('Enter No Between 1 to 20')
except:
    print("Enter Only Number's")


# local variable
def show():
    x = 10  # local variable
    print(x)
show()  # Output: 10

# global variable
x = 5  # global variable

def update():
    global x
    x = 20  # modifies global x
update()
print(x)  # Output: 20

# nonlocal variable
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20  # modifies x in outer()
    inner()
    print(x)
outer()  # Output: 20

# Local: Inside function, not visible outside.
# Global: Outside functions, visible everywhere.
# Nonlocal: In nested functions, modifies the outer (but not global) variable.


# ----------------------------------------------------------------------------------------
# File Handling 

# 'r' – Read (default)
# 'w' – Write (overwrite)
# 'a' – Append
# 'x' – Create
# 'rb' / 'wb' – Read/Write in binary mode

# Writing to a file
with open("data.txt", "w") as f:
    f.write("Hello Suresh!")

# Reading from a file
with open("data.txt", "r") as f:
    print(f.read())


# Exception Handling
try:
    # risky code
    pass
except ZeroDivisionError:
    # error handling
    pass
else:
    # runs if no error
    pass
finally:
    # always runs
    pass

# ------------------------------------------------------------------------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# super() function
class A:
    def show(self):
        print("Parent")

class B(A):
    def show(self):
        super().show()
        print("Child")

B().show()
# Output:
# Parent
# Child


# Method Overriding - When child class redefines a method of parent class.
class A:
    def show(self):
        print("A class")

class B(A):
    def show(self):
        print("B class")  # Overrides A's method


# Constructor Inheritance - Constructors (__init__) can also be inherited or overridden.
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

# --------------------------------------------------------------------------------------------