from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper

def predebug(prefix='[DEBUG]'):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(prefix + " " + func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorate

def debugmethods(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls

class debugmeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        clsobj = debugmethods(clsobj)
        return clsobj
