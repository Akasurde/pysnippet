a = ['a', 'b', 'c', 'd', 'e']

for i, value in enumerate(a):
    print("i : %s : value : %s " % (i, value))

print("Enumerate starting from 5")
for i, value in enumerate(a, 5):
    print("i : %s : value : %s " % (i, value))
