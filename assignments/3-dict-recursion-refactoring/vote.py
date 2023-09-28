"""
Calculate the winner of an IRV election.
"""


# Helper function. Feel free to use, but DON'T CHANGE.
def tally_votes(candidates, ranked_votes):
    """
    Calculate the number of votes received by each candidate in a round of an
    IRV election.

    Args:
        candidates: A list representing the candidates still in the race.
        ranked_votes: A list of lists representing ranked votes for candidates,
            with each vote from most to least preferred.

    Returns:
        A dictionary mapping candidates to the number of votes they received.
    """
    # Keep track of how many votes each candidate has.
    vote_counts = {candidate: 0 for candidate in candidates}

    for vote in ranked_votes:
        # This method of counting votes is likely the easiest way to tally up
        # votes in the grand scheme of things. An alternative is to take the
        # first candidate of each vote, but this requires you to go through and
        # edit all of the votes when you eliminate a candidate, which is more
        # work and rather error-prone.
        for candidate in vote:
            if candidate in candidates:
                vote_counts[candidate] += 1
                break
    return vote_counts


# Helper function. Feel free to use, but DON'T CHANGE.
def get_minimum_candidate(vote_counts):
    """
    Find and return the candidate who received the minimum number of votes.

    Args:
        vote_counts: A dictionary mapping candidates to the number of votes
            received in this round of the IRV election.

    Returns:
        A string representing the name of the candidate with the fewest votes.
    """
    minimum_candidate = None
    minimum_votes = None
    for candidate, num_votes in vote_counts.items():
        if minimum_votes is None or num_votes < minimum_votes:
            minimum_candidate = candidate
            minimum_votes = num_votes
    return minimum_candidate


def hold_alternative_vote(candidates, ranked_votes):
    """
    Determine the winner of an alternative (instant runoff) election.

    Given a list of candidates and ranked votes, hold an alternative vote
    election and return the winning candidate and the number of votes they
    received in the final round. Each ranked vote does not need to rank all of
    the candidates, but if all of their chosen candidates are eliminated, the
    vote is not counted in the total (for determining a majority winner).

    Args:
        candidates: A list of strings representing the candidates' names.
        ranked_votes: A list of lists  of strings representing the ranked votes
            for candidates, with each list in order from most to least
            preferred.

    Returns:
        A tuple of a string and an integer, representing the winning candidate's
        name and the number of votes they won with in the final round.
    """
    # We only need to do this process as long as there are multiple candidates
    # in the running, so repeat until a winner is chosen or until only one
    # candidate is left.
    while len(candidates) > 1:
        # Calculate how many votes each candidate gets, and the total number of
        # votes cast.
        vote_counts = tally_votes(candidates, ranked_votes)
        total_votes = sum(vote_counts.values())

        # If there is an absolute winner, return the candidate and their votes.
        for candidate, num_votes in vote_counts.items():
            if num_votes > total_votes // 2:
                return candidate, num_votes

        # If there is no absolute winner, figure out who got the fewest votes
        # and eliminate them.
        minimum_candidate = get_minimum_candidate(vote_counts)
        candidates = [
            candidate
            for candidate in candidates
            if candidate != minimum_candidate
        ]

    # If there is only one candidate left, they are the winner, but we need to
    # count the number of valid votes.
    winner = candidates[0]
    num_votes = sum([1 for vote in ranked_votes if winner in vote])
    return winner, num_votes


# Original, iterative implemention. DON'T CHANGE.
def hold_iterative_vote(candidates, ranked_votes):
    """
    Determine the winner of an alternative (instant runoff) election.

    Given a list of candidates and ranked votes, hold an alternative vote
    election and return the winning candidate and the number of votes they
    received in the final round. Each ranked vote does not need to rank all of
    the candidates, but if all of their chosen candidates are eliminated, the
    vote is not counted in the total (for determining a majority winner).

    Args:
        candidates: A list of strings representing the candidates' names.
        ranked_votes: A list of lists  of strings representing the ranked votes
            for candidates, with each list in order from most to least
            preferred.

    Returns:
        A tuple of a string and an integer, representing the winning candidate's
        name and the number of votes they won with in the final round.
    """
    # We only need to do this process as long as there are multiple candidates
    # in the running, so repeat until a winner is chosen or until only one
    # candidate is left.
    while len(candidates) > 1:
        # Calculate how many votes each candidate gets, and the total number of
        # votes cast.
        vote_counts = tally_votes(candidates, ranked_votes)
        total_votes = sum(vote_counts.values())

        # If there is an absolute winner, return the candidate and their votes.
        for candidate, num_votes in vote_counts.items():
            if num_votes > total_votes // 2:
                return candidate, num_votes

        # If there is no absolute winner, figure out who got the fewest votes
        # and eliminate them.
        minimum_candidate = get_minimum_candidate(vote_counts)
        candidates = [
            candidate
            for candidate in candidates
            if candidate != minimum_candidate
        ]

    # If there is only one candidate left, they are the winner, but we need to
    # count the number of valid votes.
    winner = candidates[0]
    num_votes = sum(1 for vote in ranked_votes if winner in vote)
    return winner, num_votes
