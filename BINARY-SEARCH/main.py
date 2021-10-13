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

def binary_search(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1

    while low <= high:
        mid: int = (low + high) // 2

        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True

    return False


gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
my_gene: Gene = string_to_gene(gene_str)

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

my_sorted_gene: Gene = sorted(my_gene)
print(binary_search(my_sorted_gene, acg))
print(binary_search(my_sorted_gene, gat))
