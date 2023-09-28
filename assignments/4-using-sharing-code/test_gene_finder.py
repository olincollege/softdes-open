"""
Test library functions to find and identify protein-coding genes in DNA.
"""
from collections import Counter
import pytest

from gene_finder import (
    get_complement,
    get_reverse_complement,
    rest_of_orf,
    find_all_orfs_one_frame,
    find_all_orfs,
    find_all_orfs_both_strands,
    find_longest_orf,
    encode_amino_acids,
)


# Define sets of test cases.
get_complement_cases = [
    # Check that the complement of A is T.
    ("A", "T"),
    # Check that the complement of C is G.
    ("C", "G"),
    # Check that the complement of T is A.
    ("T", "A"),
    # Check that the complement of G is C.
    ("G", "C"),
]

get_reverse_complement_cases = [
    # Check a single nucleotide, which should be the same as the complement.
    ("A", "T"),
]

rest_of_orf_cases = [
    # Check a start followed by a stop.
    ("ATGTGA", "ATG"),
    # Check a case without a stop codon.
    ("ATGAAA", "ATGAAA"),
    # Check a case without a stop codon where the length is not a multiple of 3.
    ("ATGA", "ATGA"),
]

find_all_orfs_one_frame_cases = [
    # Check a strand with a single ORF.
    ("ATGTGA", ["ATG"]),
    # Check a strand with two ORFs.
    ("ATGTAAATGAAATAA", ["ATG", "ATGAAA"]),
]

find_all_orfs_cases = [
    # This case from find_all_orfs has no ORFs in other frames, so it should
    # return the same result as in the one_frame case.
    ("ATGTAAATGAAATAA", ["ATG", "ATGAAA"]),
]

find_all_orfs_both_strands_cases = [
    # Test a short strand starting with a start codon whose reverse complement
    # is itself. Thus this should return two copies of the same ORF.
    ("ATGCAT", ["ATGCAT", "ATGCAT"]),
]

find_longest_orf_cases = [
    # An ORF covering the whole strand is by default the longest ORF.
    ("ATGAAAAAAAAA", "ATGAAAAAAAAA"),
]

encode_amino_acids_cases = [
    # Check a single start codon.
    ("ATG", "M"),
    # Check a case in which the length is not a multiple of 3.
    ("ATGCCCGCTTT", "MPA"),
]


# Define additional testing lists and functions that check other properties of
# functions in gene_finder.py.
@pytest.mark.parametrize("nucleotide", ["A", "T", "C", "G"])
def test_double_complement(nucleotide):
    """
    Check that taking the complement of a complement of a nucleotide produces
    the original nucleotide.

    Args:
        nucleotide: A single-character string representing one of the four DNA
            nucleotides.
    """
    assert get_complement(get_complement(nucleotide)) == nucleotide


################################################################################
# Don't change anything below these lines.
################################################################################


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("nucleotide,complement", get_complement_cases)
def test_get_complement(nucleotide, complement):
    """
    Test that each nucleotide is mapped to its correct complement.

    Given a single-character string representing a nucleotide that is "A", "T",
    "G", or "C", check that the get_complement function correctly maps the
    string to a single-character string representing the nucleotide's complement
    (also "A", "T", "G", or "C").

    Args:
        nucleotide: A single-character string equal to "A", "C", "T", or "G"
            representing a nucleotide.
        complement: A single-character string equal to "A", "C", "T", or "G"
            representing the expected complement of nucleotide.
    """
    assert get_complement(nucleotide) == complement


@pytest.mark.parametrize("strand,reverse_complement",
                         get_reverse_complement_cases)
def test_get_reverse_complement(strand, reverse_complement):
    """
    Test that a string of nucleotides get mapped to its reverse complement.

    Check that given a string consisting of "A", "C", "T", and "G" that
    represents a strand of DNA, the get_reverse_complement function correctly
    returns the reverse complement of the string, defined as the complement of
    each nucleotide in the strand in reverse order.

    Args:
        strand: A string consisting only of the characters "A", "C", "T", and
            "G" representing a strand of DNA.
        reverse_complement: A string representing the expected reverse
            complement of strand.
    """
    assert get_reverse_complement(strand) == reverse_complement


@pytest.mark.parametrize("strand,rest", rest_of_orf_cases)
def test_rest_of_orf(strand, rest):
    """
    Test that a string representing a strand of DNA gets mapped to the rest of
    its open reading frame.

    Check that given a string representing a strand of DNA as defined above, the
    rest_of_orf function returns a string representing a strand of DNA for the
    rest of the given strand's open reading frame. This is the original strand
    until reading sets of three nucleotides results in a STOP codon, or the
    entire strand if no such codon appears when reading the strand.

    Args:
        strand: A string representing a strand of DNA.
        rest: A string representing the expected rest of the open reading frame
            of strand, or the entirety of strand if reading it does not result
            in a STOP codon at any point.
    """
    assert rest_of_orf(strand) == rest


@pytest.mark.parametrize("strand,orfs", find_all_orfs_one_frame_cases)
def test_find_all_orfs_oneframe(strand, orfs):
    """
    Test that a string representing a strand of DNA gets mapped to a list of all
    non-overlapping open reading frames (ORFs) aligned to its frame.

    Check that given a string representing a strand of DNA as defined above, the
    find_all_orfs_oneframe function returns a list of strings representing all
    non-overlapping ORFs in the strand that are aligned to the strand's frame
    (i.e., starting a multiple of 3 nucleotides from the start of the strand).
    Each ORF is a strand of DNA from a START codon to a STOP codon (or in the
    case of the last ORF in the strand, to the end of the strand if no STOP
    codon is encountered during reading).

    Args:
        strand: A string representing a strand of DNA.
        orfs: A list of strings representing the expected strands of DNA that
            are ORFs within strand's frame.
    """
    assert Counter(find_all_orfs_one_frame(strand)) == Counter(orfs)


@pytest.mark.parametrize("strand,orfs", find_all_orfs_cases)
def test_find_all_orfs(strand, orfs):
    """
    Test that a string representing a strand of DNA gets mapped to a list of all
    open reading frames within the strand, with no overlapping ORFs within any
    given frame of the strand.

    Check that given a string representing a strand of DNA as defined above, the
    find_all_orfs function returns a list of strings representing all ORFs in
    the strand as defined above. Overlapping ORFs are allowed as long as they do
    not occur in different frames (i.e., each ORF is only non-overlapping with
    the other ORFs in its own frame).

    Args:
        strand: A string representing a strand of DNA.
        orfs: A list of strings representing the expected strands of DNA that
            are ORFs within strand, with no overlapping ORFs within one frame of
            strand.
    """
    assert Counter(find_all_orfs(strand)) == Counter(orfs)


@pytest.mark.parametrize("strand,orfs", find_all_orfs_both_strands_cases)
def test_find_all_orfs_both_strands(strand, orfs):
    """
    Test that a string representing a strand of DNA gets mapped to a list of
    all open reading frames within the strand or its reverse complement, with no
    overlapping ORFs within a given frame.

    Check that given a string representing a strand of DNA as defined above, the
    find_all_orfs_both_strands function returns a list of strings representing
    all ORFs in the strand or its reverse complement as defined above.

    Args:
        strand: A string representing a strand of DNA.
        orfs: A list of strings representing the expected strands of DNA that
            are ORFs within strand or its reverse complement, with no
            overlapping ORFs within one frame of either.
    """
    assert Counter(find_all_orfs_both_strands(strand)) == Counter(orfs)


@pytest.mark.parametrize("strand,orf", find_longest_orf_cases)
def test_find_longest_orf(strand, orf):
    """
    Test that a string representing a strand of DNA gets mapped to a string
    representing the longest ORF within the strand or its reverse complement.

    Check that given a string representing a strand of DNA as defined above, the
    find_longest_orf function returns a string representing a strand of DNA
    equal to the longest ORF within the strand or its reverse complement.

    Args:
        strand: A string representing a strand of DNA.
        orf: A string representing a strand of DNA equal to the expected longest
            ORF in strand or its reverse complement.
    """
    assert find_longest_orf(strand) == orf


@pytest.mark.parametrize("strand,protein", encode_amino_acids_cases)
def test_encode_amino_acids(strand, protein):
    """
    Test that a string representing a strand of DNA gets mapped to a string
    representing the amino acids encoded by the strand.

    Check that given a string representing a strand of DNA as defined above, the
    encode_amino_acids function returns a string consisting of one-letter IUPAC
    amino acid codes corresponding to the sequence amino acids encoded by the
    strand.

    Args:
        strand: A string representing a strand of DNA.
        protein: A string representing the expected sequence one-letter IUPAC
            amino acid codes encoded by strand.
    """
    assert encode_amino_acids(strand) == protein
