from debugly import debugmeta

class A(metaclass=debugmeta):
    def add(self):
        pass
    def sub(self):
        pass
a = A()
a.add()
a.sub()
