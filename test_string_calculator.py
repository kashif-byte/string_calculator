import pytest
from string_calculator import add
from exceptions import NegativeNumberError

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_itself():
    assert add("1") == 1

def test_two_numbers_returns_sum():
    assert add("1,7") == 8

def test_multiple_numbers_returns_sum():
    assert add("1,2,3,4,5") == 15

def test_newlines_between_numbers():
    assert add("1\n2,3") == 6
    
def test_mixed_delimiters():
    assert add("1,2\n3,4") == 10

def test_negative_number_throws_exception():
    with pytest.raises(NegativeNumberError, match="negative numbers not allowed: -1"):
        add("-1")

def test_multiple_negative_numbers_in_exception():
    with pytest.raises(NegativeNumberError, match="negative numbers not allowed: -1, -3"):
        add("-1,2,-3")