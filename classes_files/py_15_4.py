# object initialization
# ----------------------------------------------------

class Empolyee():
    # use in ( __init__ ) do not call to input data
    def __init__(self, n="", a=0, s=0.0):
        self.name = n
        self.age = a
        self.salary = s

    def display(self):
        print(self.name, self.age, self.salary)

    # run as after every code, as bye default
    # def __del__(self):
    #     print("Destructor is Exexuted!")


# calls the constructor function
e1 = Empolyee("Suresh", 23, 90000) 
e1.display()

# distroy the obj or delete the obj
e1 = None       # every time print destructor
# calls the destructor function
# e1.display()          
# delete obj doesn't have any attribute

e2 = Empolyee(n="Ramesh", s="20000")
e2.display()


# ---------------------------------------------------
# instance copy of obj address
# function defined within the class are called as method
# functions with instance as parameters are called as instance method 
# function defined with a class without any instance parameters or parameters are called as class method
# variables defined within the class methods are called as attributes