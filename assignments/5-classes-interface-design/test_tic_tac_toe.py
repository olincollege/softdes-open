"""
Unit tests for tic-tac-toe board.
"""
import pytest
from tic_tac_toe import TicTacToeBoard


@pytest.fixture
def board():
    """
    Create a tic tac toe board for use in testing.
    """
    return TicTacToeBoard()


@pytest.fixture(params=["X", "O"])
def player(request):
    """
    Create a player for use in testing.
    """
    return request.param


@pytest.fixture(params=range(3))
def row(request):
    """
    Create a row index for use in testing.
    """
    return request.param


@pytest.fixture(params=range(3))
def col(request):
    """
    Create a column index for use in testing.
    """
    return request.param


board_moves = [
    # Games that result in a horizontal win.
    ([(0, 0), (2, 0), (0, 1), (1, 1), (0, 2)], "X"),
    ([(0, 0), (1, 0), (2, 1), (1, 1), (0, 2), (1, 2)], "O"),
    ([(2, 0), (0, 0), (2, 1), (1, 1), (2, 2)], "X"),
    # Games that result in a vertical win.
    ([(0, 2), (0, 0), (1, 1), (2, 0), (2, 2), (1, 0)], "O"),
    ([(0, 1), (0, 0), (1, 1), (1, 2), (2, 1)], "X"),
    ([(0, 0), (0, 2), (2, 0), (1, 2), (1, 1), (2, 2)], "O"),
    # Games that result in a diagonal win.
    ([(0, 0), (0, 2), (1, 1), (1, 2), (2, 2)], "X"),
    ([(0, 0), (2, 0), (1, 0), (1, 1), (2, 2), (0, 2)], "O"),
    # Games that result in a draw.
    ([(0, 0), (1, 1), (2, 2), (0, 1), (2, 1), (2, 0), (0, 2), (1, 2), (1, 0)],
     None),
]


@pytest.fixture(params=board_moves)
def game(request):
    """
    Create a sequence of moves representing a game for use in testing.
    """
    return request.param


board_reprs = [
    # Games that result in a horizontal win.
    ([(0, 0), (2, 0), (0, 1), (1, 1), (0, 2)], "+-+-+-+\n"
                                               "|X|X|X|\n"
                                               "+-+-+-+\n"
                                               "| |O| |\n"
                                               "+-+-+-+\n"
                                               "|O| | |\n"
                                               "+-+-+-+"),
    ([(0, 0), (1, 0), (2, 1), (1, 1), (0, 2), (1, 2)], "+-+-+-+\n"
                                                       "|X| |X|\n"
                                                       "+-+-+-+\n"
                                                       "|O|O|O|\n"
                                                       "+-+-+-+\n"
                                                       "| |X| |\n"
                                                       "+-+-+-+"),
    ([(2, 0), (0, 0), (2, 1), (1, 1), (2, 2)], "+-+-+-+\n"
                                               "|O| | |\n"
                                               "+-+-+-+\n"
                                               "| |O| |\n"
                                               "+-+-+-+\n"
                                               "|X|X|X|\n"
                                               "+-+-+-+"),
    # Games that result in a vertical win.
    ([(0, 2), (0, 0), (1, 1), (2, 0), (2, 2), (1, 0)], "+-+-+-+\n"
                                                       "|O| |X|\n"
                                                       "+-+-+-+\n"
                                                       "|O|X| |\n"
                                                       "+-+-+-+\n"
                                                       "|O| |X|\n"
                                                       "+-+-+-+"),
    ([(0, 1), (0, 0), (1, 1), (1, 2), (2, 1)], "+-+-+-+\n"
                                               "|O|X| |\n"
                                               "+-+-+-+\n"
                                               "| |X|O|\n"
                                               "+-+-+-+\n"
                                               "| |X| |\n"
                                               "+-+-+-+"),
    ([(0, 0), (0, 2), (2, 0), (1, 2), (1, 1), (2, 2)], "+-+-+-+\n"
                                                       "|X| |O|\n"
                                                       "+-+-+-+\n"
                                                       "| |X|O|\n"
                                                       "+-+-+-+\n"
                                                       "|X| |O|\n"
                                                       "+-+-+-+"),
    # Games that result in a diagonal win.
    ([(0, 0), (0, 2), (1, 1), (1, 2), (2, 2)], "+-+-+-+\n"
                                               "|X| |O|\n"
                                               "+-+-+-+\n"
                                               "| |X|O|\n"
                                               "+-+-+-+\n"
                                               "| | |X|\n"
                                               "+-+-+-+"),
    ([(0, 0), (2, 0), (1, 0), (1, 1), (2, 2), (0, 2)], "+-+-+-+\n"
                                                       "|X| |O|\n"
                                                       "+-+-+-+\n"
                                                       "|X|O| |\n"
                                                       "+-+-+-+\n"
                                                       "|O| |X|\n"
                                                       "+-+-+-+"),
    # Games that result in a draw.
    ([(0, 0), (1, 1), (2, 2), (0, 1), (2, 1), (2, 0), (0, 2), (1, 2), (1, 0)],
     "+-+-+-+\n"
     "|X|O|X|\n"
     "+-+-+-+\n"
     "|X|O|O|\n"
     "+-+-+-+\n"
     "|O|X|X|\n"
     "+-+-+-+"),
]


@pytest.fixture(params=board_reprs)
def game_repr(request):
    """
    Create a representation of a sequence of moves for use in testing.
    """
    return request.param


def test_first_move(board):  # pylint: disable=redefined-outer-name
    """
    Test that the first player to move is X.

    Args:
        board: The TicTacToeBoard instance to use.
    """
    assert board.next_move() == "X"


def test_next_move(board, game):  # pylint: disable=redefined-outer-name
    """
    Test that the board correctly selects the next player to move.

    Args:
        board: The TicTacToeBoard instance to use.
        game: A tuple whose first element is a list of moves to be made in the
            game, in order.
    """
    moves, _ = game
    players = ["X", "O"]
    for i in range(len(moves)):  # pylint: disable=consider-using-enumerate
        assert board.next_move() == players[i % 2]
        board.mark(*moves[i])


def test_mark_empty(board, row, col):  # pylint: disable=redefined-outer-name
    """
    Test that marking an empty square places does not return an error.

    Args:
        board: The TicTacToeBoard instance to use.
        row: An integer representing the row index.
        col: An integer representing the column index.
    """
    board.mark(row, col)
    assert True


def test_double_mark(board, row, col):  # pylint: disable=redefined-outer-name
    """
    Test that trying to mark the same square twice results in an error.

    Args:
        board: The TicTacToeBoard instance to use.
        row: An integer representing the row index.
        col: An integer representing the column index.
    """
    board.mark(row, col)
    with pytest.raises(ValueError):
        board.mark(row, col)


def test_no_initial_win(board, player):  # pylint: disable=redefined-outer-name
    """
    Test that at the start of the game, no player is winning.

    Args:
        board: The TicTacToeBoard instance to use.
        player: A string representing the player's symbol (X or O) to check.
    """
    assert not board.check_win(player)


def test_all_blank(board, row, col):  # pylint: disable=redefined-outer-name
    """
    Test that at the start of the game, all squares are blank.

    Args:
        board: The TicTacToeBoard instance to use.
        row: An integer representing the row index.
        col: An integer representing the column index.
    """
    assert board.get_square(row, col) == " "


def test_mark_result(board, row, col):  # pylint: disable=redefined-outer-name
    """
    Test that after marking an available square, the player's mark used is
    returned by get_square.

    Args:
        board: The TicTacToeBoard instance to use.
        row: An integer representing the row index.
        col: An integer representing the column index.
    """
    board.mark(row, col)
    assert board.get_square(row, col) == "X"


def test_check_win(board, game):  # pylint: disable=redefined-outer-name
    """
    Test that the board correctly detects wins in various conditions.

    Args:
        board: The TicTacToeBoard instance to use.
        game: A tuple where the first element is a list of moves to be made in
            the game, and the second element is a string representing the winner
            of the game after those moves (or None if the game ends with no
            winner).
    """
    moves, expected_winner = game
    for row, col in moves:  # pylint: disable=redefined-outer-name
        assert not board.check_win("X")
        assert not board.check_win("O")
        board.mark(row, col)
    if expected_winner is None:
        assert not board.check_win("X")
        assert not board.check_win("O")
    else:
        assert board.check_win(expected_winner)


def test_repr(board, game_repr):  # pylint: disable=redefined-outer-name
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
    assert str(board) == board_repr
