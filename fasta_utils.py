from Bio import SeqIO


def read_fasta(file_name):

    return list(SeqIO.parse(file_name, "fasta"))
