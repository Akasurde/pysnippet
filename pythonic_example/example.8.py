def divide(x, y):
    try:
        return x / y
    except:
        return None # This is wrong


a, b = 0, 5
result = divide(a, b)
# This is wrong
if not result:
    print("Invalid inputs")




def correct_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs") from e


try:
    result = correct_divide(a, b)
except ValueError:
    print("Invalid Inputs")
else:
    print("Result: %.1f" % (result))
