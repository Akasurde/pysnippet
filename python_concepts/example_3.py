def is_authenticated(f):
    def wraps(*args, **kwargs):
        print("Checking if user authenticated")
        print("Calling function %s" % f.__name__)
        if f.__name__ == 'update_user':
            print("Updating user might take a long time")
            print(kwargs)
        else:
            print(args)
        return f(*args, **kwargs)
    return wraps

@is_authenticated
def get_user(user_id):
    print("Get User %s" % user_id)

@is_authenticated
def update_user(user_id, user_data):
    print("Update User %s" % user_id)

get_user('Abhijeet')
update_user('Abhijeet', user_data='Savitoj')


