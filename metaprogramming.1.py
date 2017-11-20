from debugly import debug, predebug

@debug
def add(x, y):
    print x + y

@predebug()
def add_prefix(x, y):
    print x + y

add(1, 2)
add_prefix(1, 2)
