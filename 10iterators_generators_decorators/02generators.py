'''
Generators:
It looks like a normal function but in actual it is different
It uses the yield keyword rather than using return 

def func_name():
    yield statement
'''

def simpleGen():
    yield 1
    yield 2
    yield 3

# print(simpleGen())

# for val in simpleGen():
#     print(val)

# TODO: it is generator object
# it = simpleGen()
# print(next(it))


# TODO: fibonacci numbers
def fib(limit):
    a,b = 0,1

    while a < limit:
        yield a
        a,b = b, a+b
    
x = fib(5)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# for i in fib(5):
#     print(i)