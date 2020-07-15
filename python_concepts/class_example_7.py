# Overriding

class Animal:
    def message(self):
        print("Print from Animal")

class Dog(Animal):
    def message(self):
        print("Print from Dog")

d = Dog()
d.message()