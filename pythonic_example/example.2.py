somelist = []

# Never compare length
if len(somelist) == 0:
    print("No. This is wrong")

# Just check not operator against list or variable
if not somelist:
    print("This is right")


somealist = [1]

# Don't check length of variable
if len(somealist) > 0:
    print("This is wrong")


# Just check if non-empty variables
if somealist:
    print("This is right")
