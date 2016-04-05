import pytest

def return_a(x):
    return x == 1

@pytest.mark.skipif(return_a(1), reason="Some impossible condition")
def test_function_one():
    pass

@pytest.mark.skipif(return_a(0), reason="Some possible condition")
def test_function_two():
    pass
