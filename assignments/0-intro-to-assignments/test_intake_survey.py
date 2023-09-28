"""
Check the validity of the intake survey responses (to the extent possible).
"""
# Import all required libraries.
import pytest

# Import the student's responses from their filled-in survey.
import intake_survey


def test_name_filled_in():
    """
    Ensure that the student's preferred name is filled in.
    """
    assert isinstance(intake_survey.preferred_name, str)
    assert intake_survey.preferred_name


def test_pronouns_is_string():
    """
    Ensure that the student's pronouns is of the correct data type (even if
    empty).
    """
    assert isinstance(intake_survey.pronouns, str)


@pytest.mark.parametrize("response", [
    pytest.param(intake_survey.previous_programming_experience,
                 id="programming_experience"),
    pytest.param(intake_survey.previous_python_experience,
                 id="python_experience"),
    pytest.param(intake_survey.previous_tools_experience,
                 id="tools_experience"),
])
def test_experience_level_filled_in(response):
    """
    Check that the student's level of experience is a valid integer.

    Args:
        response: the student's reported experience level.
    """
    assert isinstance(response, int)
    assert 1 <= response <= 5


@pytest.mark.parametrize("responses", [
    pytest.param(intake_survey.learning_goals, id="learning_goals"),
    pytest.param(intake_survey.concerns, id="concerns"),
])
def test_longform_responses_filled_in(responses):
    """
    Check that the student wrote at least one learning goal and concern.

    Args:
        responses: a list of strings representing the student's responses.
    """
    # Check that only strings appear in the set of responses.
    assert all(map(lambda response: isinstance(response, str), responses))
    # Check that the list contains at least one non-empty string.
    assert [response for response in list(responses) if response]
