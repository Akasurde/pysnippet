domestic_animals = ['cow', 'dog', 'cat']

print("Before processing :")
print(domestic_animals)

print("After processing :")
print(map(lambda x: x.title(), domestic_animals))
print(list(map(lambda x: x.title(), domestic_animals)))
