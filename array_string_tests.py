import unittest
from array_string import has_unique_chars
from array_string import is_permutation
from array_string import is_rotation
from array_string import compress_string


class TestArrayString(unittest.TestCase):

    def test_has_unique_chars(self):
        self.assertTrue(has_unique_chars('art'))
        self.assertFalse(has_unique_chars('hip hop'))
        self.assertFalse(has_unique_chars('  '))
        self.assertTrue(has_unique_chars(' '))

    def test_is_permutation(self):
        self.assertFalse(is_permutation('acb ', 'def'))
        self.assertTrue(is_permutation('nib', 'bin'))
        self.assertFalse(is_permutation('nib', 'Nbin'))
        self.assertFalse(is_permutation('n ', 'n'))
        self.assertTrue(is_permutation('', ''))

    def test_is_rotation(self):
        self.assertFalse(is_rotation('asdf', 'sdfaa'))
        self.assertTrue(is_rotation('asdf', 'sdfa'))
        self.assertTrue(is_rotation('ddd', 'ddd'))
        self.assertFalse(is_rotation('ddd', 'dddd'))
        self.assertTrue(is_rotation(' ', ' '))

    def test_compress_string(self):
        self.assertEqual(compress_string(None), None)
        self.assertEqual(compress_string(''), '')
        self.assertEqual(compress_string('A'), 'A')
        self.assertEqual(compress_string('AABBCC'), 'AABBCC')
        self.assertEqual(compress_string('AAABCCDDDD'), 'A3B1C2D4')

if __name__ == '__main__':
    unittest.main()
