class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.age = age
        self.salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, new_name):
        self.__name = new_name

e1 = Employee("John", 23, 50000)
# print(e1.name)

# e1.name = "Rats"

# print(e1.__name)

# print(e1.name)

e1.set_name = "Jacky"
print(e1.name)