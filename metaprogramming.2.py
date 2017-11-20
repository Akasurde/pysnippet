from debugly import debugmethods

@debugmethods
class A():
    def add(self):
        pass
    def sub(self):
        pass

for key, val in vars(A).items():
    print key, val

a = A()
a.add()
a.sub()
