# why need decorator


def greet(name):
    return "hello " + name

# Assigning function to variables
greet_someone = greet

print(greet_someone('Abhijeet'))

# Function inside function
def greet_1(name):
    def get_msg():
        return "Hello, "

    result = get_msg() + name
    return result

print(greet_1('Abhijeet'))


# Decorator

def login_required(func):
    def func_wrapper(name):
        return "<p>Welcome, {0}</p>".format(func(name))
    return func_wrapper

@login_required
def home_page(name):
    return "{0}".format(name)

print(home_page('abhijeet'))


def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
   return "Welcome, {0}".format(name)

print get_text("Abhijeet")

