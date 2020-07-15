# Operator Overloading

class Number:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        return "%s + %si" % (self.real, self.img)

    def __repr__(self):
        return "%s + %si" % (self.real, self.img)

    def __add__(self, other):
        x = self.real + other.real
        y = self.img + other.img
        return Number(x, y)

    def __sub__(self, other):
        x = self.real - other.real
        y = self.img - other.img
        return Number(x, y)



n1 = Number(1, 2)
n2 = Number(4, 3)

print("%s" % (n2 - n1))
