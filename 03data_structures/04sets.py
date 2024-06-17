# sets -> {} or set()

'''
sets are unordered
sets do not have indexes
sets are iterable
sets are mutable
sets do not hold duplicate values
'''

s = {1,2,2,2,4,4,6,7,8}
# print(s)
# print(type(s))

# for i in s:
#     print(i)

# print(len(s))

# s.add(14)
# print(s)

# s.update([1,2,34,5,7,8])
# print(s)

# s.remove(34)
# s.discard(34)

a = {1,2,3,4,5}
b = {4,5,6,7}

# print(a.union(b))
# print(a | b)

# print(a.intersection(b))
# print(a & b)

# print(a.difference(b))
# print(a - b)

print(b.difference(a))
print(b-a)
