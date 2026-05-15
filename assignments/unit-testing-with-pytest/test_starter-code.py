"""
Unit tests for the Calculator module using pytest.

This file demonstrates the structure for testing calculator functions.
Complete and expand these tests to meet the assignment requirements.
"""

import pytest
from starter_code import add, subtract, multiply, divide


class TestAddition:
    """Test cases for the add() function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
    
    def test_add_with_zero(self):
        """Test adding zero."""
        assert add(5, 0) == 5
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-2, -3) == -5


class TestSubtraction:
    """Test cases for the subtract() function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2
    
    def test_subtract_with_zero(self):
        """Test subtracting zero."""
        assert subtract(5, 0) == 5
    
    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative."""
        assert subtract(2, 5) == -3


class TestMultiplication:
    """Test cases for the multiply() function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(3, 4) == 12
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-3, -4) == 12


class TestDivision:
    """Test cases for the divide() function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(10, 2) == 5
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)


# TODO: Add more tests for edge cases and the power() function
