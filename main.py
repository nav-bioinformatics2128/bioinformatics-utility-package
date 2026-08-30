import argparse

from fasta_utils import read_fasta
from dna_utils import gc_content
from dna_utils import reverse_complement
from dna_utils import validate_dna
from protein_utils import translate


def main():

    parser = argparse.ArgumentParser(
        description="Analyze DNA sequences from a FASTA file."
    )

    parser.add_argument(
        "fasta_file",
        help="Path to the FASTA file"
    )

    args = parser.parse_args()

    records = read_fasta(args.fasta_file)

    if not records:
        print("No sequences available for analysis.")
        return

    for record in records:

        sequence = str(record.seq)

        print("\nID:", record.id)

        if validate_dna(sequence):

            print("Valid DNA sequence")
            print("Length:", len(sequence))
            print("GC:", gc_content(sequence))

            print("Reverse Complement:")
            print(reverse_complement(sequence))

            print("Protein:")
            print(translate(sequence))

        else:

            print("Invalid DNA sequence")


if __name__ == "__main__":
    main()
