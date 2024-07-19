'''
dunder methods / magic methods

len() --> __len__
+ --> __add__
'''

# print(dir(str))

class Num:
    def __init__(self, num):
        self.num = num

    def __add__(self, obj):
        return self.num + obj.num

    def __lt__(self, obj):
        return self.num < obj.num
    
    def __str__(self):
        return 'I am an object of class Num'
    

# n1 = Num(5)
# n2 = Num(4)
# print(n1 + n2)
# print(n1 < n2)
# print(n1)


class NumList:
    def __init__(self) :
        self.nums = [1,2,3,4,5]
    
    def __len__(self):
        return len(self.nums)

obj = NumList()
print(len(obj))