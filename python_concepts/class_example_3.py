class Cat:
    species = "Felis silvestris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "<Cat %s>" % self.name

    def __repr__(self):
        return "Cat(%s)" % self.name

    def describe(self):
        print("I am %s of type '%s' and I am %s years old" % (self.name, self.species, self.age))

    def speak(self):
        print("%s says Meow" % self.name)


c = Cat('Felix', 4)
c.describe()
c.speak()
print(str(c))
print(repr(c))
