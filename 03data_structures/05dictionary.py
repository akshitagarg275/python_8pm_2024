# dictionary --> {key : value} or dict()

'''
mutable datatype
keys can only be the immutable datatype
values can be any datatype

keys are used to uniquely fetch the value
dictionary is iterable
'''

user = {
    "fname" : "John",
    "lname" : "Doe",
    "age" : 23,
    "course" : ["Python", "Django"],
    "gender" : "M"
}

# print(user)
# print(type(user))

# print(user["fname"])
# user["fname"] = "Jane"
# user["country"] = "India"
# print(user)

# for i in user:
#     print(user[i])

# TODO: to get the values
# print(user.values())
# TODO: to get the keys
# print(user.keys())
# TODO: to get key value pair
# print(user.items())

# TODO: throws an error if key is not available
# print(user["fnames"])

# print(user.get("fnames", "NA"))

# TODO: fromkeys
# seq = ("a", "b", "c")
# user1 = dict.fromkeys(seq, 5)
# print(user1)

# print(user)
# print(user.pop("fname"))
# print(user)

# print(user)
# user.popitem()

# print(user)

stu = dict(fname="Jane", lname = "Doe")
# print(stu)

stu2 = dict(**stu, age =23)
print(stu2)