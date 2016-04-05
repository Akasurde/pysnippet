def setup_module(module):
    print("\nInside setup_module : %s" % (module.__name__))
def teardown_module(module):
    print("\nInside teardown_module : %s" % (module.__name__))
def setup_function(function):
    print("\nInside setup_function : %s" % (function.__name__))
def teardown_function(function):
    print("\nInside teardown_function : %s" % (function.__name__))
def test_negative_number():
    print("\nInside test_negative_number")
    assert True

class TestUnitMultiply:
    def setup(self):
        print("\nInside setup()")
    def teardown(self):
        print("\nInside teardown()")
    def setup_class(cls):
        print("\nInside setup_class : %s" % (cls.__name__))
    def teardown_class(cls):
        print("\nInside teardown_class : %s" % (cls.__name__))
    def setup_method(self, method):
        print("\nInside setup_method : %s" % (method.__name__))
    def teardown_method(self, method):
        print("\nInside teardown_method : %s" % (method.__name__))

    def test_positive_number(self):
        print("Test_positive_number")
        assert True
