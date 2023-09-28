"""
Check the correctness of password checkers.
"""
# Import all required libraries.
from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation,
)
import pytest

# Import the student's submitted code.
from password import (
    not_common_password,
    meets_length_restriction,
    uses_all_character_classes,
    long_enough_or_all_rules,
)


@pytest.mark.parametrize(
    "password,passes_check",
    [
        # Check that common passwords are rejected.
        ("123456", False),
        ("qwerty", False),
        ("password", False),
        # Check that case alterations of common passwords are accepted.
        ("QWERTY", True),
        ("PaSsWoRd", True),
        # Check that passwords *containing* common passwords are fine.
        ("12345678", True),
        ("asdfqwerty", True),
        ("ilovepasswords", True),
        # Check that passwords not matching the common passwords are fine.
        ("iloveyou", True),
        ("letmein", True),
        ("000000", True),
        ("TROGDOR the BURNiNATOR", True),
    ],
)
def test_not_common_password(password, passes_check):
    """
    Check that the password checker rejects one of the three common passwords
    and accepts all others.

    Args:
        password: A string representing the password to check.
        passes_check: A bool representing the expected output of the checker.
    """
    assert not_common_password(password) == passes_check


@pytest.mark.parametrize(
    "password,passes_check",
    [
        # Check that too short of a password is rejected.
        ("", False),
        ("abc", False),
        # Check that too long of a password is rejected.
        ("a" * 17, False),
        # Check that exactly 6 characters is accepted.
        ("0" * 6, True),
        # Check that exactly 16 characters is accepted.
        ("1" * 16, True),
    ],
)
def test_meets_length_restriction(password, passes_check):
    """
    Check that the password checker only accepts passwords between 6 and 16
    characters long, inclusive.

    Args:
        password: A string representing the password to check.
        passes_check: A bool representing the expected output of the checker.
    """
    assert meets_length_restriction(password) == passes_check


@pytest.mark.parametrize(
    "password,passes_check",
    [
        # Check that an empty string is rejected.
        ("", False),
        # Check that a password only missing lowercase letters is rejected.
        ("A1!", False),
        # Check that a password only missing uppercase letters is rejected.
        ("00:1a:7d:da:71:10", False),
        # Check that a password only missing digits is rejected.
        ("zomgCamelCase!!", False),
        # Check that a password only missing punctuation is rejected.
        ("LaTeX2e", False),
        # Check that a password containing all four character classes is accepted.
        (ascii_lowercase + ascii_uppercase + digits + punctuation, True),
        # Check that a password containing all four character classes, as well as
        # characters not in any of the four classes, is accepted.
        ("Charlie, DOB 1/1/1947", True),
    ],
)
def test_uses_all_character_classes(password, passes_check):
    """
    Check that the password checker only accepts passwords that use at least one
    character each in lowercase letters, uppercase letters, digits, and
    punctuation.

    Args:
        password: A string representing the password to check.
        passes_check: A bool representing the expected output of the checker.
    """
    assert uses_all_character_classes(password) == passes_check


@pytest.mark.parametrize(
    "password,passes_check",
    [
        # Check that an empty string is rejected.
        ("", False),
        # Check that a password of exactly 16 characters that does not match all
        # three other checkers is rejected.
        ("0123456789abcdef", False),
        # Check that a password of at most 16 characters, but a common password, is
        # rejected.
        ("password", False),
        # Check that a password shorter than 6 characters is rejected.
        ("pytho", False),
        # Check that a password of at most 16 characters, not a common password,
        # at least 6 characters, but not containing all four character classes, is
        # rejected.
        ("diamond hands", False),
        # Check that a password containing all four character classes, and between 6
        # and 16 characters (inclusive) is accepted.
        ("/r/TF2", True),
        # Check that a password longer than 16 characters, but not matching all
        # three other checkers, is accepted.
        ("longer than 16 characters, oh yeah", True),
    ],
)
def test_long_enough_or_all_rules(password, passes_check):
    """
    Check that the password checker only accepts passwords that are longer than
    16 characters, or that pass all of the other checkers.

    Args:
        password: A string representing the password to check.
        passes_check: A bool representing the expected output of the checker.
    """
    assert long_enough_or_all_rules(password) == passes_check
