from main import addition
from multiplication import multiply
from subtraction import subtract

def test_add_positive():
    assert addition(5,2) == 7

def test_add_negative():
    assert addition(10,-40) == -30

def test_add_zeros():
    assert addition(2,0) == 2

def test_multiplication():
    assert multiply(2,2) == 4

def test_subtraction():
    assert subtract(300,20) == 280
