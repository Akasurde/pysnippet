# Overloading

class Person:
    def Hello_with_name(self, name):
        print("Hello" + name)

    def Hello_wo_name(self):
        print("Hello")

    def Hello(self, name=None):
        if name:
            print("Hello " + name)
        else:
            print("Hello")

c1 = Person()
c1.Hello()
c1.Hello_wo_name()
c1.Hello_with_name('a')
c1.Hello('Abhijeet')
