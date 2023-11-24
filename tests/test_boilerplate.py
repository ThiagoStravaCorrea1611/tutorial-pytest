import pytest

@pytest.mark.skip
def test_always_pass():
    assert True

@pytest.mark.skip
def test_always_fail():
    assert False

