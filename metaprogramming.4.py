class Structure:
    _fields = []
    def __init__(self, *args):
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

class Triangle(Structure):
    _fields = ['x', 'y', 'z']

class Circle(Structure):
    _fields = ['r']

class Square(Structure):
    _fields = ['a']

t = Triangle(3, 4, 5)

