'''
first class objects : Function can be used or passed as arguments

'''

def upperCasing(text):
    return text.upper()

# print(upperCasing("hello"))

# func = upperCasing
# print(func)
# print(type(func))

# print(func("python"))


# TODO: passing function as methods
def upperCasing(text):
    return text.upper()

def lowerCasing(text):
    return text.lower()

def greet(func):
    greeting = func("Good morning")
    print(greeting)

# greet(upperCasing)
# greet(lowerCasing)


# TODO: returning function from another function

def adder(x):
    def add(y):
        return x + y
    
    return add

# add_15 = adder(15)
# print(add_15(10))

# TODO: decorator

def outer(func):
    def inner():
        print("****************")
        func()
        print("***************")
    return inner
@outer
def funcToBeExecuted():
    print("Python is a PL")

funcToBeExecuted()

# res = outer(funcToBeExecuted)
# res()