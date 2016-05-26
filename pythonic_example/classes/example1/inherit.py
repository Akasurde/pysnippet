class Diagram(object):
    def __init__(self):
        self.name = 'diagram'
        print("Init called")

    def cal_area(self):
        raise NotImplementedError("Calculate Area not implemented")

    def cal_circum(self):
        pass

class Triangle(Diagram):
    def __init__(self):
        self.name = 'triangle'
        print("Init from triangle")

    def cal_area(self, x, y, z):
        print("Area of triangle : " , x * y * z)

    def cal_circum(self, x, y, z):
        print("Circumference of triangle" , x + y + z)

class Circle(Diagram):
    def __init__(self):
        print("Init from circle")

    def cal_area(self, r):
        print("Area of circle : " , 3.14 * r * r)

    def cal_circum(self, r):
        print("Circumference of triangle" , 2 * 3.14 * r)


triangle = Triangle()
triangle.cal_area(2, 4, 6)
print(triangle.name)

circle = Circle()
circle.cal_area(14)

d = Diagram()
#d.cal_area()
print(d.name)
