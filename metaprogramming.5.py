class Descriptor:
    def __init__(self, name=None):
        self.name = name
    def __set__(self, instance, name):
        print("Set", name)
        self.name = name.title()
    def __delete__(self, instance):
        print("Delete", self.name)
        del self.name

class Person:
    name = Descriptor()

p = Person()
p.name = "Abhijeet"
