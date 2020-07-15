def is_authenticated(f):
    def wraps(*args):
        print("Checking if user authenticated")
        print("Calling function %s" % f.__name__)
        return f(args)
    return wraps

@is_authenticated
def get_user(user_id):
    print("Get User %s" % user_id)

get_user('Abhijeet')