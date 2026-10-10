from bioinformatics.dna_utils import validate_dna
from bioinformatics.dna_utils import gc_content
from bioinformatics.dna_utils import reverse_complement


def test_validate_dna():

    assert validate_dna("ATGC") is True
    assert validate_dna("ATGCGCTA") is True
    assert validate_dna("ATGX") is False


def test_gc_content():

    assert gc_content("ATGC") == 50.0
    assert gc_content("GGCC") == 100.0
    assert gc_content("AAAA") == 0.0


def test_reverse_complement():

    assert reverse_complement("ATGC") == "GCAT"
    assert reverse_complement("AAAA") == "TTTT"
    assert reverse_complement("GGCC") == "GGCC"


def test_empty_sequence():
    assert gc_content("") == 0
