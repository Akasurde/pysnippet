#Scope
# function  : default
# class
# module
# session

import pytest

scopevar = "function"
#scopevar = "module"
#scopevar = "class"

@pytest.fixture(scope=scopevar)
def mysql_db(request):
    print("Connecting to database")
    s = { 'foo': 1, 'bar': 2}
    def close_connection():
        print("Closing database connection")
    request.addfinalizer(close_connection)
    return s


def test_1():
    print("Running test_1")

def test_2():
    print("Running test_2")

class TestCase1:
    def test_3(self, mysql_db):
        print("Running test_3")
