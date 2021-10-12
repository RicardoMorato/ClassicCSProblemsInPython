# To contextualize you about the problem we are solving here.
# We will be using "binary search" to search inside a DNA for a specific Codon (a sequence of three nucleotides)

from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

def string_to_gene(s: str) -> Gene:
    gene: Gene = []

    for i in range(0, len(s), 3):
        if (i + 2) >= len(s): # This will prevent us of going past the end of the string
            return gene

        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)

    return gene


gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
my_gene: Gene = string_to_gene(gene_str)
