import pytest
from calculator_simple import add, subtract, multiply, divide, calculate

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6

def test_divide_normal():
    assert divide(6, 3) == 2
    assert divide(7.5, 2.5) == 3

def test_divide_by_zero():
    result = divide(5, 0)
    assert isinstance(result, str)
    assert "Division by zero" in result

def test_calculate_add():
    assert calculate("+", 2, 3) == 5

def test_calculate_unknown_operation():
    result = calculate("%", 2, 3)
    assert "Unknown operation" in result
