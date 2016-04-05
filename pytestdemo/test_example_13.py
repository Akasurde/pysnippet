import pytest

@pytest.fixture()
def my_fixture(request):
    print('\n-----------------')
    print('fixturename : %s' % request.fixturename)
    print('scope       : %s' % request.scope)
    print('function    : %s' % request.function.__name__)
    print('cls         : %s' % request.cls)
    print('module      : %s' % request.module.__name__)
    print('fspath      : %s' % request.fspath)
    print('-----------------')

    if request.function.__name__ == 'test_three':
        request.applymarker(pytest.mark.xfail)

def test_one(my_fixture):
    print('test_one():')

class TestClass():
    def test_two(self, my_fixture):
        print('test_two()')

def test_three(my_fixture):
    print('test_three()')
    assert False
