from __future__ import print_function
import pytest

@pytest.fixture()
def resource_a():
    print('\nresources_a() "setup"')

def test_1_that_needs_resource_a(resource_a):
    print('test_1_that_needs_resource_a()')

def test_2_that_does_not():
    print('\ntest_2_that_does_not()')

def test_3_that_does(resource_a):
    print('test_3_that_does()')

