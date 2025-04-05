import pytest

from testing.exercises.code import multiply, divide, reverse_string


def test_multiply_positives():
    assert multiply(2, 5) == 10


def test_multiply_negatives():
    assert multiply(-2, -5) == 10


def test_multiply_positive_negative():
    assert multiply(-2, 5) == -10


def test_reverse_string():
    assert reverse_string('hello') == 'olleh'


def test_reverse_empty():
    assert reverse_string('') == ''


def test_divide():
    assert divide(28, 7) == 4


def test_divide_zero():
    with pytest.raises(ValueError) as e:
        divide(7, 0)
    assert str(e.value) == 'Cannot divide by zero'
