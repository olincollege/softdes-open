"""
Generate a random image.
"""
import argparse
import math
import sys
from random import choice, randrange
from PIL import Image

DEFAULT_WIDTH = 350
DEFAULT_HEIGHT = 350
DEFAULT_MIN_DEPTH = 7
DEFAULT_MAX_DEPTH = 9


def average(x, y):  # pylint: disable=invalid-name
    """
    Return the average of two numbers.
    """
    return (x + y) / 2


def cosine(x):  # pylint: disable=invalid-name
    """
    Return the cosine of pi times a number.
    """
    return math.cos(math.pi * x)


def sine(x):  # pylint: disable=invalid-name
    """
    Return the sine of pi times a number.
    """
    return math.sin(math.pi * x)


def multiply(x, y):  # pylint: disable=invalid-name
    """
    Return the product of two numbers.
    """
    return x * y


# Map each function to the number of arguments it takes.
NUM_ARGS = {
    average: 2,
    cosine: 1,
    multiply: 2,
    sine: 1,
}


def first(x, _):  # pylint: disable=invalid-name
    """
    Return the first of two arguments.
    """
    return x


def second(_, y):  # pylint: disable=invalid-name
    """
    Return the second of two arguments.
    """
    return y


BASE_FUNCTIONS = [first, second]


def build_random_function(min_depth, max_depth):
    """
    Your docstring goes here.
    """
    pass


def convert_scale(old_value, old_min, old_max, new_min, new_max):
    """
    Convert a value from one scale to another.

    Args:
        old_value: An int or float representing a value on the old scale.
        old_min: An int or float representing the minimum value on the old
            scale.
        old_max: An int or float representing the maximum value on the old
            scale.
        new_min: An int or float representing the new minimum value, that is,
            what old_min will get mapped to.
        new_max: An int or float representing the new maximum value, that is,
            what old_max will get mapped to.

    Returns:
        A float representing the equivalent value on the new scale.
    """
    return new_min + (new_max - new_min) / (old_max - old_min) * (
        old_value - old_min
    )


def color_map(value):
    """
    Map a value between -1 and 1 to an 8-bit color value (0 to 255).

    Args:
        value: An int or float representing a value between -1 and 1, inclusive.

    Returns:
        An int representing a color value between 0 and 255, inclusive.
    """
    return int(convert_scale(value, -1, 1, 0, 255))


def generate_image(width, height, min_depth, max_depth):
    """
    Generate an image with pixel colors set according to randomly-generated
    functions.

    Generate an image with the given dimensions, whose pixel colors are
    determined by randomly-generated functions for each of the

    Args:
        width: A positive int representing the width of the generated image in
            pixels.
        height: A positive int representing the height of the generated image in
            pixels.
        min_depth: A nonnegative int representing the minimum recursive depth of
            the random functions used to generate the image.
        max_depth: A nonnegative int representing the maximum recursive depth of
            the random functions used to generate the image.

    Returns:
        A PIL.Image instance representing the randomly generated image.
    """
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    channels = tuple(
        build_random_function(min_depth, max_depth) for _ in range(3)
    )
    for i in range(width):
        for j in range(height):
            # pylint: disable=invalid-name
            x = convert_scale(i, 0, width, -1, 1)
            y = convert_scale(j, 0, height, -1, 1)
            pixels[i, j] = tuple(
                color_map(function(x, y)) for function in channels
            )
    return image


def get_parser(name):
    """
    Return the command-line argument parser used for this script.

    Args:
        name: A string representing the name of the script.

    Returns:
        An argparse namespace representing the successfully parsed arguments'
        names and values.
    """
    parser = argparse.ArgumentParser(name)
    parser.add_argument(
        "--width",
        type=int,
        default=DEFAULT_WIDTH,
        help=(
            f"Width of the generated image in pixels (default: {DEFAULT_WIDTH})"
        ),
    )
    parser.add_argument(
        "--height",
        type=int,
        default=DEFAULT_HEIGHT,
        help=(
            "Height of the generated image in pixels (default:"
            f" {DEFAULT_HEIGHT})"
        ),
    )
    parser.add_argument(
        "--min-depth",
        type=int,
        default=DEFAULT_MIN_DEPTH,
        help=(
            "Minimum recursive depth of color functions"
            f" (default: {DEFAULT_MIN_DEPTH})"
        ),
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=DEFAULT_MAX_DEPTH,
        help=(
            "Maximum recursive depth of color functions"
            f" (default: {DEFAULT_MAX_DEPTH})"
        ),
    )
    parser.add_argument("filename", help="Path to save the generated image to")
    return parser


def main(args):
    """
    Generate and save a random image.

    Args:
        args: A list of strings representing arguments to the script.
    """
    parser = get_parser(args[0])
    parsed_args = parser.parse_args(args[1:])
    image = generate_image(
        parsed_args.width,
        parsed_args.height,
        parsed_args.min_depth,
        parsed_args.max_depth,
    )
    image.save(parsed_args.filename)


if __name__ == "__main__":
    main(sys.argv)
