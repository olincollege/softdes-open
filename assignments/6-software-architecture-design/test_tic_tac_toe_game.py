"""
Unit tests for tic-tac-toe controller.
"""
import io
import sys
import pytest
from tic_tac_toe_game import main


# Test cases for game, consisting of a sequence of moves and a number of "extra"
# moves that the game should not take as input (0 if the game should take all
# moves as input).
game_cases = [
    # Standard game where X wins.
    ([(0, 0), (2, 0), (0, 1), (1, 1), (0, 2)], 0),
    # Standard game where O wins.
    ([(0, 0), (1, 0), (2, 1), (1, 1), (0, 2), (1, 2)], 0),
    # Standard game ending in a draw.
    ([(1, 1), (0, 0), (2, 0), (0, 2), (0, 1), (2, 1), (1, 0), (1, 2), (2, 2)],
     0),
    # X win with extra moves left over.
    ([(0, 0), (2, 0), (0, 1), (1, 1), (0, 2), (1, 0), (2, 2)], 2),
    # O win with extra moves left over.
    ([(0, 0), (1, 0), (2, 1), (1, 1), (0, 2), (1, 2), (0, 1)], 1),
    # Draw with extra moves left over.
    ([(1, 1), (0, 0), (2, 0), (0, 2), (0, 1), (2, 1), (1, 0), (1, 2), (2, 2),
      (0, 0)], 1),
]


@pytest.fixture(params=game_cases)
def game_info(request):
    """
    Provide a pair of text input to the move method of the controller and the
    expected board state.
    """
    moves, extra_moves = request.param
    move_string = "\n".join(map(lambda move: " ".join(map(str, move)), moves))
    bytes_read = len(move_string)
    if extra_moves > 0:
        bytes_read += 1 - 4 * extra_moves
    return move_string, bytes_read


def test_game(game_info, monkeypatch):  # pylint: disable=redefined-outer-name
    """
    Test that a game of tic-tac-toe is played correctly.

    Args:
        game: A tuple consisting of a string representing input to the move
            method of the TextController instances used, and an integer
            specifying the appropriate number of bytes that should be read out
            of the string during the game.
    """
    move_string, bytes_read = game_info

    # Patch standard input to pass the text in user_input to the move method.
    monkeypatch.setattr("sys.stdin", io.StringIO(move_string))

    # Consume input until the game has completed, and check that the appropriate
    # amount of input was consumed.
    main()
    assert sys.stdin.tell() == bytes_read
