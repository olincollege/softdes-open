"""
Helper constants and functions for Gene Finder project.

Author: Steve Matsumoto <smatsumoto@olin.edu>
"""
import random


# Use these for convenient notation in the amino_acid implementation. These are
# to help implementation and are not designed to be human-readable. For a more
# readable list of codons/amino acids, see
# https://en.wikipedia.org/wiki/DNA_codon_table instead.
PURINES = {"A", "G"}
PARTIAL_CODON_TABLE = {
    "CT": "L",  # Leucine
    "GT": "V",  # Valine
    "TC": "S",  # Serine
    "CC": "P",  # Proline
    "AC": "T",  # Threonine
    "GC": "A",  # Alanine
    "CG": "R",  # Arginine
    "GG": "G",  # Glycine
}
BRANCHED_CODON_TABLE = {
    "TT": ("L", "F"),  # Leucine, Phenylalanine
    "TA": ("*", "Y"),  # STOP, Tyrosine
    "CA": ("Q", "H"),  # Glutamine, Histidine
    "AA": ("K", "N"),  # Lysine, Asparagine
    "GA": ("E", "D"),  # Glutamic acid, Aspartic acid
    "AG": ("R", "S"),  # Arginine, Serine
}


def amino_acid(codon):  # pylint: disable=too-many-return-statements
    """
    Return the amino acid symbol corresponding to the DNA codon.

    Given a string `codon` of exactly three DNA nucleotides, return the IUPAC
    amino acid code corresponding to `codon`. A list of the amino acid codes and
    their corresponding codons can be found here:
    https://en.wikipedia.org/wiki/DNA_codon_table

    Args:
        codon: A string of exactly three DNA nucleotides (A, T, C, or G).

    Returns:
        A string of a single character representing the IUPAC notation of the
        amino acid corresponding to `codon`.
    """
    # Some amino acids can be determined solely by the first two nucleotides.
    if codon[:2] in PARTIAL_CODON_TABLE:
        return PARTIAL_CODON_TABLE[codon[:2]]

    # Many other amino acids can be determined by the first two nucleotides,
    # plus whether the last nucleotide is a purine (A/G) or pyramidine (T/C).
    if codon[:2] in BRANCHED_CODON_TABLE:
        branches = BRANCHED_CODON_TABLE[codon[:2]]
        if codon[-1] in PURINES:
            return branches[0]
        return branches[1]

    # The few amino acids left can be handled on a case-by-case basis.
    if codon == "ATG":
        return "M"  # Methionine/START
    if codon[:2] == "AT":
        return "I"  # Isoleucine
    # At this point we know the first two characters of the codon are "TG".
    if codon[-1] not in PURINES:
        return "C"  # Cysteine
    if codon[-1] == "A":
        return "*"  # STOP
    return "W"  # Tryptophan


def shuffle(strand):
    """
    Shuffle the order of nucleotides in a strand of DNA.

    Args:
        strand: A string representing a strand of DNA as a sequence of
            nucleotides (A, T, C, G).

    Returns:
        A string representing the shuffled strand, with the same number of each
        nucleotide, but likely in a different order.
    """
    return "".join(random.sample(strand, len(strand)))


def load_fasta_file(path):
    """
    Read and return a sequence of DNA nucleotides from a FASTA file.

    Args:
        path: A string representing the path to the FASTA file.

    Returns:
        A string representing the sequence of DNA nucleotides (i.e., the
        characters A, T, C, or G) in the FASTA file.
    """
    sequence = ""
    read_header = False
    with open(path, "r", encoding="ascii") as fasta_file:
        for line in fasta_file:
            if not read_header:
                # Skip the header line.
                read_header = True
                continue
            sequence += line.strip()
    return sequence
