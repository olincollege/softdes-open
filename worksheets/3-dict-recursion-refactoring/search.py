"""
Sample search algorithm implementations for refactoring practice.
"""


def linear_search(num_list, target_num):
    """
    Find the index where a target number occurs in a list.

    Given a list of numbers and a target value, return the first index where the
    target number is found, or None otherwise. Use a linear search algorithm,
    checking each index one at a time.

    Args:
        num_list: A list of numbers (ints or floats) representing the list to
            search in.
        target_num: An int or float representing the value to search for.

    Returns:
        An int representing the first index where target_num occurs, or None if
        target_num is not in num_list.
    """
    index = 0
    num_list_length = len(num_list)
    while index < num_list_length:
        current_value = num_list[index]
        if current_value == target_num:
            return index
        next_index = index + 1
        index = next_index
    return None


def binary_search(num_list, target_num):
    """
    Find the index where a target number occurs in a list.

    Given a list of numbers and a target value, return the first index where the
    target number is found, or None otherwise. Use a binary search algorithm,
    assuming that the list is sorted.

    Args:
        num_list: A list of numbers (ints or floats), assumed to be sorted from
            least to greatest, representing the list to search in.
        target_num: An int or float representing the value to search for.

    Returns:
        An int representing the first index where target_num occurs, or None if
        target_num is not in num_list.
    """
    lo = 0
    hi = len(num_list)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if num_list[mid] == target_num:
            return mid
        if target_num < num_list[mid]:
            hi = mid
        else:
            lo = mid + 1
    return None
