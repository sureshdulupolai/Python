# single inheritance

# example 1:
# -----------------------------------------------------------------------------------

class Parent():
    def __init__(self, n):
        self.name = n

class Child(Parent):        # child address only created but parent take data of child and process it and send to same data
    # display is method of the class
    def display(self):
        print(self.name)

obj = Child("John")             # this is where the object is getting created
obj.display()                   # we are using the object to call the method of the class

# note:- 
# a constructor is called only when an instance is created
# a method of the class can only be called by the object of class

print()
# example 2:
# -----------------------------------------------------------------------------------

class Parent():
    def __init__(self):
        self.name = "Thomas"

class Child(Parent):
    def __init__(self, a):
        self.age = a
        # Parent.__init__(self)
        super().__init__()

    def display(self):
        print(self.name, self.age)

obj1 = Child(27)
obj1.display()
