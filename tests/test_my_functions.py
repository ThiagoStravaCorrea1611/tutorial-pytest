import pytest
import time
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

def test_add_strings():
    result = my_functions.add("I like", " Burgers!")
    assert result == "I like Burgers!"

def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2

def test_divide_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2

@pytest.mark.skip(reason="THis feature is currently broken")
def test_add_broken():
    assert my_functions.add(1, 4) == 3

@pytest.mark.xfail(reason="We know we can not divide by zero")
def test_divide_zero_broken():
    assert my_functions.divide(10, 0) == 10/0