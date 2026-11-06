def dna_bases(dna):
    for base in dna:
        yield base


def find_g_bases(dna):
    for base in dna:
        if base == "G":
            yield base


def count_g_bases(dna):
    count = 0

    for base in find_g_bases(dna):
        count += 1

    return count


dna = "AGTGC"

print("DNA:", dna)
print("G bases:")

for base in find_g_bases(dna):
    print(base)

print("Total G bases:", count_g_bases(dna))
