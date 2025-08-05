# access convention

class Employee():
    # set_data function is declare one's
    def set_data(self, n, a, s):
        self.name = n
        self.age = a
        self.salary = s

    # but this is operation you can do any operation multiple time
    def display_data(self):
        print(self.name, self.age, self.salary)

objOne = Employee()
objOne.name = "Suresh"
objOne.age = 22
objOne.salary = 70000
objOne.display_data()

# update data in same address
objOne.name = "Ramesh"
objOne.display_data()
