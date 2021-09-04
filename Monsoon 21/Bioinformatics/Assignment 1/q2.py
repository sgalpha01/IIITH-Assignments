import re
import requests
from requests.exceptions import HTTPError


URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id="


def get_fasta(acc_num):
    url = URL + acc_num + "&rettype=fasta"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Sequence retrieved successfully!")
        return response.text
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


def get_seq(fasta):
    return "".join(fasta.split("\n")[1:]).strip()


def get_indices(dna_seq, re_seq):
    idx = []
    for i in range(len(dna_seq) - len(re_seq) + 1):
        if dna_seq[i : i + len(re_seq)] == re_seq:
            idx.append(i + 1)

    return idx


def get_frag_len(cut_positions, len_dna_seq):
    frag_len = [cut_positions[0]]
    for i in range(len(cut_positions) - 1):
        frag_len.append(cut_positions[i + 1] - cut_positions[i])
    frag_len.append(len_dna_seq - cut_positions[-1])

    return frag_len


if __name__ == "__main__":
    is_accession = (
        input("Do you want to search using accession ID? (y/n): ").strip().lower()
    )
    if is_accession == "y":
        acc_num = input("Enter Accession ID: ").strip()
        dna_seq = get_seq(get_fasta(acc_num))
    elif is_accession == "n":
        dna_seq = input("Enter your DNA sequence: \n").strip()
    else:
        print("Oops! option not valid. Please run the script again.")
    re_seq = input("Enter the Sequence of Restriction Enzyme: ").strip().upper()
    cut_positions = get_indices(dna_seq, re_seq)
    print(f"Site Length: {len(re_seq)}")
    print(f"Frequency: {len(cut_positions)}")
    print(f"Cut Positions:\n{cut_positions}")
    print(f"Fragment Length:\n{sorted(get_frag_len(cut_positions, len(dna_seq)))}")
