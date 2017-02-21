# here username and password is required parameter to print_me
# method

def print_me(**kwargs):
    required = ('username', 'password')
    if not all([x in kwargs for x in required]):
        print "Required parameter not found"
print("This fails")
print_me(a="a")
print("This will not fail")
print_me(username="a", password="a")
print("This fails")
print_me(username="a")
print("This fails")
print_me(password="a")
