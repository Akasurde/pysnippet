numbers = range(1, 20)
even = lambda x: x % 2 == 0
odd = lambda x: x % 2 != 0

print(list(filter(even, numbers)))
print(list(filter(odd, numbers)))