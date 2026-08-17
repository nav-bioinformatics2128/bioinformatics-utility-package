def gc_content(sequence):
    gc = sequence.count("G") + sequence.count("C")
    return round((gc / len(sequence)) * 100, 2)


def reverse_complement(sequence):
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    reverse = sequence[::-1]

    reverse_comp = ""

    for base in reverse:
        reverse_comp += complement[base]

    return reverse_comp
