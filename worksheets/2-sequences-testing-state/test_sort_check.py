"""
Test a function to check whether a list is sorted or not.
"""
from sort_check import is_sorted


def test_empty_list():
    """
    Check that an empty list is considered sorted.
    """
    assert is_sorted([])
