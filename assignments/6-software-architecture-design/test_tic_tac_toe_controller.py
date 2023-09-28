"""
Unit tests for tic-tac-toe controller.
"""
import io
import pytest
from tic_tac_toe_board import TicTacToeBoard
from tic_tac_toe_controller import TextController
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
    Test that the TextController and TicTacToeController classes are structured
    correctly (i.e., that they have the proper methods and attributes).

    Args:
        func: A function that takes a class and a string representing a method
            name and returns a boolean, used to test various functionality of
            the tic-tac-toe controller
    """
    assert func(TextController, "move")


@pytest.fixture
def board():
    """
    Create a tic tac toe board for use in testing.
    """
    return TicTacToeBoard()


# Test cases for move. Since the prompt repeats until given an valid input, each
# sequence ends with a valid input.
move_cases = [
    # Single valid move.
    ("0 0", {(0, 0): TicTacToeBoard.player_1_mark}),
    # Multiple valid moves.
    ("0 0\n1 1", {(0, 0): TicTacToeBoard.player_1_mark,
                  (1, 1): TicTacToeBoard.player_2_mark}),
    # Only one index given.
    ("1\n0 0", {(0, 0): TicTacToeBoard.player_1_mark}),
    # Non-numerical input.
    ("0 abc\nabc 0\nabc def\n0 0", {(0, 0): TicTacToeBoard.player_1_mark}),
    # Row or column index too large.
    ("0 3\n3 0\n3 3\n0 0", {(0, 0): TicTacToeBoard.player_1_mark}),
    # Row or column index negative.
    ("0 -1\n-1 0\n-1 -1\n0 0", {(0, 0): TicTacToeBoard.player_1_mark}),
    # Square already taken.
    ("0 0\n0 0\n1 1", {(0, 0): TicTacToeBoard.player_1_mark,
                       (1, 1): TicTacToeBoard.player_2_mark}),
]


@pytest.fixture(params=move_cases)
def move_case(request):
    """
    Provide a pair of text input to the move method of the controller and the
    expected board state.
    """
    return request.param


def test_draw(board, move_case, monkeypatch):  # pylint: disable=redefined-outer-name
    """
    Test that the board is correctly represented as a string in different
    conditions.

    Args:
        board: The TicTacToeBoard instance to use.
        move_case: A tuple consisting of a string representing input to the move
            method of the TextController instance used, and a dictionary mapping
            (row, col) tuples to the expected mark found there after the input
            has been consumed by the controller (the default mark is assumed to
            be blank).
    """
    controller = TextController(board)
    user_input, check_squares = move_case
    valid_moves = 0

    # Patch standard input to pass the text in user_input to the move method.
    monkeypatch.setattr("sys.stdin", io.StringIO(user_input))

    # Consume all input until none is left, using it to make moves in the game.
    try:
        while True:
            controller.move()
            valid_moves += 1
    except EOFError:
        pass

    # Check that the move method was called the appropriate number of times.
    assert valid_moves == len(check_squares)

    # Check that the board contains exactly the correct marks.
    for row in range(3):
        for col in range(3):
            if (row, col) in check_squares:
                assert board.get_square(row, col) == check_squares[(row, col)]
            else:
                assert board.get_square(row, col) == TicTacToeBoard.blank_mark
