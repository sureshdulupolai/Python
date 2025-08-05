class Fruit:                        
    count = 0                           # class variable > initializes the class variable

    def __init__(self, n, a, s):        # constructor
        self.name = n                   # attribute                      
        self.age = a
        self.salary = s
        Fruit.count += 1                # incrementing of class variable

    def display(self):                  # instance method
        print(Fruit.count)

    def disp():                         # class method
        print("Hello World!")


f1 = Fruit("Apple", 5, "Green")
f1.display()                            # count = 1

f2 = Fruit("Orange", 7, "Magenta")
f2.display()                            # count = 2

# error because any address is not connected
# if address is not a parameter of function then class does not have attribute as that function
# the class method always be called as class method
# f2.disp()                             # error

# to class disp()
Fruit.disp()                