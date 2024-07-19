'''
2D Vector -> 3i^ + 4j^

3D Vector -> 3i^ + 4j^ + 5j^

'''

class Vec2d:
    def __init__(self, icap, jcap):
        self.icap = icap
        self.jcap = jcap

    def printMe(self):
        print(f"{self.icap}i^ + {self.jcap}j^")

class Vec3d(Vec2d):

    def __init__(self, icap, jcap, kcap):
        super().__init__(icap, jcap)
        self.kcap = kcap

    def printMe(self):
        print(f"{self.icap}i^ + {self.jcap}j^ + {self.kcap}k^")        

obj = Vec2d(4,5)
# obj.printMe()

obj1 = Vec3d(2,3,4)
obj1.printMe()

