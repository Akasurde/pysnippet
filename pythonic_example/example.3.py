#!/usr/bin/env python3
from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)

print(my_values)

# Get all values
print("Red     : ", my_values.get('red'))
print("Green   : ", my_values.get('green'))
print("Yellow  : ", my_values.get('yellow'))


# Assign default values
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
yellow = my_values.get('yellow', [''])[0] or 0

print('Red     : %r' % red)
print('Green   : %r' % green)
print('Yellow  : %r' % yellow)


print(int(my_values.get('red', [''])[0] or 0))

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

print('Red       : %d' % get_first_int(my_values, 'red'))
print('Green     : %d' % get_first_int(my_values, 'green'))
print('Yellow    : %d' % get_first_int(my_values, 'yellow'))
