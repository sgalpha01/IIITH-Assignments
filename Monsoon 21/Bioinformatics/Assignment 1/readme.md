# Assignment 1

Q1. Given a DNA sequence in the forward strand, find

    (i) the sequence of the reverse strand
    (ii) the RNA sequence synthesised
    (iii)  the amino acid synthesised

`Input:`

```console
❯ echo gtttcattataccagtttagatctatcgacagggcgttgagtgtgtgcttactcacggct \
ggcatgtaggtaacagtagtggggaagcgtaacatctgaggcctgactcacatatagagt \
gtcgaccaaggggtgaagcatcatacgccatacaggcccctagcgaaacgacctagtcta \
aagacacacgagaatgaaacccgtggacttggttacagcgtaataatctggtcagagctg \
gtccggcgctggcgatgtaccttacgccactgcaaaccggctttgcagagaacatctggg \
tacattcccgtgtcatgtcaaagcaggtgattcccgcgaaaaacaattaacgacgcattt \
gctattgacgaagtcctagttctccgaattgagcgggagacatatgatgtcgagactgca \
ggaaccgaattatcctgtccgcagatccaatagctcacagaggtaaggggagtgtgatgg \
tgccctagggtgtttgaacg | python q1.py
```

`Output:`

```console
The sequence of reverse strand:
3' - CAAAGTAATATGGTCAAATCTAGATAGCTGTCCCGCAACTCACACACGAATGAGTGCCGACCGTACATCCATTGTCATCACCCCTTCGCATTGTAGACTCCGGACTGAGTGTATATCTCACAGCTGGTTCCCCACTTCGTAGTATGCGGTATGTCCGGGGATCGCTTTGCTGGATCAGATTTCTGTGTGCTCTTACTTTGGGCACCTGAACCAATGTCGCATTATTAGACCAGTCTCGACCAGGCCGCGACCGCTACATGGAATGCGGTGACGTTTGGCCGAAACGTCTCTTGTAGACCCATGTAAGGGCACAGTACAGTTTCGTCCACTAAGGGCGCTTTTTGTTAATTGCTGCGTAAACGATAACTGCTTCAGGATCAAGAGGCTTAACTCGCCCTCTGTATACTACAGCTCTGACGTCCTTGGCTTAATAGGACAGGCGTCTAGGTTATCGAGTGTCTCCATTCCCCTCACACTACCACGGGATCCCACAAACTTGC - 5'

The sequence of RNA:
GUUUCAUUAUACCAGUUUAGAUCUAUCGACAGGGCGUUGAGUGUGUGCUUACUCACGGCUGGCAUGUAGGUAACAGUAGUGGGGAAGCGUAACAUCUGAGGCCUGACUCACAUAUAGAGUGUCGACCAAGGGGUGAAGCAUCAUACGCCAUACAGGCCCCUAGCGAAACGACCUAGUCUAAAGACACACGAGAAUGAAACCCGUGGACUUGGUUACAGCGUAAUAAUCUGGUCAGAGCUGGUCCGGCGCUGGCGAUGUACCUUACGCCACUGCAAACCGGCUUUGCAGAGAACAUCUGGGUACAUUCCCGUGUCAUGUCAAAGCAGGUGAUUCCCGCGAAAAACAAUUAACGACGCAUUUGCUAUUGACGAAGUCCUAGUUCUCCGAAUUGAGCGGGAGACAUAUGAUGUCGAGACUGCAGGAACCGAAUUAUCCUGUCCGCAGAUCCAAUAGCUCACAGAGGUAAGGGGAGUGUGAUGGUGCCCUAGGGUGUUUGAACG

------------------------------------------------------------
5' -> 3' Frame 1:
------------------------------------------------------------
Amino Acid Sequence:
VSLYQFRSIDRALSVCLLTAGM*VTVVGKRNI*GLTHI*SVDQGVKHHTPYRPLAKRPSLKTHENETRGLGYSVIIWSELVRRWRCTLRHCKPALQRTSGYIPVSCQSR*FPRKTINDAFAIDEVLVLRIERETYDVETAGTELSCPQIQ*LTEVRGV*WCPRVFE

Amino acids that can be synthesised from frame 1 are:
1: M

------------------------------------------------------------
5' -> 3' Frame 2:
------------------------------------------------------------
Amino Acid Sequence:
FHYTSLDLSTGR*VCAYSRLACR*Q*WGSVTSEA*LTYRVSTKG*SIIRHTGP*RNDLV*RHTRMKPVDLVTA**SGQSWSGAGDVPYATANRLCREHLGTFPCHVKAGDSREKQLTTHLLLTKS*FSELSGRHMMSRLQEPNYPVRRSNSSQR*GECDGALGCLN

Amino acids that can be synthesised from frame 2 are:
1: MKPVDLVTA
2: MMSRLQEPNYPVRRSNSSQR
3: MSRLQEPNYPVRRSNSSQR

------------------------------------------------------------
5' -> 3' Frame 3:
------------------------------------------------------------
Amino Acid Sequence:
FIIPV*IYRQGVECVLTHGWHVGNSSGEA*HLRPDSHIECRPRGEASYAIQAPSETT*SKDTRE*NPWTWLQRNNLVRAGPALAMYLTPLQTGFAENIWVHSRVMSKQVIPAKNN*RRICY*RSPSSPN*AGDI*CRDCRNRIILSADPIAHRGKGSVMVP*GV*T

Amino acids that can be synthesised from frame 3 are:
1: MYLTPLQTGFAENIWVHSRVMSKQVIPAKNN
2: MSKQVIPAKNN
3: MVP
```

Q2. Write a program to generate a restriction map for Wuhan isolate-1 genome (Acc. Id.: NC_045512) using EcoRI as RE compare your results with REBsites.

`I/O:`

```console
❯ python q2.py
Do you want to search using accession ID? (y/n): y
Enter Accession ID: NC_045512
Sequence retrieved successfully!
Enter the Sequence of Restriction Enzyme: GAATTC
Site Length: 6
Frequency: 9
Cut Positions:
[1161, 11734, 17280, 17728, 20278, 22870, 26439, 28551, 29620]
Fragment Length:
[283, 448, 1069, 1161, 2112, 2550, 2592, 3569, 5546, 10573]
```

We can confirm the output using this [link](https://tools.neb.com/REBsites/rsdisp.php?prid=gRxd3H6Hm46-NC_045512&page=1&gelset=agarose&gelid=gel_07_1).

![Image](https://tools.neb.com/REBsites/TMP/gRxd3H6Hm46-NC_045512.rsdisp.png?c=6133ac86a3b08)

It can also be confirmed from http://www.restrictionmapper.org.

Q3. Write a program to identify restriction recognition sites in a given DNA sequence.

The solution to this program is based on the following assumption:

- Restriction sites are palindromic subsequences.
- The majority of the restrictions sites are of length 4, 5, and 6.

This script asks for the length of the site as spaced separated integers. You can enter `6` as input.

`Example:`

```console
❯ python q3.py
Enter DNA sequence: gctcgtGAATTCggttccggttGAATTCgcacGGATCCgaccGGATCCgt
Enter Lengths of Restriction Sites: 6
The following indices may be restriction sites:
[6, 22, 32, 42]
```

In this example, 4 sites (in capital) were inserted which was successfully detected by the script.