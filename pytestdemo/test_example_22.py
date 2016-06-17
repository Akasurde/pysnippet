import pytest

@pytest.fixture()
def test_package(request):
    def make_test_package(version='1.0'):

        def fin():
            return test_package

        request.addfinalizer(fin)

    return make_test_package


def test_install_package(test_package):
    package = test_package(version='1.1')
