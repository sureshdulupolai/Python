# multiple inheritance

class Parent1:
    def __init__(self):
        self.name = "John"

class Parent2():
    def __init__(self):
        self.age = 24

class Child(Parent1, Parent2):
    def __init__(self):
        self.prof = "Banker"
        Parent1.__init__(self)
        Parent2.__init__(self)

        # by defult it will call to first one only and this method does'nt use in this, it's good for one parent child connect
        # user super().__init__()
        # user super().__init__()           

    def display(self):
        print(self.name, self.age, self.prof)

objc = Child()
objc.display()