import pytest

@pytest.fixture()
def somedata():
    f = { 'foo': 1, 'bar': 2}
    return f

def test_db_connection(somedata):
    assert somedata['foo'] == 1
