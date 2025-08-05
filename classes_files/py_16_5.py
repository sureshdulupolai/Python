# encapultion
# -----------------------------------------------------------------------

class Parent():
    def __init__(self):
        self.__name = "John"            # private
        self._age = 27                  # Proctected - not suppoted in py (this is also acting like public only)
        self.prof = "banker"            # public

    def display(self):
        print(self.__name, self._age, self.prof)

class child(Parent):
    def display(self):
        print(self.__name, self._age, self.prof)
        # print(self._age, self.prof)   # run code because private member is not printing

# Private Value Can be accessable by object of the parent class only
# c1 = child()
# why does'nt work is "child" is public for ( __name ) private variable
# but,
# b1 = parent()
# use only - b1.display()
# don't use print(b1.__name)
# this also not work because it was in public space aur global space public area

c1 = Parent()
c1.display()