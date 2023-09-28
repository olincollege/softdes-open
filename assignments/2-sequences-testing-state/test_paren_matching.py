"""
Check that parenthesis matching implementations are correct.
"""
import marshal
import pytest


# Add your test cases here.
UNIT_TEST_CASES = [
    # Check that a simple pair of parentheses is accepted.
    ("()", True),
    # Check that a pair of parentheses in the wrong order is rejected.
    (")(", False),
]


# Don't change anything below this line.
# NOTE: This is somewhat hacky code to make things work, so some aspects of the
#       style in this code is definitely not up to the usual standard. Don't
#       use the style of this code as a model for your own!
def correct_solution(string):
    """
    Check whether a string of parentheses is correctly matched.

    Args:
        string: A string of parentheses to check.

    Returns:
        True if the parentheses in string are matched, and False otherwise.
    """
    count = 0
    for char in string:
        if char == "(":
            count += 1
        elif count == 0:
            return False
        else:
            count -= 1
    return count == 0


# Define implementations here.
IMPL_COUNT = 14
IMPLEMENTATIONS = [f"compiled/impl_{i}.dat" for i in range(IMPL_COUNT)]

for filename in IMPLEMENTATIONS:
    with open(filename, "rb") as f:
        exec(marshal.load(f))  # pylint: disable=exec-used

FUNCTIONS = [
    ("correct", correct_solution),
    ("0", impl_0),  # pylint: disable=undefined-variable
    ("1", impl_1),  # pylint: disable=undefined-variable
    ("2", impl_2),  # pylint: disable=undefined-variable
    ("3", impl_3),  # pylint: disable=undefined-variable
    ("4", impl_4),  # pylint: disable=undefined-variable
    ("5", impl_5),  # pylint: disable=undefined-variable
    ("6", impl_6),  # pylint: disable=undefined-variable
    ("7", impl_7),  # pylint: disable=undefined-variable
    ("8", impl_8),  # pylint: disable=undefined-variable
    ("9", impl_9),  # pylint: disable=undefined-variable
    ("10", impl_10),  # pylint: disable=undefined-variable
    ("11", impl_11),  # pylint: disable=undefined-variable
    ("12", impl_12),  # pylint: disable=undefined-variable
    ("13", impl_13),  # pylint: disable=undefined-variable
]

assert IMPL_COUNT == len(FUNCTIONS) - 1


def function_id(fixture_value):
    """
    Get the identifier of a function name from a Pytest fixture value.
    """
    return fixture_value[0]


@pytest.fixture(params=FUNCTIONS, ids=function_id)
def implementation(request):
    """
    Get a specific implementation of a parenthesis matching checker.
    """
    return request.param


def case_id(fixture_value):
    """
    Create a test case identifier to display in Pytest output.
    """
    return f"{fixture_value[0]}-{fixture_value[1]}"


@pytest.fixture(params=UNIT_TEST_CASES, ids=case_id)
def unit_test_case(request):
    """
    Get a specific test case identifier.
    """
    return request.param


def test_correctness(implementation, unit_test_case):  # pylint: disable=redefined-outer-name, line-too-long
    """
    Check that an implementation of parenthesis match checking passes a test
    case.
    """
    string, matches = unit_test_case
    assert implementation[1](string) == matches
