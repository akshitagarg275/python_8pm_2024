'''
static method
We do not need to write the self keyword
'''

class Employee:

    @staticmethod
    def greet():
        print("Hello")

e1 = Employee()
e2 = Employee()
# e1.greet()
# e2.greet() 

Employee.greet()   

