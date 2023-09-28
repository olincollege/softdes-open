"""
Common tests used to test multiple components of the tic-tac-toe game.
"""
from tic_tac_toe_board import TicTacToeBoard


def _is_private_variable(class_name, var_name):
    """
    Check if a variable name is private in a class.

    Given a class and variable name, check whether that variable name is a
    private variable. A variable name is considered private if it begins with
    exactly one underscore (_) and is not a class-private variable (in the form
    _Class__var).

    Args:
        class_name: A class used to derive the comparison string for the
            class-private variable name.
        var_name: A string representing the variable name.

    Returns:
        True if var_name is a private variable in class_name and False
        otherwise.
    """
    return (var_name.startswith("_")
            and not var_name.startswith("__")
            and not var_name.startswith(f"_{class_name.__name__}"))


def check_private_board(class_name, _):
    """
    Check whether a class has at least one private variable.

    Private variables are determined as defined in the _is_private_variable
    function.

    Args:
        class_name: A class to check for private variables.

    Returns:
        True if the class has at least one private variable and False otherwise.
    """
    board = TicTacToeBoard()
    instance = class_name(board)
    private_variables = [attr for attr in dir(instance)
                         if _is_private_variable(class_name, attr)]
    return len(private_variables) >= 1


def check_board_attribute(class_name, _):
    """
    Check whether a class has an attribute called "board".

    Args:
        class_name: A class to check for the board attribute.
    """
    return hasattr(class_name, "board")


def check_board_property(class_name, _):
    """
    Check whether TicTacToeView has a property called board (created with the
    property decorator).

    Args:
        class_name: A class to check for the board property.
    """
    return isinstance(class_name.board, property)


def equal(board_1, board_2):
    """
    Check that two TicTacToeBoard instances are equal by value.

    Part of testing involves checking that two boards are equal, but the
    TicTacToeBoard class does not have an __eq__ method, and comparing memory
    addresses using is may not always work (if a solution makes a copy of the
    board squares, somehow). Thus, the board contents and next moves should be
    compared by value.

    Args:
        board_1: A TicTacToeBoard instance representing one of the boards to
            compare.
        board_2: A TicTacToeBoard instance representing one of the boards to
            compare.

    Returns:
        True if the boards contain the same content and False otherwise.
    """
    if board_1 is board_2:
        return True
    if board_1.next_move() != board_2.next_move():
        return False
    for row in range(3):
        for col in range(3):
            if board_1.get_square(row, col) != board_2.get_square(row, col):
                return False
    return True


def check_board_assignment(class_name, _):
    """
    Check that the board used when creating a component instance is the one
    stored in the instance.

    Args:
        class_name: A class to check for proper board attribute assignment.
    """
    board = TicTacToeBoard()
    instance = class_name(board)
    return equal(instance.board, board)


def check_core_method(class_name, method_name):
    """
    Check that a class has a method.

    Args:
        class_name: A class to check.
        method_name: A string representing the method name to check for.
    """
    return hasattr(class_name, method_name)


def check_abstract_method(class_name, method_name):
    """
    Check that a class's method is abstract.

    Args:
        class_name: A class to check.
        method_name: A string representing a method name to check as an abstract
            method (i.e., whether it has __abstractmethod__ set to True).
    """
    method = getattr(class_name.__base__, method_name)
    return (hasattr(method, "__isabstractmethod__")
            and method.__isabstractmethod__)
