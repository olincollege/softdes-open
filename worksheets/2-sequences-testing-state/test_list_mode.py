"""
Test a function to find the most commonly occurring element in a list.
"""
from list_mode import mode


def test_all_same():
    """
    Check that a list consisting entirely of one element reports that element as
    its mode.
    """
    assert mode([1, 1, 1]) == 1
