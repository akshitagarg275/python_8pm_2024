'''
Inheritance

Base Class (Parent) ---> Derived Class (Child)
single Inheritance
Multiple Inheritance
Multilevel Inheritance

'''

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("Employee is working!!")
    
class Programmer(Employee):
    def __init__(self, name, age, language):
        self.language = language
        super().__init__(name,age)

    def work(self):
        print(f"I code in {self.language}")
        super().work()

e1 = Programmer("Jane", 23, "python")
e1.work()