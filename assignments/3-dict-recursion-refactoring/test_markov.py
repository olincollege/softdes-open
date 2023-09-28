"""
Test that Markov text generation code is working properly.
"""
import collections
import pytest
from markov import (
    build_word_list,
    build_next_words,
    generate_sentence,
    generate_text,
)


# Word lists for source texts with unusual spacing.
SPACING_CASES = [
    # Sample text given in assignment instructions.
    (
        "I am Sam.\n\nI am Sam.\nSam I am.",
        {
            "": ["I", "I", "Sam"],
            "I": ["am", "am", "am."],
            "am": ["Sam.", "Sam."],
            "Sam.": [""],
            "Sam": ["I"],
            "am.": [""],
        },
    ),
    # Single word.
    (
        "Hippopotomonstrosesquipedaliophobia.",
        {
            "": ["Hippopotomonstrosesquipedaliophobia."],
            "Hippopotomonstrosesquipedaliophobia.": [""],
        },
    ),
    # A sentence with many newlines.
    (
        "Hi!\n\n\n\n\n\n\n\n\n\n\n\n...anyone there?",
        {
            "": ["Hi!", "...anyone"],
            "Hi!": [""],
            "...anyone": ["there?"],
            "there?": [""],
        },
    ),
    # A string with leading and trailing whitespace.
    (
        "    INT. KITCHEN - CONTINUOUS       ",
        {
            "": ["INT.", "KITCHEN"],
            "INT.": [""],
            "KITCHEN": ["-"],
            "-": ["CONTINUOUS"],
        },
    ),
    # A string with leading and trailing newlines.
    (
        "\nWait, is this the first line?\n",
        {
            "": ["Wait,"],
            "Wait,": ["is"],
            "is": ["this"],
            "this": ["the"],
            "the": ["first"],
            "first": ["line?"],
            "line?": [""],
        },
    ),
    # Multiple spaces within a sentence.
    (
        (
            "Hello, I'm Microsoft Word.  Since April 2020, two spaces after a"
            " sentence is considered an error."
        ),
        {
            "": ["Hello,", "Since"],
            "Hello,": ["I'm"],
            "I'm": ["Microsoft"],
            "Microsoft": ["Word."],
            "Word.": [""],
            "Since": ["April"],
            "April": ["2020,"],
            "2020,": ["two"],
            "two": ["spaces"],
            "spaces": ["after"],
            "after": ["a"],
            "a": ["sentence"],
            "sentence": ["is"],
            "is": ["considered"],
            "considered": ["an"],
            "an": ["error."],
            "error.": [""],
        },
    ),
]

# Test cases for word splitting function.
WORD_LIST_PARAMS = map(lambda case: (case[0], case[0].split()), SPACING_CASES)

# Single sentences with non-repeating words to test sentence generation.
NONREPEATING_SENTENCE_CASES = [
    (
        "Call me Ishmael.",
        {"": ["Call"], "Call": ["me"], "me": ["Ishmael."], "Ishmael.": [""]},
    ),
    # Sentence with punctuation-only word.
    (
        "I - wait, what?",
        {
            "": ["I"],
            "I": ["-"],
            "-": ["wait,"],
            "wait,": ["what?"],
            "what?": [""],
        },
    ),
    # Sentence with repeated words, but with differing case/punctuation.
    (
        "You are what you are.",
        {
            "": ["You"],
            "You": ["are"],
            "are": ["what"],
            "what": ["you"],
            "you": ["are."],
            "are.": [""],
        },
    ),
    # Sentence with punctuation in middle of word.
    (
        "Just type example.com into your browser!",
        {
            "": ["Just"],
            "Just": ["type"],
            "type": ["example.com"],
            "example.com": ["into"],
            "into": ["your"],
            "your": ["browser!"],
            "browser!": [""],
        },
    ),
]

GEN_SENTENCE_PARAMS = [case[0] for case in NONREPEATING_SENTENCE_CASES]

# Word list generation should be done with all of the previous test cases, with
# some additional cases.
NEXT_WORDS_CASES = (
    SPACING_CASES
    + NONREPEATING_SENTENCE_CASES
    + [
        # Test a word being followed by different words.
        (
            "Arlington Boston Arlington Cambridge.",
            {
                "": ["Arlington"],
                "Arlington": ["Boston", "Cambridge."],
                "Boston": ["Arlington"],
                "Cambridge.": [""],
            },
        ),
        # Test multiple starting words.
        (
            "Raindrops. Roses. Whiskers on kittens.",
            {
                "": ["Raindrops.", "Roses.", "Whiskers"],
                "Raindrops.": [""],
                "Roses.": [""],
                "Whiskers": ["on"],
                "on": ["kittens."],
                "kittens.": [""],
            },
        ),
        # Test a sentence with multiple instances of the same word sequences.
        (
            "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.",
            {
                "": ["Buffalo"],
                "Buffalo": ["buffalo", "buffalo", "buffalo."],
                "buffalo": ["Buffalo", "buffalo", "buffalo", "Buffalo"],
                "buffalo.": [""],
            },
        ),
    ]
)

NEXT_WORDS_PARAMS = [(case[0].split(), case[1]) for case in NEXT_WORDS_CASES]


@pytest.mark.parametrize("source_text,split_text", WORD_LIST_PARAMS)
def test_build_word_list(source_text, split_text):
    """
    Check that splitting a source text into words yields the correct sequence
    of strings.

    Args:
        source_text: A string representing the source text.
        split_text: A list of strings representing the words in source_text (not
            including leading or trailing whitespace).
    """
    assert build_word_list(source_text) == split_text


@pytest.mark.parametrize("word_list,next_words", NEXT_WORDS_PARAMS)
def test_build_next_words(word_list, next_words):
    """
    Check that the solution correctly builds the dictionary of next words.

    Args:
        word_list: A list of words representing the split words of a source
            text.
        next_words: A dictionary representing the set of words that follow each
            word in the source text.
    """
    actual_next_words = build_next_words(word_list)

    # Check that they have the same words as keys.
    assert set(actual_next_words.keys()) == set(next_words.keys())

    for word, possible_next_words in actual_next_words.items():
        # Check that each word has the same set of words following it. To ensure
        # that different ordering of the words doesn't cause the check to fail,
        # simply make sure that the same next words appear an equal number of
        # times.
        assert collections.Counter(possible_next_words) == collections.Counter(
            next_words[word]
        )


# Defining and using this fixture in other functions will cause a pylint error
# by default, so suppress it here.
# pylint: disable=redefined-outer-name
@pytest.fixture(params=GEN_SENTENCE_PARAMS)
def sentence(request):
    """
    Fixture used when generating sentences or text.

    Args:
        request: A Pytest request instance representing the requesting test.

    Returns:
        A string representing the sentence.
    """
    return request.param


def test_generate_sentence(sentence):
    """
    Check that generating a Markov sentence from a source text with only unique
    words results in the same sentence.

    Args:
        sentence: A string representing the source text.
    """
    word_list = build_word_list(sentence)
    next_words = build_next_words(word_list)

    # The test cases we use here are all single sentences with no repeating
    # words, so generating a single sentence should just return the original
    # sentence.
    assert generate_sentence(next_words) == sentence


# Defining and using this fixture in other functions will cause a pylint error
# by default, so suppress it here.
# pylint: disable=redefined-outer-name
@pytest.fixture(params=list(range(1, 3)))
def num_sentences(request):
    """
    Fixture used when generating a number of sentences.

    Args:
        request: A Pytest request instance representing the requesting test.

    Returns:
        An int represnting a number of sentences to generate.
    """
    return request.param


def test_generate_text(sentence, num_sentences):
    """
    Check that generating a number of Markov sentences from a source text with
    only unique words results in the source sentence some number of times.

    Args:
        sentence: A string representing a source text of only one sentence.
        num_sentences: An int representing a number of random sentences to
            generate.
    """
    word_list = build_word_list(sentence)
    next_words = build_next_words(word_list)
    assert generate_text(next_words, num_sentences) == " ".join(
        [sentence] * num_sentences
    )
