'''
constructor: It is a special method in a class that gets
invoked automatically when an object is created

def __init__(self):
    // statements

'''

class Employee:

    def __init__(self, name , age):
        self.n = name
        self.age = age
        # print("Calling the constructor: ", self)
    
    def getValues(self):
        print(f"Name is: {self.n} and age is : {self.age}")

e1 = Employee("Jane", 23)
e1.getValues()
e2 = Employee("Rahul", 34)
e2.getValues()