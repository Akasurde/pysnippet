from __future__ import print_function
import pytest

@pytest.fixture(scope='module')
def resource_a_setup(request):
    print('\nresources_a_setup()')
    def resource_a_teardown():
        print('\nresources_a_teardown()')
    request.addfinalizer(resource_a_teardown)

def test_1_that_needs_resource_a(resource_a_setup):
    print('test_1_that_needs_resource_a()')

def test_2_that_does_not():
    print('\ntest_2_that_does_not()')

def test_3_that_does(resource_a_setup):
    print('\ntest_3_that_does()')
