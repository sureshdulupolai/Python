# calling functions and methods 
def printit():                          # function
    print('Opener')

class Message():
    def display(self, msg):             # instance method with argument
        printit()                       # call to the function outside class
        print(msg)

    def show():                         # class method
        printit()                       # call to the function ouside class
        print("Hello")
        # display()                     # cannot call other method within the same class

printit()                               
m = Message()                           # an instance of the class is created 
m.display("Good Morning")               # calling the instance method of the class using the object of the class
Message.show()                          # calling the class method of the class using the name of the class