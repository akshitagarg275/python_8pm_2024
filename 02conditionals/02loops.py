# Loops -> To repeat certain code for the certain no of times

# DRY -> Donot Repeat Yourself

# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

# while loop
# for in loop

# TODO : while loop
'''
initialization
condition 
    # while statements
increment/decrement (re-initialization)
'''
# initialisation
# i = 1
# # condition
# while i <= 5:
#     # while statement
#     print("Hello: ", i)
#     # increment/decrement
#     i = i + 1 #re-initialisation

# print("After the execution of the loop")

# i = 0
# while i <= 10 :
#     print(i)
#     i = i + 2

# i = 0 
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1

# TODO: odd numbers
# TODO: print all the multiples of 5


'''
for in loop
'''

# fruits = ["apple", "mango", "banana", "orange", "grapes"]

# for fruit in fruits:
#     print(fruit)


colors = ("red", "yellow", "orange", "green", "purple")

# for color in colors:
#     print(color)

# for i in range(5):
#     print(i)


# full_name = "John Doe"

# for s in full_name:
#     print(s)


# TODO: else block in the loop
'''
If the loop execution is terminated using break statement
than the else block will not get executed at all.

else block in the loop will get executed only if the loop is 
executed completely
'''

# for i in colors:
#     if i == "green":
#         # continue  # else block will get executed
#         break  # else block will not get executed
#     print(i)
# else:
#     print("for loop executed completely")


# TODO: infinite loop

while True:
    print("Hello")