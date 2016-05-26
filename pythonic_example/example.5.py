a = [1, 2, 3, 4, 5, 6]

sp = []
for i in a:
    sp.append(i ** 2)
print(sp)


# [experssion  for item1 in iterable1 if condition1
#              for item2 in iterable2 if condition2]
squares = [x**2 for x in a]
print(a)
print(squares)

# list of squares of even numbers

even_squares = [ x**2 for x in a if x % 2 == 0]
print(even_squares)


# Nested

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)


print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
