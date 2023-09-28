"""
Function to check whether a list is already sorted or not.
"""


def is_sorted(list_):
    """
    Check whether a list is sorted or not.

    Args:
        list_: A list to check for being sorted or not.

    Returns:
        True if list_ is sorted, and False otherwise.
    """
    copy = list_
    copy.sort()
    return list_ == copy
