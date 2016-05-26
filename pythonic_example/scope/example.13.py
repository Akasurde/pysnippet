i = 1

def foo():
    global i
    i = 5
    print(i, "in foo()")

#foo()
print(i, "in global")
foo()

