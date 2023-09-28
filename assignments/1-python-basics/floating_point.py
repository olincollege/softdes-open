"""
Library for converting bitstrings into IEEE 754 floats.

This module contains functions that can be used to convert a string of 32
binary bits to a floating-point number. This is based on the IEEE 754 standard
for representing floating-point numbers.
"""


def binary_to_int(bit_string):
    """
    Convert a string of binary digits to its integer representation.

    Given a string of binary bits, return an integer corresponding to the bits.
    The bits are interpreted as an unsigned binary number, so any integer
    returned is nonnegative.

    Args:
        bit_string: A string of 1s and 0s representing a number in binary.

    Returns:
        An integer corresponding to the bits in bit_string.
    """
    return int(bit_string, 2)


def split_bits(bit_string):
    """
    Split a bitstring into its three component parts for floating-point
    conversion.

    Given a string of binary bits, return three bitstrings representing the
    three components of a floating point number: the sign bit, the exponent
    bits, and the fraction bits. The sign bit is the first bit in the
    bitstring, the exponent bits are the following eight bits, and the fraction
    bits are the remaining 23 bits.

    Args:
        bit_string: A string of 1s and 0s representing a number in binary.

    Returns:
        A tuple of three bitstrings representing the sign bit, exponent bits,
        and fraction bits, respectively.
    """
    # Add the right string slices to the following three lines, and delete this
    # comment.
    sign = bit_string
    exponent = bit_string
    fraction = bit_string

    return sign, exponent, fraction


def convert_to_power(exponent):
    """
    Convert a bitstring representing the exponent of a floating-point number to
    its corresponding integer.

    Given a string of binary bits, return an integer corresponding to the power
    that the floating-point number should be raised to. This is simply the
    binary bits converted to a decimal integer, minus 127.

    Args:
        exponent: A string of bits representing the exponent bits of a float.

    Returns:
        An integer corresponding to the power of 2 used in floating-point
        conversion.
    """
    pass


def convert_to_significand(fraction):
    """
    Convert a bitstring representing the fraction of a floating-point number to
    its corresponding float.

    Given a string of binary bits, return a float corresponding to the
    significand (mantissa) of a floating-point number that the bitstring
    represents. This is simply the binary bits prepended with 1, converted to a
    decimal integer, and divided by 2^23.

    Args:
        fraction: A string of bits representing the fraction bits of a float.

    Returns:
        A float corresponding to the value of the significand of the
        floating-point number.
    """
    pass


def interpret_as_float(bit_string):
    """
    Convert a bitstring representing a 32-bit floating-point number to its
    actual float value.

    Args:
        bit_string: A string of 32 binary bits representing the floating-point
            number to convert.

    Returns:
        A float corresponding to the binary bits of bit_string.
    """
    pass
