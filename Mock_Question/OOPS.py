# Inheritance - One class inherits properties/methods from another.
class Parent:
    def speak(self):
        print("I am Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

c = Child()
c.speak()  # Inherited


# Encapsulation - Hide internal details using private or protected variables.
class Person:
    def __init__(self):
        self.name = "Suresh"         # public
        self._college = "PDTC"       # protected
        self.__age = 22              # private

    def show(self):
        print(self.__age)  # allowed inside class

p = Person()
print(p.name)        # OK
print(p._college)    # Not recommended (protected)
# print(p.__age)     # Error (private)


# Operator Overloading - Use operators like +, - with objects.
class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

p1 = Point(10)
p2 = Point(20)
print(p1 + p2)  # Output: 30


# Function Overloading - Python does not support directly, use default arguments
class Demo:
    def greet(self, name=None):
        if name:
            print("Hello", name)
        else:
            print("Hello")

d = Demo()
d.greet()           # Hello
d.greet("Suresh")   # Hello Suresh


# Polymorphism - Same method, different behaviors depending on object type.
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for animal in (Cat(), Dog()):
    animal.sound()



# Inheritance: Code reuse from parent to child.
# Encapsulation: Hides sensitive data.
# Operator Overloading: Re-define operators for objects.
# Function Overloading: Same function with different input (via defaults).
# Polymorphism: One interface, many implementations.


# ----------------------------------------------------------------------------------------------------------
# ✅ Single Inheritance (A → B)
class A:
    def showA(self):
        print("Class A")

class B(A):  # inherits A
    def showB(self):
        print("Class B")


# ✅ Multiple Inheritance (A + C → D)
class C:
    def showC(self):
        print("Class C")

class D(A, C):  # inherits A and C
    def showD(self):
        print("Class D")


# ✅ Multilevel Inheritance (A → E → F)
class E(A):  # child of A
    def showE(self):
        print("Class E")

class F(E):  # child of E
    def showF(self):
        print("Class F")


# ✅ Hierarchical Inheritance (A → G and A → H)
class G(A):  # another child of A
    def showG(self):
        print("Class G")

class H(A):  # another child of A
    def showH(self):
        print("Class H")


# ✅ Hybrid Inheritance (A + C → I → J)
class I(A, C):  # Multiple inheritance
    def showI(self):
        print("Class I")

class J(I):  # Multilevel + multiple = hybrid
    def showJ(self):
        print("Class J")

# Testing the classes
print("➡ Single Inheritance:")
b = B()
b.showA()
b.showB()

print("\n➡ Multiple Inheritance:")
d = D()
d.showA()
d.showC()
d.showD()

print("\n➡ Multilevel Inheritance:")
f = F()
f.showA()
f.showE()
f.showF()

print("\n➡ Hierarchical Inheritance:")
g = G()
g.showA()
g.showG()
h = H()
h.showA()
h.showH()

print("\n➡ Hybrid Inheritance:")
j = J()
j.showA()
j.showC()
j.showI()
j.showJ()
