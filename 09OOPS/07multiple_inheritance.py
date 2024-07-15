'''
Multiple Inheritance -> Child class will inherit from two parents

order of inheritance matters

MRO -> Method Resolution Order

'''

class Human:
    eyes = 2
    ears = 2

    def breathe(self):
        print("I can breathe!")
    
    def work(self):
        print("We should work!!")

class Employee:
    company = "ABC"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("Employee is working!!")

    def breathe(self):
        print("I try to breathe....")

class Programmer(Employee, Human):
    def __init__(self, name, age, language):
        self.language = language
        super().__init__(name,age)

    def work(self):
        print(f"I code in {self.language}")
        super().work()

    def breathe(self):
        super().breathe()

e1 = Programmer("Jane", 23, "python")
e1.work()
e1.breathe()