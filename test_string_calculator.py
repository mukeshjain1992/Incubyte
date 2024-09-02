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

