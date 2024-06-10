# list --> [ ] , list ()
'''
- list can contain homogeneous as well heterogeneous datatypes
- It is iterable
- It has fixed order (oredered)
- Each element inside the list is uniquely identified using index number 
- List is mutable
'''

# fruits = ["apple", "guava", "banana", "orange", "papaya", "blueberry"]
# print(fruits)
# print(type(fruits))

# print(len(fruits))

# TODO: indexing
# print(fruits[0])
# print(fruits[3])
# print(fruits[-1])

# TODO: iterable
# for fruit in fruits:
#     print(fruit, end=" ")

# TODO: mutability
# print("List before: ", fruits)
# fruits[0] = "pineapple"
# print("List after: ", fruits)


# even = list(range(0 , 11, 2))
# print(even)

# TODO: slicing 
# fruits = ["apple", "guava", "banana", "orange", "papaya", "blueberry" , "guava"]


# listName[start_index : end_index: step]

# print(fruits[2: 5])
# print(fruits[1: 6 : 2])
# print(fruits[ : 4])
# print(fruits[: :])
# print(fruits[-5 : -2])


# TODO: append -> adding the element at the end of the list
# print("before: ", fruits)
# fruits.append("cherry")
# print("after: ", fruits)

# fruits.clear()
# del(fruits)
# print("after: ", fruits)

# print(fruits.index("guava"))

fruits = ["apple", "guava", "banana", "orange", "papaya", "blueberry" , "guava"]
# fruits.insert(2,"mango")
# print(fruits)

# fruits.extend(["strawberry", "water melon", "musk melon"])
# print(fruits)

# TODO: count : to know the no of objects
# print(fruits.count("guava"))

# print(fruits.remove("banana"))
# print(fruits)

# while "guava" in fruits:
#     fruits.remove("guava")

# print(fruits)
# print("before: ", fruits)
# print(fruits.pop())
# print("after: ", fruits)

# TODO: reverse
fruits = ["apple", "guava", "banana", "orange", "papaya", "blueberry" , "guava"]

# print(fruits.reverse())
# print(reversed(fruits))
# print(fruits)


# TODO: sort
print("before sorting: ", fruits)
# print(fruits.sort())
# print(sorted(fruits))
fruits = sorted(fruits, reverse=True)
print("after sorting: ", fruits)