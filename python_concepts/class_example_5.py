class Base(object):
    def __init__(self):
        print("Base init'ed")

class ChildA(Base):
    def __init__(self):
        print("ChildA init'ed")
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        print("ChildB init'ed")
        super(ChildB, self).__init__()

class ChildC(ChildA, ChildB):
    def __init__(self):
        print("ChildC init'ed")
        super(ChildA, self).__init__()
        super(ChildB, self).__init__()

    def print_mro(self):
        mro = type(self).mro()
        print(mro)


# c_a = ChildA()
# c_b = ChildB()
# b = Base()
c_c = ChildC()
c_c.print_mro()