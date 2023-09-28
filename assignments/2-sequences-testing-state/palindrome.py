"""
Find the digits of the next largest palindromic number.
"""


def digit_list(integer):
    """
    Create a list of an integer's digits in order.

    Given an integer, return a list of the integer's digits, from most
    significant to least significant. Thus the number 123 would result in the
    list [1, 2, 3].

    Args:
        integer: An int representing the number whose digits to make a list.

    Returns:
        A list representing the digits of integer in order.
    """
    return [int(digit) for digit in str(integer)]


def next_palindrome_digits(digits):
    """
    Given a list of single-digit integers representing a palindromic number,
    return a list of the digits of the next largest palindromic number.

    A palindromic number is one whose digits are the same forwards and
    backwards, such as 33, 1221, or 2468642. Given a list of single digits
    representing such a number, such as [1, 2, 2, 1] for 1221, return the
    digits of the next largest palindromic number. For 1221, this would be
    1331, so return [1, 3, 3, 1].

    Args:
        digits: A list of single-digit integer representing the digits of
            the palindromic number to start from.

    Returns:
        A list of single-digit integers representing the digits of the next
        palindromic number.
    """
    high_mid = len(digits) // 2
    low_mid = (len(digits) - 1) // 2
    while high_mid < len(digits) and low_mid >= 0:
        if digits[high_mid] == 9:
            digits[high_mid] = 0
            digits[low_mid] = 0
            high_mid += 1
            low_mid -= 1
        else:
            digits[high_mid] += 1
            if low_mid != high_mid:
                digits[low_mid] += 1
            return digits
    return [1] + len(digits) * [0] + [1]


def assemble(digits):
    """
    Assemble a list of digits into an integer.

    Given a list of single-digit integers representing the digits of a possibly
    multi-digit integer, return the integer corresponding to those digits. As an
    example the list [1, 2, 3] would be assembled into the integer 123.

    Args:
        digits: A list of ints representing the digits of the number to
            assemble.

    Returns:
        An int representing the number assembled from digits.
    """
    integer = 0
    for digit in digits:
        integer = integer * 10 + digit
    return integer


def next_palindrome(palindromic_int):
    """
    Given a positive integer whose digits are a palindrome, find the next number
    whose digits are a palindrome.

    Given a palindromic integer (whose digits are the same forwards and
    backwards), find the next number (in increasing order) that is a palindromic
    integer. For example, if the starting palindromic integer is 292, the next
    palindromic integer is 303.

    Note that this function does not behave correctly if the integer argument is
    negative or not palindromic.

    Args:
        palindromic_int: An int representing a palindromic integer.

    Returns:
        An int representing the next palindromic integer.
    """
    digits = digit_list(palindromic_int)
    next_digits = next_palindrome_digits(digits)
    return assemble(next_digits)
