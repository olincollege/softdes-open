"""
Check the correctness of IEEE 754 floating-point number conversion.
"""
# Import all required libraries.
import math
import pytest

# Import the student's submitted code.
from pricy_fall import terminal_velocity


@pytest.mark.parametrize(
    "mass,area,timestep,final_velocity",
    [
        # These test cases were randomly generated.
        (11, 5, 0.01, -9.281955411225052),
        (12, 2, 0.01, -15.328514267535121),
        (16, 15, 0.01, -6.463172659534776),
        (5, 8, 0.01, -4.947372655977238),
        (20, 1, 0.01, -27.98586451154314),
        (7, 1, 0.01, -16.556691974909405),
        (13, 3, 0.01, -13.026769423210247),
        (13, 7, 0.01, -8.528066661996395),
        (1, 20, 0.01, -1.3994227537441408),
        (13, 17, 0.01, -5.472417428653486),
    ],
)
def test_terminal_velocity(mass, area, timestep, final_velocity):
    """
    Test that an implementation of Euler's method correctly calculates the
    terminal velocity of a falling sphere.

    Args:
        mass: The mass of the sphere in kg.
        area: The cross-sectional area of the sphere in m^2.
        timestep: The timestep for Euler's method in seconds.
        final_velocity: The expected terminal velocity of the sphere in m/s.
    """
    assert math.isclose(terminal_velocity(mass, area, timestep), final_velocity)
