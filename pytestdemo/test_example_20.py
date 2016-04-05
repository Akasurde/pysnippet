import pytest

@pytest.fixture()
def test_one():
    print("Something")
    pytest.skip('No Redis server found')
