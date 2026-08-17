from fasta_utils import read_fasta
from dna_utils import gc_content
from dna_utils import reverse_complement
from protein_utils import translate


records = read_fasta("sample.fasta")


for record in records:

    sequence = str(record.seq)

    print(record.id)

    print("GC:", gc_content(sequence))

    print("Reverse Complement:")

    print(reverse_complement(sequence))

    print("Protein:")

    print(translate(sequence))

    print("-" * 40)
