# global scope
x = 100

def func():
    # local scope
    # x = 20
    global x
    x = 30
    print("Inside the func: ", x)

# func()
# print("Outside value of x: ", x)


def outer():
    y = 10
    # print("Outer: ", y)
    def inner():
        nonlocal y
        y = 50
        print("Inner: ", y)
    inner()
    print("Outer: ", y)

# outer()

# print(dir())