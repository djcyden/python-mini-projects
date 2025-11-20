from calculator_debug import (
    add,
    subtract,
    multiply,
    divide,
    calculate,
)


def test_add_debug():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract_debug():
    assert subtract(10, 3) == 7
    assert subtract(0, 5) == -5


def test_multiply_debug():
    assert multiply(2, 4) == 8
    assert multiply(-2, 3) == -6


def test_divide_normal_debug():
    assert divide(10, 2) == 5
    assert divide(7.5, 2.5) == 3


def test_divide_by_zero_debug():
    result = divide(5, 0)
    assert isinstance(result, str)
    assert "Division by zero" in result


def test_calculate_add_debug():
    assert calculate("+", 20, 30) == 50


def test_calculate_unknown_op_debug():
    result = calculate("???", 1, 2)
    assert "Unknown operation" in result
