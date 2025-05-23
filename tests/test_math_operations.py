import pytest
from calculator import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(5, 0) == 5
    assert add(0, 5) == 5

def test_add_float_numbers():
    assert add(2.5, 3.7) == 6.2 