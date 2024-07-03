# TODO: recursion
'''
divide the big problem into smaller one
find the solution of the smaller problem
'''

# TODO:  factorial of a number
'''
5! = 5 * 4 * 3 * 2 * 1 = 120
0! = 1

5! = 5 * 4!
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1

base condition -> num = 1 --> return num

fact(num) = num * fact(num - 1)
'''

def fact(num):
    # base condition
    if num == 1:
        return 1

    return num * fact(num - 1)

# ans = fact(5)
# print(ans)

# TODO : fibonacci series
'''
0, 1 , 1, 2, 3, 5

fib(5)

# base condition
if num ==1 or num == 0
    return num

# smaller prob
fib(num) = fib(num - 1) + fib(num - 2)
'''

def fib(num):
    # base condition
    if num == 0 or num == 1:
        return num
    return fib(num-1) + fib(num-2)

print(fib(3))

# TODO: find raise to the power