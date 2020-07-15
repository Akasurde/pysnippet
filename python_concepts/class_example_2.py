class Animal:
    pass


class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print("I am %s of type %s and I am %s years old" % (self.name, self.species, self.age))

    def speak(self):
        print("%s says Woof" % self.name)


d = Dog('CheeseCake', 5)
# d.describe()
# d.speak()
print(str(d))
print(repr(d))

#print(d.species)
