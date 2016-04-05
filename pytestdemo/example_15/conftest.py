
import pytest

@pytest.fixture(scope="session")
def resource_a(request):
    print('In resource_a()')

    def resource_a_fin():
            print('\nIn resource_a_fin()')
    request.addfinalizer(resource_a_fin)

@pytest.fixture(scope="module")
def resource_b(request, resource_a):
    print('In resource_b()')

    def resource_b_fin():
            print('\nIn resource_b_fin()')
    request.addfinalizer(resource_b_fin)

@pytest.fixture(scope="function")
def resource_c(request, resource_b):
    print('In resource_c()')

    def resource_c_fin():
            print('\nIn resource_c_fin()')
    request.addfinalizer(resource_c_fin)


# these are just some fun dividiers to make the output pretty
# completely unnecessary, I was just playing with autouse fixtures
@pytest.fixture(scope="function", autouse=True)
def divider_function(request):
    print('\n        --- function %s() start ---' % request.function.__name__)
    def fin():
            print('        --- function %s() done ---' % request.function.__name__)
    request.addfinalizer(fin)

@pytest.fixture(scope="module", autouse=True)
def divider_module(request):
    print('\n    ------- module %s start ---------' % request.module.__name__)
    def fin():
            print('    ------- module %s done ---------' % request.module.__name__)
    request.addfinalizer(fin)

@pytest.fixture(scope="session", autouse=True)
def divider_session(request):
    print('\n----------- session start ---------------')
    def fin():
            print('----------- session done ---------------')
    request.addfinalizer(fin)
