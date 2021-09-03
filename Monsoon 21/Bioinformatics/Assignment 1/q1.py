"""
1. Given a DNA sequence in the forward strand, find
    (i) the sequence of the reverse strand
    (ii) the RNA sequence synthesised
    (iii)  the amino acid synthesised

Sample DNA sequence:
gtttcattataccagtttagatctatcgacagggcgttgagtgtgtgcttactcacggct
ggcatgtaggtaacagtagtggggaagcgtaacatctgaggcctgactcacatatagagt
gtcgaccaaggggtgaagcatcatacgccatacaggcccctagcgaaacgacctagtcta
aagacacacgagaatgaaacccgtggacttggttacagcgtaataatctggtcagagctg
gtccggcgctggcgatgtaccttacgccactgcaaaccggctttgcagagaacatctggg
tacattcccgtgtcatgtcaaagcaggtgattcccgcgaaaaacaattaacgacgcattt
gctattgacgaagtcctagttctccgaattgagcgggagacatatgatgtcgagactgca
ggaaccgaattatcctgtccgcagatccaatagctcacagaggtaaggggagtgtgatgg
tgccctagggtgtttgaacg
"""
import json, re, sys


def get_rev_strand(forw_strand):
    forw_strand = forw_strand.upper()  # if input is in small letters
    complement_map = {"A": "T", "C": "G", "G": "C", "T": "A"}
    rev_strand = ""

    for nuc in forw_strand:
        rev_strand += complement_map[nuc]

    return rev_strand


def get_rna_from_dna(forw_strand):
    forw_strand = forw_strand.upper()  # if input is in small letters
    rna_seq = ""

    for nuc in forw_strand:
        if nuc == "T":
            rna_seq += "U"
        else:
            rna_seq += nuc

    return rna_seq


def get_aa_from_dna(forw_strand):
    forw_strand = forw_strand.upper()  # if input is in small letters
    aa_seq_1, aa_seq_2, aa_seq_3 = "", "", ""
    start_1, start_2, start_3 = [], [], []
    orf_1, orf_2, orf_3 = [], [], []

    with open("codon_map.json") as codon_map:
        codon_map = json.load(codon_map)

    for i in range(len(forw_strand) - 2):
        codon = forw_strand[i : i + 3]

        if i % 3 == 0:
            aa_seq_1 += codon_map[codon]
            if codon == "ATG":
                start_1.append(i // 3)
            if codon_map[codon] == "*":
                orf_1 += [(j, i // 3) for j in start_1]
                start_1.clear()
        elif i % 3 == 1:
            aa_seq_2 += codon_map[codon]
            if codon == "ATG":
                start_2.append(i // 3)
            if codon_map[codon] == "*":
                orf_2 += [(j, i // 3) for j in start_2]
                start_2.clear()

        else:
            aa_seq_3 += codon_map[codon]
            if codon == "ATG":
                start_3.append(i // 3)
            if codon_map[codon] == "*":
                orf_3 += [(j, i // 3) for j in start_3]
                start_3.clear()

    return aa_seq_1, aa_seq_2, aa_seq_3, orf_1, orf_2, orf_3


if __name__ == "__main__":
    forw_strand = sys.stdin.read()
    forw_strand = re.sub(r"[\n\t\s]*", "", forw_strand)  # remove whitespaces

    print("The sequence of reverse strand:")
    print(f"3' - {get_rev_strand(forw_strand)} - 5'", end="\n\n")

    print("The sequence of RNA:")
    print(f"{get_rna_from_dna(forw_strand)}", end="\n\n")

    aa_data = get_aa_from_dna(forw_strand)

    for i in range(3):
        print("---" * 20)
        print(f"5' -> 3' Frame {i + 1}:")
        print("---" * 20)
        print("Amino Acid Sequence:")
        print(aa_data[i], end="\n\n")
        print(f"Amino acids that can be synthesised from frame {i + 1} are:")
        for j in range(len(aa_data[i + 3])):
            print(f"{j + 1}: {aa_data[i][aa_data[i + 3][j][0]: aa_data[i + 3][j][1]]}")
        print("")