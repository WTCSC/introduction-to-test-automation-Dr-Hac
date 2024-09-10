import pytest
import math_it_up
import statistics
import random

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
    for i in range(1000):
        assert math_it_up.is_even(i) == (i % 2 == 0)


def test_is_odd():
    """
    Tests for the `is_odd` function
    """
    for i in range(1000):
        assert math_it_up.is_odd(i) == (i % 2 != 0)


def test_mean():
    """
    Tests for the `mean` function
    """
    l = []
    for i in range(1000):
        l.append(i + random.randint(1, 100))
        assert math_it_up.mean(l) == statistics.mean(l)


def test_median():
    """
    Tests for the `median` function
    """
    l = []
    for i in range(1000):
        l.append(i + random.randint(1, 100))
        assert math_it_up.median(l) == statistics.median(l)


def test_mode():
    """
    Tests for the `mode` function
    """
    l = []
    for i in range(1000):
        l.append(i + random.randint(1, 100))
        assert math_it_up.mode(l) == statistics.multimode(l)

