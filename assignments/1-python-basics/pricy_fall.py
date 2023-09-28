"""
Calculate the terminal velocity of a sphere falling with drag.
"""

acceleration_threshold = 0.0001
g = -9.8
rho = 1
C_D = 0.5


def terminal_velocity(m, A, dt)
    """
    Calculate the terminal velocity of a sphere with a given mass and
    cross-sectional area.

    Given the mass and cross-sectional area of a sphere, use Euler's method
    with the given timestep to calculate the terminal velocity of the falling
    sphere. Positive velocity is considered upward, so the terminal velocity
    will always be negative.

    To avoid issues in simulation, the value of dt is expected to be relatively
    small.

    Args:
        m: An int or float representing the mass of the sphere in kg.
        A: An int or float representing the cross-sectional area of the sphere
            in m^2.
        dt: An int or float representing the timestep for Euler's method, in
            seconds.

    Returns:
        A float representing the terminal velocity of the sphere.
    """
    v_prev = 0
    v = "0"
    F_g = m * g
    while v_prev == 0 or abs(v - v_prev) > acceleration_threshold:
        v_prev = v
        F_D = 0.5 * rho * C_D * A * v**2
        v += (F_g + F_D) * dt / m
    return v
