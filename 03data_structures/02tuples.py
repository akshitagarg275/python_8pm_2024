# tuples -> () or tuple()
'''
homogeneous/heterogeneous values
tuples are iterable,
There is the index value which uniquely identifies element
It has the fixed order
tuples are immutable
'''

fruits = ("apple", "guava", "banana", "orange", "papaya", "blueberry")
# print(fruits)
# print(type(fruits))
# print(len(fruits))

# for fruit in fruits:
#     print(fruit)

# TODO: indexing
# print(fruits[2])
# print(fruits[5])
# print(fruits[-1])

# TODO: immutability -> value inside the tuple cannot be modified
# fruits[0] = "pineapple"
# print(fruits)

# TODO: slicing
# tuple_name[start_idx : end_idx : step]

fruits = ("apple", "guava", "banana", "orange", "papaya", "blueberry")

# print(fruits[1: 4])
# print(fruits[0: 6: 2])
# print(fruits[: : 2])
# print(fruits[-4: -1])

# print(fruits.count("apple"))
# print(fruits.index("apple"))


# TODO: swapping the values
a = 10
b = 50

# print("before: value of a: ",a)
# print("before: value of b: ",b)

# a,b = b,a

# print("after: value of a: ",a)
# print("after: value of b: ",b)

# a = (5,)
# print(a)
# print(type(a))