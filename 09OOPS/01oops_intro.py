'''
OOPS : Object Oriented Programming System

class -> It is the blueprint
object -> It is the real world entity

class -> attributes (variables) and methods (functions)

4 pillars of OOPS:

abstraction -> hiding unneccesaary info

encapsulation -> encapsulates attributes and the methods altogether

inheritance -> parent (super) -> child (dervied) relation

polymorphism -> Poly(many) + morphs (forms)
2 + 2 = 4
'2' + '2' = 22

memory is allocates at the time of object creation

'''

class Example:
    pass

# obj = Example()
# print(obj)
# print(type(obj))


class Employee:
    # class attribute
    company = "ABC"

    def greet(self):
        print("Welcome here!!!")

e1 = Employee()
e1.greet()
# print(e1.company)

e2 = Employee()
e2.greet()

e2.company = "Google"
# modified the class attribute using class name
Employee.company = "XYZ"
print("e1: ", e1.company)
print("e2: ",e2.company)


e3 = Employee()
print("e3: ", e3.company)