codon_table = {
    "ATG": "M",
    "TTT": "F",
    "TTC": "F",
    "TAA": "*",
    "TAG": "*",
    "TGA": "*"
}


def translate(sequence):

    protein = ""

    for i in range(0, len(sequence)-2, 3):

        codon = sequence[i:i+3]

        protein += codon_table.get(codon, "X")

    return protein
