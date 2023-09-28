"""
Unit tests for tic-tac-toe view.
"""
import pytest
from tic_tac_toe_board import TicTacToeBoard
from tic_tac_toe_view import TextView
from test_common import (
    check_private_board,
    check_board_attribute,
    check_board_property,
    check_board_assignment,
    check_core_method,
    check_abstract_method,
)


@pytest.mark.parametrize("func", [check_private_board, check_board_attribute,
                                  check_board_property, check_board_assignment,
                                  check_core_method, check_abstract_method])
def test_view_classes(func):
    """
    Test that the TextView and TicTacToeView classes are structured correctly
    (i.e., that they have the proper methods and attributes).

    Args:
        func: A function that takes a class and a string representing a method
            name and returns a boolean, used to test various functionality of
            the tic-tac-toe view.
    """
    assert func(TextView, "draw")


board_reprs = [
    ([], "+-+-+-+\n"
         "| | | |\n"
         "+-+-+-+\n"
         "| | | |\n"
         "+-+-+-+\n"
         "| | | |\n"
         "+-+-+-+\n"
         "It is now X's turn."),
    ([(0, 0), (2, 0), (0, 1), (1, 1), (0, 2)], "+-+-+-+\n"
                                               "|X|X|X|\n"
                                               "+-+-+-+\n"
                                               "| |O| |\n"
                                               "+-+-+-+\n"
                                               "|O| | |\n"
                                               "+-+-+-+\n"
                                               "It is now O's turn."),
    ([(0, 0), (1, 0), (2, 1), (1, 1), (0, 2), (1, 2)], "+-+-+-+\n"
                                                       "|X| |X|\n"
                                                       "+-+-+-+\n"
                                                       "|O|O|O|\n"
                                                       "+-+-+-+\n"
                                                       "| |X| |\n"
                                                       "+-+-+-+\n"
                                                       "It is now X's turn."),
]


@pytest.fixture
def board():
    """
    Create a tic tac toe board for use in testing.
    """
    return TicTacToeBoard()


@pytest.fixture(params=board_reprs)
def game_repr(request):
    """
    Create a representation of a sequence of moves for use in testing.
    """
    return request.param


def test_draw(board, game_repr, capsys):  # pylint: disable=redefined-outer-name
    """
    Test that the board is correctly represented as a string in different
    conditions.

    Args:
        board: The TicTacToeBoard instance to use.
        game_repr: A tuple where the first element is a list of moves to be made
            in the game, and the second element is a string representing the
            expected string representation of the board after those moves have
            been made.
    """
    moves, board_repr = game_repr
    for row, col in moves:  # pylint: disable=redefined-outer-name
        board.mark(row, col)
    view = TextView(board)
    view.draw()
    assert capsys.readouterr().out.strip() == board_repr
