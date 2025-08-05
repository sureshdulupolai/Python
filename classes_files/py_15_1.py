# classes and object

class Employee():
    def set_data(self, n, a, s):
        self.name = n
        self.age = a
        self.salary = s

    def display(self):
        print(self.name, self.age, self.salary)

# ----------------------------------------------------------------
e1 = Employee()             # 123

# the instant method of the class can only be called using the object of the class
e1.set_data("Suresh", 22, 70000)
e1.display()

# ----------------------------------------------------------------
e2 = Employee()             # 456

# the instant method of the class can only be called using the object of the class
e2.set_data("Ramesh", 23, 80000)
e2.display()