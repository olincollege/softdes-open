"""
Tic-tac-toe board implementation.
"""


class TicTacToeBoard:
    """
    Tic-tac-toe board with basic play functionality.

    Attributes:
        player_1_mark: A string representing the first player's symbol.
        player_2_mark: A string representing the second player's symbol.
        blank_mark: A string representing a blank square symbol.
        _board: A list of lists representing the squares of the board.
        _next_move: A string representing the symbol of the next player to
            move.
    """

    # Define class attributes for each player's symbol and for a blank square,
    # in case we ever want to change these later.
    player_1_mark = "X"
    player_2_mark = "O"
    blank_mark = " "

    def __init__(self):
        """
        Create a new, empty TicTacToeBoard.
        """
        # Writing the following ensures that each square of the board is
        # independent from each other. Writing something like
        # [[" "] * 3] * 3
        # will cause the board to be made up of copies of the same cell,
        # resulting in strange behavior.
        self._board = [[self.blank_mark for _ in range(3)] for _ in range(3)]
        self._next_move = self.player_1_mark

    def next_move(self):
        """
        Return the symbol (X or O) of the next player to move.

        Returns:
            A string representing the next player's mark (X or O).
        """
        return self._next_move

    def mark(self, row, col):
        """
        If possible, mark a given square of the board with the next player's
        move.

        Given a row and column index (each 0, 1, or 2), mark the corresponding
        square of the board with the next player's move. Assume that each index
        is within the appropriate bounds. If a player's mark already exists at
        the requested square, raise an error instead.

        Args:
            row: An int representing the index of the row of the board to mark.
            col: An int representing the index of the column of the board to
                mark.

        Raises:
            ValueError: if the requested square already has a player's mark.
        """
        if self.get_square(row, col) != self.blank_mark:
            raise ValueError
        self._board[row][col] = self._next_move

        # Change the next player to move here. An alternative would be to
        # calculate the next player to move based on the number of X's and O's
        # on the board, but this is easier.
        self._flip_next_move()

    def _flip_next_move(self):
        """
        Change the next player to move.
        """
        if self._next_move == self.player_1_mark:
            self._next_move = self.player_2_mark
        else:
            self._next_move = self.player_1_mark

    def _check_row_win(self, player):
        """
        Check whether the given player has won along a row of the board.

        Args:
            player: A string representing the player's symbol (X or O).

        Returns:
            True if player has won along any row of the board and False
            otherwise.
        """
        for row in range(3):
            if self._board[row][0] == self._board[row][1] \
               == self._board[row][2] == player:
                return True
        return False

    def _check_col_win(self, player):
        """
        Check whether the given player has won along a column of the board.

        Args:
            player: A string representing the player's symbol (X or O).

        Returns:
            True if player has won along any column of the board and False
            otherwise.
        """
        for col in range(3):
            if self._board[0][col] == self._board[1][col] \
               == self._board[2][col] == player:
                return True
        return False

    def _check_diag_win(self, player):
        """
        Check whether the given player has won along a diagonal of the board.

        Args:
            player: A string representing the player's symbol (X or O).

        Returns:
            True if player has won along a diagonal of the board and False
            otherwise.
        """
        # We use trace to refer to the diagonal from the upper left to the lower
        # right of the board.
        trace_win = True
        for i in range(3):
            if self._board[i][i] != player:
                trace_win = False
                break
        # We use trace to refer to the diagonal from the upper right to the
        # lower left of the board.
        cross_win = True
        for i in range(3):
            if self._board[i][2 - i] != player:
                cross_win = False
                break
        return trace_win or cross_win

    def check_win(self, player):
        """
        Check that a given player has won (has three in a row) anywhere on the
        board.

        Args:
            player: A string representing the player's symbol (X or O).

        Returns:
            True if player has won and False otherwise.
        """
        return (self._check_row_win(player) or self._check_col_win(player)
                or self._check_diag_win(player))

    def get_square(self, row, col):
        """
        Return the mark at the given square of the board.

        Args:
            row: An int representing the index of the row of the board to get.
            col: An int representing the index of the column of the board to
                get.

        Returns:
            A string representing the contents of the given square (X, O, or a
            space).
        """
        return self._board[row][col]

    def __repr__(self):
        """
        Return a string representing the contents of the board.
        """
        row_divider = "+-+-+-+"
        lines = [row_divider]
        for i in range(3):
            row = f"|{'|'.join(self._board[i])}|"
            lines.append(row)
            lines.append(row_divider)
        return "\n".join(lines)
