class Alphabet:
    def __init__(self, value):
        self._value = value
        # self.y = ''
        pass
          
    # getting the values    
    @property
    def value(self):
        print('Getting value')
        return self._value
          
    # # setting the values    
    # @value.setter
    # def value(self, value):
    #     print('Setting value to ' + value)
    #     if value == 'Abhijeet':
    #         self.y = value
    #     self._value = value
          
    # # deleting the values
    # @value.deleter
    # def value(self):
    #     print('Deleting value')
    #     del self.y
    #     del self._value

 

# passing the value
x = Alphabet('GeeksforGeeks')
print(x.value)
# print(x._value)
# print(x.value)
  
# x._value = 'Abhijeet'
# print(x.value)

# print(x.y)
# # x.value = 'Abhijeet'
# x._value = 'Abhijeet'
# print(x.y)

  
# del x.value
# print(x.y)
