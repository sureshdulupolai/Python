# hierarchial inheritance
# --------------------------------------------------------------------------------------------

class Parent():
    def __init__(self):
        self.name = 'John'
        self.age = 25
        self.prof = "Banker"

class Child1(Parent):
    def __init__(self):
        self.city = "New York"
        Parent.__init__(self)

    def display(self):
        print(self.name, self.age, self.city)

class Child2(Parent):
    def __init__(self):
        self.country = "US"
        Parent.__init__(self)

    def display(self):
        print(self.age, self.prof, self.country)

obj = Child2()
obj1 = Child1()
obj1.display()
obj.display()