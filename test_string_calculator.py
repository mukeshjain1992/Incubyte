import pytest
from string_calculator import StringCalculator

def test_add_empty_string():
    calculator = StringCalculator()
    assert calculator.add("") == 0

def test_add_single_number():
    calculator = StringCalculator()
    assert calculator.add("1") == 1

def test_add_two_numbers():
    calculator = StringCalculator()
    assert calculator.add("1,2") == 3

def test_add_multiple_numbers():
    calculator = StringCalculator()
    assert calculator.add("1,2,3") == 6

def test_add_with_newlines():
    calculator = StringCalculator()
    assert calculator.add("1\n2,3") == 6

def test_add_with_custom_delimiter():
    calculator = StringCalculator()
    assert calculator.add("//;\n1;2") == 3

def test_add_with_negative_number():
    calculator = StringCalculator()
    with pytest.raises(ValueError, match="negative numbers not allowed: -2"):
        calculator.add("1,-2,3")

def test_ignore_numbers_greater_than_1000():
    calculator = StringCalculator()
    assert calculator.add("2,1001") == 2


def test_add_with_any_length_delimiter():
    calculator = StringCalculator()
    assert calculator.add("//[***]\n1***2***3") == 6
