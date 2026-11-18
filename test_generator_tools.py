
import unittest

from bioinformatics.generator_tools import (
    dna_bases,
    find_g_bases,
    count_g_bases
)


class TestGeneratorTools(unittest.TestCase):

    def test_dna_bases(self):
        result = list(dna_bases("AGTGC"))
        self.assertEqual(result, ["A", "G", "T", "G", "C"])

    def test_find_g_bases(self):
        result = list(find_g_bases("AGTGC"))
        self.assertEqual(result, ["G", "G"])

    def test_count_g_bases(self):
        result = count_g_bases("AGTGC")
        self.assertEqual(result, 2)

    def test_empty_dna(self):
        self.assertEqual(list(dna_bases("")), [])
        self.assertEqual(list(find_g_bases("")), [])
        self.assertEqual(count_g_bases(""), 0)


if __name__ == "__main__":
    unittest.main()
  
