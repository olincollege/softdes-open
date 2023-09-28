"""
Check the correctness of the look-and-say sequence.
"""
# Import all required libraries.
import pytest

# Import the student's submitted code.
from sequence import next_number, look_and_say


LOOK_AND_SAY = [
    1,
    11,
    21,
    1211,
    111221,
    312211,
    13112221,
    1113213211,
    31131211131221,
    13211311123113112211,
    11131221133112132113212221,
    3113112221232112111312211312113211,
    1321132132111213122112311311222113111221131221,
    11131221131211131231121113112221121321132132211331222113112211,
]


@pytest.mark.parametrize("index", range(len(LOOK_AND_SAY) - 1))
def test_next_number(index):
    """
    Check that the submitted code correctly calculates the next number in the
    look-and-say sequence.

    Args:
        index: An integer representing the index of the look-and-say sequence to
            pass to the function to calculate the next number.
    """
    assert next_number(LOOK_AND_SAY[index]) == LOOK_AND_SAY[index + 1]


@pytest.mark.parametrize("steps", range(len(LOOK_AND_SAY) + 1))
def test_look_and_say(steps, capsys):
    """
    Check that the submitted code correctly prints the numbers of the look-and-
    say sequence.

    Args:
        steps: An integer representing the number of steps of the look-and-say
            sequence to print.
    """
    look_and_say(steps)
    output = capsys.readouterr()
    assert output.out.strip() == "\n".join(map(str, LOOK_AND_SAY[:steps]))
