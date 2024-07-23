'''
iterators: the ones on which we can apply the for loop
iterables : list, dict, tuple, set
iterator : it is an object that is used to iterate over the iterables
iteration

python iterator object is initialised using the iter() method, It uses next() method
for the iteration

__iter__() : iter() method used for initialisation
__next__(): the next method returns the next value for iterable
'''

# string = "python"
# it = iter(string)
# print(it)
# print(type(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


class Test:

    def __init__(self, limit):
        self.limit = limit

    # creating the iter object 
    # and also initialising it
    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x

        if x > self.limit:
            raise StopIteration
        
        self.x = x + 1
        return x

for i in Test(15):
    print(i)