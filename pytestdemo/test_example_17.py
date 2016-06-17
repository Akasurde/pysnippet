import pytest

@pytest.yield_fixture()
def mysql_db():
    print("\n[Setup] In MySQL connection")
    b = {'foo': 1, 'bar': 2, 'baz': 3}
    b = [1, 2, 4]
    yield b
    print("\n[Teardown] In MySQL connection")

def test_one(mysql_db):
    print("\n\tIn test_one")
    assert mysql_db[1] == 1

def test_two(mysql_db):
    print("\n\tIn test_two")
    assert mysql_db[1] == 2

def test_three(mysql_db):
    print("\n\tIn test_three")
    assert mysql_db[2] == 3
