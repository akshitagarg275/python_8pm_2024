# Functions

'''
syntax:

def functionName():
    //function statements
'''
# function defination
# def greet():
#     print("Hello")


# function calling
# greet()
# greet()

# TODO: funtion with parameters

def greet(name): 
    print(f"Hello, {name}")

# greet("John")

# fname = "Jane"
# greet(fname)


# def calc(num1, num2):
#     sum = num1 + num2
#     print(f"sum is: {sum}")


# calc(2, 6)

# TODO: return 

def calc(num1,num2):
    sum = num1 + num2
    return sum

ans = calc(4,5)
print(ans)

print(calc(7,8))
