from fasta_utils import read_fasta
from dna_utils import gc_content
from dna_utils import reverse_complement
from dna_utils import validate_dna
from protein_utils import translate


records = read_fasta("sample.fasta")


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
