import pytest

@pytest.fixture()
def foo(request):
    print("\tIn foo")
    def fin():
        print("\tIn foo teardown")
    request.addfinalizer(fin)

@pytest.fixture()
def bar(request, foo):
    print("\t\tIn bar")
    def fin():
        print("\t\tIn bar teardown")
    request.addfinalizer(fin)

@pytest.fixture()
def baz(request, bar):
    print("\t\tIn baz")
    def fin():
        print("\t\tIn baz teardown")
    request.addfinalizer(fin)


def test_one(baz):
    print("In test_one")

def test_two(bar):
    print("In test_two")
