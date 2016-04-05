import pytest

@pytest.fixture()
def before():
    print("Running before")

def test_1(before):
    print("Running test 1")

@pytest.mark.usefixtures("before")
def test_2():
    print("Running test 2")

@pytest.mark.usefixtures("before")
class TestCase1:
    def test_3(self):
        print("Running test 3")


class TestCase2:
    @pytest.mark.usefixtures("before")
    def test_4(self):
        print("Running test 4")
