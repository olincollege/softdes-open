"""
Check the correctness of IEEE 754 floating-point number conversion.
"""
# Import all required libraries.
import math
import pytest

# Import the student's submitted code.
from floating_point import (
    split_bits,
    convert_to_power,
    convert_to_significand,
    interpret_as_float,
)


@pytest.mark.parametrize(
    "bit_string,sign,exponent,fraction",
    [
        # These cases were randomly generated.
        (
            "00000111100100000101111001010110",
            "0",
            "00001111",
            "00100000101111001010110",
        ),
        (
            "11101011100110010100011000000001",
            "1",
            "11010111",
            "00110010100011000000001",
        ),
        (
            "00111111000100000111111000101000",
            "0",
            "01111110",
            "00100000111111000101000",
        ),
        (
            "01011111100111100100001001101101",
            "0",
            "10111111",
            "00111100100001001101101",
        ),
        (
            "01100011010100111110001000010101",
            "0",
            "11000110",
            "10100111110001000010101",
        ),
        (
            "00100100001001001010010101100110",
            "0",
            "01001000",
            "01001001010010101100110",
        ),
        (
            "10000010110000011110011101011000",
            "1",
            "00000101",
            "10000011110011101011000",
        ),
        (
            "10100111110111101111100111100000",
            "1",
            "01001111",
            "10111101111100111100000",
        ),
        (
            "00111011110010100101101101110001",
            "0",
            "01110111",
            "10010100101101101110001",
        ),
        (
            "11010110010100000001011100110010",
            "1",
            "10101100",
            "10100000001011100110010",
        ),
    ],
)
def test_split_bits(bit_string, sign, exponent, fraction):
    """
    Check that the library properly splits 4-byte bitstrings into their sign
    bit, exponent bits, and fraction bits.

    Args:
        bit_string: A string representing the 32-bit string of binary digits to
            split into their components.
        sign: A string representing the expected sign bit of the bitstring.
        exponent: A string representing the expected exponent bits of the
            bitstring.
        fraction: A string representing the expected fraction bits of the
            bitstring.
    """
    assert split_bits(bit_string) == (sign, exponent, fraction)


@pytest.mark.parametrize(
    "exponent,power",
    [
        # These cases were randomly generated.
        ("01100110", -25),
        ("11001010", 75),
        ("11100101", 102),
        ("01011111", -32),
        ("11101110", 111),
        ("00001011", -116),
        ("00100100", -91),
        ("11101010", 107),
        ("00110110", -73),
        ("00100001", -94),
    ],
)
def test_convert_to_power(exponent, power):
    """
    Check that the library properly converts the exponent bits into the
    appropriate exponent.

    Args:
        exponent: A string representing the 8 binary bits of the exponent.
        power: An int representing the expected power of 2 used for the float.
    """
    assert convert_to_power(exponent) == power


@pytest.mark.parametrize(
    "fraction, significand",
    [
        # These cases were randomly generated.
        ("01101010110111000100100", 1.4174237251281738),
        ("00100010000110111000110", 1.133232831954956),
        ("10000000110101011100100", 1.5032620429992676),
        ("10111111110111110110100", 1.7495026588439941),
        ("00000100011001010100111", 1.017170786857605),
        ("01010101011001011110111", 1.333586573600769),
        ("11000010111001000111010", 1.761298418045044),
        ("01101010011100010011100", 1.41579008102417),
        ("10000001110100100000010", 1.507110834121704),
        ("10111010001100100001101", 1.7273269891738892),
    ],
)
def test_convert_to_significand(fraction, significand):
    """
    Check that the library properly converts the exponent bits into the
    appropriate exponent.

    Args:
        fraction: A string representing the 23 binary bits of the fraction.
        significand: A float representing the expected significand in the float.
    """
    # There is a possibility that the values of the expected floats may be
    # slightly different, so check that they are within some close value of each
    # other instead of checking for hard equality.
    assert math.isclose(convert_to_significand(fraction), significand)


@pytest.mark.parametrize(
    "bit_string,converted_float",
    [
        # These cases were randomly generated.
        ("01010110110110001001000100100000", 119058909364224.0),
        ("00011001100010010011110011000000", 1.4190004719566593e-23),
        ("10001100010101111110111111000000", -1.6635144663006297e-31),
        ("11011000100011100111001101100110", -1253010269274112.0),
        ("11010011110111001100111001111011", -1896713945088.0),
        ("01001100000100010101000001100101", 38093204.0),
        ("11100110010010010100010110000000", -2.3761942794248038e23),
        ("01011000110110010110111101010011", 1912577256849408.0),
        ("00101000001000100110110010001101", 9.016344698035018e-15),
        ("00111100101101010000110001111001", 0.022100673988461494),
    ],
)
def test_interpret_as_float(bit_string, converted_float):
    """
    Check that the library properly converts bit strings into floating-point
    numbers.

    Args:
        bit_string: A string representing the 32 binary bits of the float.
        converted_float: A float representing the IEEE 754 value of the float.
    """
    # There is a possibility that the values of the expected floats may be
    # slightly different, so check that they are within some close value of each
    # other instead of checking for hard equality.
    assert math.isclose(interpret_as_float(bit_string), converted_float)
