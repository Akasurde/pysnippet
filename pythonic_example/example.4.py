a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print a[0]

print(a[:])
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])

print('before', a)
a[2:7] = [99, 12, 'x']
print('after ', a)
