"""
Function for the One Billion Seconds exercise.
"""

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
DAYS_PER_YEAR = 365.25  # Include leap days (approximately)


def time_to_billion_seconds(age):
    """
    Replace this with your docstring.
    """
    # Calculate how many seconds remain until a billion seconds old.
    age_seconds = (
        age
        * DAYS_PER_YEAR
        * HOURS_PER_DAY
        * MINUTES_PER_HOUR
        * SECONDS_PER_MINUTE
    )
    seconds_remaining = 1e9 - age_seconds

    # Split the total number of days remaining into years and days.
    total_days_remaining = seconds_remaining / (
        SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_PER_DAY
    )
    years_remaining = total_days_remaining // DAYS_PER_YEAR
    days_remaining = int(total_days_remaining % DAYS_PER_YEAR)

    # If total_days_remaining is negative, we need to swap the sign on
    # days_remaining.
    if years_remaining < 0:
        days_remaining *= -1

    print(
        f"You have {years_remaining} years and {days_remaining} days until"
        " you are a billion seconds old."
    )
