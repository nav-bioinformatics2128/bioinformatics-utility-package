import argparse

from bioinformatics.fasta_utils import read_fasta
from bioinformatics.dna_utils import gc_content
from bioinformatics.dna_utils import reverse_complement
from bioinformatics.dna_utils import validate_dna
from bioinformatics.protein_utils import translate
from bioinformatics.sequence_models import SequenceInfo

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
        info = SequenceInfo(
    sequence_id=record.id,
    length=len(sequence),
    gc_percent=gc_content(sequence)
)

    print("\nSequence Summary:")
    print(info)

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
