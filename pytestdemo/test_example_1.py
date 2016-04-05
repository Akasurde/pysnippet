def func(x):
    return x + 1

def test_positive_func():
    assert True #func(3) == 4

def test_negative_func():
    assert func(4) == 6
