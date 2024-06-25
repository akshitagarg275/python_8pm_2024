# Functions

'''
syntax:

def functionName():
    //function statements
'''
# function defination
def greet():
    print("Hello")


# function calling
# greet()
# greet()

# TODO: funtion with parameters

def greet(name): 
    print(f"Hello, {name}")

# greet("John")

# fname = "Jane"
# greet(fname)


def calc(num1, num2):
    sum = num1 + num2
    print(f"sum is: {sum}")

# calc(2, 6)

# TODO: return 

def calc(num1,num2):
    sum = num1 + num2
    sub = num2 - num1
    return sum, sub
    # NOTE: unreachable code
    # print("Hello")

# ans = calc(4,5)
# print(ans)

# print(calc(7,8))

# ans1 , ans2 = calc(3,6)
# print("Sum is: ", ans1)
# print("Sub is: ", ans2)

# TODO: default parameters
# NOTE: non-default arguments(manadatory) should be followed by the default arguments
def profile(name = "NA", age = "NA"):
    print(f"Name is : {name} and age is : {age}")

# profile("John", 23)
# profile("Jane")
# profile()

# TODO: keyword parameters
def profile(name, age):
    print(f"Name is : {name} and age is: {age}")

# profile(age = 23, name = "Jane")

# TODO: variable length parameters

def func(a,b, *args):
    print("value in a: ",a)
    print("value in b: ", b)
    # print(args)
    # print(type(args))
    for i in args:
        print(i)

# func(1,2,3,4,5,6)
# func()

# TODO: variable length keyword parameters
def key_func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for k,v in kwargs.items():
        print(f"key is: {k} and value is: {v}")

# key_func(fname = "Jane", lname = "Doe", age = 23)

# TODO: Lambda functions
# anonymous functions
'''
lambda parameters: return
'''

# def sum(a,b):
#     return a+b


# sum = lambda a,b: a+b
# print(sum(4,5))

even = lambda num : num%2 == 0

# print(even(41))

# check = lambda num : f"Number {num} is even" if num%2 == 0 else f"Number {num} is odd"

# print(check(45))
# print(check(22))

result = lambda x,y : f"{x} is smaller than {y}" if x<y else (f"{x} is greater than {y}" if x >y else f"{x} is equal to {y}")
# print(result(4,5))
# print(result(3,2))
# print(result(1,1))


# TODO: usage of Lamda functions

# TODO: map -> creating a new list on the basis of the condition

nums = [1,2,3,4,5,6,7]

# squares = list(map(lambda num : num **2 , nums))

# print(squares)

# TODO: filter-> filtering out the values

# even = list(filter(lambda num : num%2 == 0, nums))
# print(even)


# TODO: reduce
from functools import reduce

sum = reduce(lambda x,y : x+y, nums)
print(sum)