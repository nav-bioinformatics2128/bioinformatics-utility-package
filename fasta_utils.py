from Bio import SeqIO


def read_fasta(file_name):

    try:
        records = list(SeqIO.parse(file_name, "fasta"))

    except FileNotFoundError:
        print("Error: FASTA file not found.")
        return []

    if not records:
        print("Error: FASTA file contains no sequences.")
        return []

    return records
