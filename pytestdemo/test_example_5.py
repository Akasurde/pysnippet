import pytest
from sample import funct


def func():
    print("asasd")
    return 1

def test_debugger():
    a = 2
    pytest.set_trace()
    funct()
    assert a == 2
