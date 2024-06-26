'''

Errors
- syntax error -> Print(" ")
- logical error -> '2' + '2' = 22
- runtime error -> while executing the program

Exception Handling
It is a way of handling the errors gracefully

else -> if there is no exception than else block statements will get executed

try :
    //try statements
except BaseException as e :
    // except statements

else:
    // else block statements
finally:
    // finally block statements
    
'''

# num1 = 5
# num2 = 0

# try:
#     print(num1/num2)

# except ZeroDivisionError as e:
#     print("Error: ", e)
#     print("Denominator can be zero")
# except BaseException as e:
#     print("Error: ",e)


# try:

#     file = open("./tfdf.py","r")
#     # file = open("./01functions.py")
    

# except FileNotFoundError as e:
#     print("File does not exist")
#     print("Error: ", e)

# else:
#     print("I am in else block")
#     file.close()
# finally:
#     print("I am in the final block")

# print("Other lines of code")


# TODO: raising the exception

# name = 'John'

# if name == 'John':
#     raise NameError("User is not allowed")



def func():
    try:
        return 1
    except :
        return 2
# print(func())
    
def func2():
    try:
        return 1
    except :
        return 2
    else:
        return 3

# print(func2())

def func3():
    try:
        return 1
    except :
        return 2
    else:
        return 3
    finally:
        return 4
    
print(func3())






