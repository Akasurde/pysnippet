class A:
    #def process(self):
    #    print('A process()')
    pass


class B:
    # pass
    def process(self):
        print('B process()')


class C(A, B):
    # pass
    def process(self):
         print('C process()')

class D(B, C):
    pass


# Example 1
#obj = C()
#obj.process()
#print(C.mro())   # print MRO for class C



# Example 2
obj = D()
obj.process()
# print(D.mro())
