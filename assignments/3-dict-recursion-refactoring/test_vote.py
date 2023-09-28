"""
Test that the single transferable voting code is working properly.
"""
import random
import pytest

from vote import hold_alternative_vote


def alice_bob_votes(alice=0, bob=0, alice_bob=0, bob_alice=0):
    """
    Make a set of ranked votes for two candidates.

    Args:
        alice: The number of votes for just Alice.
        bob: The number of votes for just Bob.
        alice_bob: The number of votes for Alice, then Bob.
        bob_alice: The number of votes for Bob, then Alice.

    Returns:
        A list of lists representing votes for Alice and Bob.
    """
    votes = []
    votes += [["Alice"] for _ in range(alice)]
    votes += [["Bob"] for _ in range(bob)]
    votes += [["Alice", "Bob"] for _ in range(alice_bob)]
    votes += [["Bob", "Alice"] for _ in range(bob_alice)]
    return votes


# Defining and using this fixture in other functions will cause a pylint error
# by default, so suppress it here.
# pylint: disable=redefined-outer-name
@pytest.fixture(
    params=[
        # Unanimously chosen winner with all votes ranking the winner higher.
        (["Alice", "Bob"], alice_bob_votes(alice_bob=100), ("Alice", 100)),
        # Unanimously chosen with no votes for the other candidate.
        (["Alice", "Bob"], alice_bob_votes(bob=100), ("Bob", 100)),
        # Unanimously chosen with a mix of votes.
        (
            ["Alice", "Bob"],
            alice_bob_votes(alice=50, alice_bob=50),
            ("Alice", 100),
        ),
        # Winner by one vote with only ranked votes.
        (
            ["Alice", "Bob"],
            alice_bob_votes(alice_bob=50, bob_alice=51),
            ("Bob", 51),
        ),
        # Winner by one vote with only single votes.
        (["Alice", "Bob"], alice_bob_votes(alice=51, bob=50), ("Alice", 51)),
        # Winner by one vote with mixed votes.
        (
            ["Alice", "Bob"],
            alice_bob_votes(alice=25, bob=25, alice_bob=25, bob_alice=26),
            ("Bob", 51),
        ),
    ]
)
def simple_majority(request):
    """
    Fixture used to provide test cases for a simple majority election.

    Args:
        request: A Pytest request instance representing the requesting test.

    Returns:
        A tuple representing the parameters to pass to hold_alternative_vote.
    """
    return request.param


# Defining and using this fixture in other functions will cause a pylint error
# by default, so suppress it here.
# pylint: disable=redefined-outer-name
@pytest.fixture(params=[True, False])
def shuffle_votes(request):
    """
    Fixture used to control whether votes are shuffled or not.

    Args:
        request: A Pytest request instance representing the requesting test.

    Returns:
        A boolean representing whether to shuffle votes before testing.
    """
    return request.param


def test_simple_runoff(simple_majority, shuffle_votes):
    """
    Test a simple majority election.

    Args:
        simple_majority: A tuple of candidates and votes representing the
            parameters to pass to hold_alternative_vote.
        shuffle_votes: A boolean indicating whether to randomly shuffle the
            order of votes or not.
    """
    candidates, votes, winner = simple_majority

    # Shuffling votes around shouldn't change the results at all, but check
    # to see if it does.
    if shuffle_votes:
        random.shuffle(votes)

    assert hold_alternative_vote(candidates, votes) == winner


# Defining and using this fixture in other functions will cause a pylint error
# by default, so suppress it here.
# pylint: disable=redefined-outer-name
@pytest.fixture(
    params=[
        # Tie with single votes.
        (["Alice", "Bob"], alice_bob_votes(alice=150, bob=150)),
        # Tie with ranked votes.
        (["Alice", "Bob"], alice_bob_votes(alice_bob=75, bob_alice=75)),
        # Tie with mixed votes.
        (
            ["Alice", "Bob"],
            alice_bob_votes(alice=50, bob=50, alice_bob=50, bob_alice=50),
        ),
    ]
)
def simple_tie(request):
    """
    Fixture used to provide test cases for a simple tie election.

    Args:
        request: A Pytest request instance representing the requesting test.

    Returns:
        A tuple representing the parameters to pass to hold_alternative_vote.
    """
    return request.param


def test_simple_tie(simple_tie, shuffle_votes):
    """
    Test that in the case of a tie, a candidate is returned with the correct
    number of votes.

    Args:
        simple_tie: A tuple of candidates and votes representing the parameters
            to pass to hold_alternative_vote.
        shuffle_votes: A boolean indicating whether to randomly shuffle the
            order of votes or not.
    """
    candidates, votes = simple_tie

    # Shuffling votes around shouldn't change the results at all, but check
    # to see if it does.
    if shuffle_votes:
        random.shuffle(votes)

    winner, votes = hold_alternative_vote(candidates, votes)
    assert winner in ["Alice", "Bob"]
    assert votes == 150


def test_transfer_votes(shuffle_votes):
    """
    Test an election in which votes are transferred once.

    Args:
        shuffle_votes: A boolean indicating whether to randomly shuffle the
            order of votes or not.
    """
    votes = []
    votes += [["Bob", "Alice", "Charlie"] for _ in range(50)]
    votes += [["Charlie", "Alice", "Bob"] for _ in range(26)]
    votes += [["Alice", "Charlie", "Bob"] for _ in range(25)]

    if shuffle_votes:
        random.shuffle(votes)

    assert hold_alternative_vote(["Alice", "Bob", "Charlie"], votes) == (
        "Charlie",
        51,
    )


def test_three_way_majority(shuffle_votes):
    """
    Test a three-way election where one candidate has an absolute majority.

    Args:
        shuffle_votes: A boolean indicating whether to randomly shuffle the
            order of votes or not.
    """
    votes = []
    votes += [["Bob", "Alice", "Charlie"] for _ in range(51)]
    votes += [["Charlie", "Alice", "Bob"] for _ in range(25)]
    votes += [["Alice", "Bob", "Charlie"] for _ in range(25)]

    if shuffle_votes:
        random.shuffle(votes)

    assert hold_alternative_vote(["Alice", "Bob", "Charlie"], votes) == (
        "Bob",
        51,
    )


def test_double_transfer(shuffle_votes):
    """
    Test an election in which votes get transferred twice.

    Args:
        shuffle_votes: A boolean indicating whether to randomly shuffle the
            order of votes or not.
    """
    cand_1 = "Memphis"
    cand_2 = "Nashville"
    cand_3 = "Chattanooga"
    cand_4 = "Knoxville"
    candidates = [cand_1, cand_2, cand_3, cand_4]
    votes = [[cand_1, cand_2, cand_3, cand_4] for _ in range(42)]
    votes += [[cand_2, cand_3, cand_4, cand_1] for _ in range(26)]
    votes += [[cand_3, cand_4, cand_2, cand_1] for _ in range(15)]
    votes += [[cand_4, cand_3, cand_2, cand_1] for _ in range(17)]

    if shuffle_votes:
        random.shuffle(votes)

    assert hold_alternative_vote(candidates, votes) == ("Knoxville", 58)
