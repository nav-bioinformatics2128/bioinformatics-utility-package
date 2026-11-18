bioinformatics-utility-package

A modular bioinformatics toolkit in Python for FASTA file analysis, GC content calculation, reverse complement generation, and DNA-to-protein translation using Biopython.

DNA Generator Tools

The "generator_tools.py" module provides simple DNA sequence processing functions using Python generators.

Features

- "dna_bases(dna)": Generates individual nucleotide bases.
- "find_g_bases(dna)": Filters and generates only G bases.
- "count_g_bases(dna)": Counts the number of G bases.

Example

Input:

dna = "AGTGC"

Output:

DNA: AGTGC
G bases:
G
G
Total G bases: 2

Concepts Used

- Python functions
- For loops
- Conditional statements
- Generators and "yield"
- Counting with variables
