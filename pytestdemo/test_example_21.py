import pytest

@pytest.fixture()
def my_fixture(request, httpcode):
    print(httpcode)

    def teardown_session():
        """ define fixture for session level teardown """
        print('This is teardown session, uninstalling server')
    request.addfinalizer(teardown_session)

def test_s(request):
    my_fixture(request, 401)
    print("I am here")

