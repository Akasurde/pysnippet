import pytest

@pytest.mark.mymarker
@pytest.mark.other_marker
def test_something():
    print("In test_something")
