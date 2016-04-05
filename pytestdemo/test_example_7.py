from __future__ import print_function

def resource_a_setup():
    print('resources_a_setup()')

def resource_a_teardown():
    print('resources_a_teardown()')

def setup_module(module):
    print('\nsetup_module()')
    resource_a_setup()

def teardown_module(module):
    print('\nteardown_module()')
    resource_a_teardown()

def test_1_that_needs_resource_a():
    print('test_1_that_needs_resource_a()')

def test_2_that_does_not():
    print('\ntest_2_that_does_not()')
