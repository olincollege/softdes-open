"""
Various checkers for password strength.

This module contains a variety of functions that can be used to check passwords
for various sets of passwords rules, such as not using common blocklisted
passwords, using passwords of a certain length, or ensuring the use of various
character types in passwords. These functions can be used in conjunction to
provide more complex password checking.
"""

from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def not_common_password(password):
    """
    Check that a password is not one of the three most common passwords.

    Check whether or not the password is one of the three most common
    passwords: 123456, qwerty, or password. If the password does not match any
    of these, return True, and False otherwise.

    Args:
        password: A string representing the password to check.

    Returns:
        True if the password does not match any of the three common passwords
        and False otherwise.
    """
    pass


def meets_length_restriction(password):
    """
    Check that a password's length is between 6 and 16 characters (inclusive).

    Args:
        password: A string representing the password to check.

    Returns:
        True if the password is between 6 and 16 characters and False
        otherwise.
    """
    pass


def count_occurrences_in_string(target, characters_to_count):
    """
    Count how many characters from a target string appear in another string.

    Given a target string and a string representing characters to count, count
    and return the number of characters in the target appear in the set of
    characters to count.

    As an example, if the target is "aaaabbcdef" and the set of characters to
    count is "bcd", then return 4, since "b" shows up twice in the target and
    "c" and "d" each show up once.

    Args:
        target: A string representing the target string.
        characters_to_count: A string representing the characters to count in
            the target string.

    Returns:
        An integer representing the number of characters in the target string
        that appear in the set of characters to count.
    """
    occurrences = 0
    for character in target:
        if character in characters_to_count:
            occurrences += 1
    return occurrences


def uses_all_character_classes(password):
    """
    Check that a password uses at least one character in each character class.

    Check whether or not the given password contains at least one character in
    each of four character classes: lowercase letters, uppercase letters,
    numbers, and punctuation.

    Args:
        password: A string representing the password to check.

    Returns:
        True if the password contains at least one character in each class and
        False otherwise.
    """
    pass


def long_enough_or_all_rules(password):
    """
    Check that either a password is longer than 16 characters, or that it meets
    all of the other rules.

    Check whether or not the given password is strictly longer than 16
    characters, or that it matches all three of the other rules:

    * It is not one of the three most common passwords.
    * It is between 6 and 16 characters, inclusive.
    * It uses at least one character in each character class.

    The password is considered to pass this check if it satisfies either of
    these two criteria (long enough, or matches all other rules).

    Args:
        password: A string representing the password to check.

    Returns:
        True if the password is long enough or if it matches the three rules
        described above, and False otherwise.
    """
    pass
