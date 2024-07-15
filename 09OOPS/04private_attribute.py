class Employee:
    company = "ABC"

    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def profile(self):
        print(f"name is : {self.__name} and age is: {self.age}")
    
e1 = Employee("John", 23)
e1.profile()

e1.__name = "Sam"
# e1.profile()