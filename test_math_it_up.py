import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""


def test_is_even():
    """
    Tests for the `is_even` function
    """
    assert math_it_up.is_even(2) == True  # test that the number 2 is even
    assert math_it_up.is_even(3) == False  # test that the number 3 is not even


def test_is_odd():
    """
    Tests for the `is_odd` function
    """
    assert math_it_up.is_odd(2) == False  # test that the number 2 is not odd
    assert math_it_up.is_odd(3) == True  # test that hte number three is odd


def test_mean():
    """
    Tests for the `mean` function
    """
    assert math_it_up.mean([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]) == 16.75  # test that the mean of the list is 16.75


def test_median():
    """
    Tests for the `median` function
    """
    assert math_it_up.median([9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]) == 15.5  # test that the median of the list is 15.5


def test_mode():
    """
    Tests for the `mode` function
    """
    assert math_it_up.mode([9, 10, 12, 13, 13, 13, 15, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]) == [13, 15]  # test that the mode of the list is [13, 15]
