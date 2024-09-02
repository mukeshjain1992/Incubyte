import pytest
from string_calculator import StringCalculator

def test_add_empty_string():
    calculator = StringCalculator()
    assert calculator.add("") == 0

def test_add_single_number():
    calculator = StringCalculator()
    assert calculator.add("1") == 1