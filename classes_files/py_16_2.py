# Multi-Level Inheritance

class Parent():
    def __init__(self):         # constructor
        self.name = "Thamos"

class Child(Parent):
    def __init__(self):         # constructor
        self.age = 25
        Parent.__init__(self)
    
class GrandChild(Child):
    # data inside the instance can only be put by the constructor( obj(valueOne, valueTwo) ) or the initializer method ( obj.functionName(valueOne, valuetwo) )
    def __init__(self):         # constructor
        self.prof = "Banker"
        super().__init__()

    def display(self):
        print(self.name, self.age, self.prof)

# This will only create the address ( instance ) i.e. n empty memory location
# after that it willl search for the __init__ function ( constructor )
# if the constructor is not found it will return back
# but will not go to any of the other methods inside the class
obj_gc = GrandChild()       

# methods inside the class can only be called using the object ( instance ) of the class
# objects ( instance ) carry the address .i.e. the memory space
obj_gc.display()


# -------------------------------------------------------------

class Parent():
    def __init__(self, n=""):         
        self.name = n

class Child(Parent):
    def __init__(self, n="", a=18):         
        self.age = a
        Parent.__init__(self, n)
    
class GrandChild(Child):
    def __init__(self, n="", a=18, p=""):         
        self.prof = p
        super().__init__(n, a)

    def display(self):
        print(self.name, self.age, self.prof)

# variable name or object name was same then also it work, because the address is different
obj_gc = GrandChild(n="Suresh", a=18, p="Developer") 
obj_gc.display()

obj_gc = GrandChild() 
obj_gc.display()    # empytSting Space for "Name", by Default age = 18, emptyString Space for "Prof"

obj_gc = GrandChild("Ramesh", 40, "Developer") 
obj_gc.display()