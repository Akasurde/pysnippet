def my_gen():
    for i in range(10):
        yield i

print(type(my_gen()))

for i in my_gen():
    print(i)


def log(message, values):
    if not values:
         print(message)
    else:
        value_str = ", ".join(str(x) for x in values)
        print('%s: %s' % (message, value_str))

log('Hi THere', [1, 2])
log('No argument', [])

def better_log(message, *values):
    if not values:
        print(message)
    else:
        value_str = ", ".join(str(x) for x in values)
        print('%s: %s' % (message, value_str))


better_log('Hi There', 1, 2)
better_log('No argument')


it = my_gen()
better_log("Hi", *it)
