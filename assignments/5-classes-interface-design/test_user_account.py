"""
Unit tests for Sleepy Follow user account class.
"""
import pytest
from user_account import UserAccount


def check_username_exists(username):
    """
    Check that a user has the username property.

    Args:
        username: A string representing the user's username.

    Returns:
        True if user.username exists and False otherwise.
    """
    user = UserAccount(username)
    return hasattr(user, "username")


def check_username_match(username):
    """
    Check that a user account is created with the correct username.

    Args:
        username: A string representing the user's username.

    Returns:
        True if user.username is equal to username and False otherwise.
    """
    user = UserAccount(username)
    return user.username == username


def check_username_property(_):
    """
    Check that the UserAccount class has username as a property.

    Returns:
        True if username is a property of the UserAccount class and False
        otherwise.
    """
    # In an instance, the username property will show up as the type of the
    # underlying attribute (string) rather than as a property, so this needs
    # to be checked at the class level to ensure that it is a property and not
    # an instance variable.
    return isinstance(UserAccount.username, property)


def _is_private_variable(var_name):
    """
    Check if a variable name is private in the UserAccount class.
    """
    return (var_name.startswith("_")
            and not var_name.startswith("__")
            and not var_name.startswith("_UserAccount"))


def check_private_variables(username):
    """
    Check if a UserAccount instance has the correct number of private
    variables.

    Args:
        username: A string representing the user's username.

    Returns:
        True if the user has at least two private instance attributes and False
        otherwise.
    """
    user = UserAccount(username)
    private_variables = [attr for attr in dir(user)
                         if _is_private_variable(attr)]
    return len(private_variables) >= 2


@pytest.mark.parametrize("func", [check_username_exists,
                                  check_username_match,
                                  check_username_property,
                                  check_private_variables])
def test_instance_attributes(func):
    """
    Check that the instance attributes are set correctly.

    This is used to test Problem 2.1 (@property Value).

    Args:
        func: A function that takes a string and returns a boolean, used to
            test the instance attributes of the refactored code.
    """
    assert func("")


def check_post_dict():
    """
    Check that a user's posts are stored as a dictionary.
    """
    user = UserAccount("")
    return isinstance(user._posts, dict)  # pylint: disable=protected-access


def check_get_post():
    """
    Check that a user's posts can be retrieved with the post ID.
    """
    user = UserAccount("OlinCommunityCollege")
    post_id = "Ib-4vBKoaNAaMW7VTO14DiTJwqoGTNq5uaHwbpnEYcM"
    post_text = "Hello World!"
    user.post(post_text)
    return user.get_post(post_id) == (post_id, post_text)


def check_none_post():
    """
    Check that a get_post returns None for a nonexisting post ID.
    """
    user = UserAccount("")
    user.post("")
    return user.get_post("") is None


def check_no_posts():
    """
    Check that a new user account reports 0 posts.
    """
    user = UserAccount("")
    return user.num_posts() == 0


def check_one_post():
    """
    Check that making a post increments the number of posts.
    """
    user = UserAccount("")
    user.post("")
    return user.num_posts() == 1


@pytest.mark.parametrize("func", [check_post_dict,
                                  check_get_post,
                                  check_none_post,
                                  check_no_posts,
                                  check_one_post])
def test_post_history(func):
    """
    Check that the user's post history is set correctly.

    This is used to test Problem 2.2 (A-dict-ed to Refactoring).

    Args:
        func: A function that returns a boolean, used to test various
             functionality of the user's post history.
    """
    assert func()


def check_no_generate_method():
    """
    Check that the UserAccount class does not have a generate_new_post_id
    method.
    """
    return not hasattr(UserAccount, "generate_new_post_id")


def check_generate_function():
    """
    Check that the generate_new_post_id exists as a function external to the
    UserAccount class.
    """
    try:
        from user_account import generate_new_post_id  # pylint: disable=import-outside-toplevel
        return True
    except ImportError:
        return False


def check_generate_correctness():
    """
    Check that the generate_new_post_id function works as intended.
    """
    from user_account import generate_new_post_id  # pylint: disable=import-outside-toplevel
    user = UserAccount("OlinCommunityCollege")
    expected_post_id = "Ib-4vBKoaNAaMW7VTO14DiTJwqoGTNq5uaHwbpnEYcM"
    return generate_new_post_id(user) == expected_post_id


@pytest.mark.parametrize("func", [check_no_generate_method,
                                  check_generate_function,
                                  check_generate_correctness])
def test_post_id(func):
    """
    Check that post IDs are generated correctly.

    This is used to test Problem 2.3 (Moving the Post Goals).

    Args:
        func: A function that returns a boolean, used to test various
             functionality of the user's post history.
    """
    assert func()
