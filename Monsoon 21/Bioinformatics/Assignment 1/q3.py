def recog_sites(dna_seq, lengths=[6]):
    compliment_map = {"A": "T", "C": "G", "G": "C", "T": "A"}
    restriction_sites = []
    for i in range(len(dna_seq) - 3):
        for curr_len in lengths:
            is_site = True
            for j in range(curr_len // 2):
                try:
                    if dna_seq[i + j] != compliment_map[dna_seq[i + curr_len - j - 1]]:
                        is_site = False
                        break
                except (KeyError, IndexError):
                    is_site = False
                    continue

            if is_site:
                restriction_sites.append(i)

    return restriction_sites


if __name__ == "__main__":
    dna_seq = input("Enter DNA sequence: ").strip().upper()
    lengths = list(map(int, input("Enter Lengths of Restriction Sites: ")))
    print("The following indices may be restriction sites:")
    print(recog_sites(dna_seq, lengths))