import pytest

@pytest.fixture()
def my_fixture(request):
    a, b, c = request.param
    print(a, b, c)

    def fin():
        print("Fin")
    request.addfinalizer(fin)


@pytest.mark.parametrize('my_fixture', [('Abhijeet', 'Madhuri', 'Punit')], indirect=True)
@pytest.mark.parametrize('your_fixture', ('Abhijeet1', 'Madhuri1', 'Punit1'))
def test_a(my_fixture, your_fixture):
    print(your_fixture)
    print("testcase 1")

@pytest.mark.parametrize('my_fixture', [('Abhijeet', 'Madhuri', 'Punit')], indirect=True)
@pytest.mark.parametrize('your_fixture', ('Abhijeet1', 'Madhuri1', 'Punit1'))
@pytest.mark.parametrize('your_fixture1', ('Abhijeet2', 'Madhuri2', 'Punit2'))
def test_b(my_fixture, your_fixture, your_fixture1):
    print(your_fixture)
    print("testcase 2")
