def validate_dna(sequence):

    valid_bases = {"A", "T", "G", "C"}

    sequence = sequence.upper()

    for base in sequence:

        if base not in valid_bases:
            return False

    return True


def gc_content(sequence):

    sequence = sequence.upper()

    if len(sequence) == 0:
        return 0

    gc = sequence.count("G") + sequence.count("C")

    return round((gc / len(sequence)) * 100, 2)



def reverse_complement(sequence):

    sequence = sequence.upper()

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    reverse = sequence[::-1]

    result = ""

    for base in reverse:

        result += complement.get(base, "N")

    return result
