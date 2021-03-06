import unittest
from array_string import has_unique_chars
from array_string import is_permutation
from array_string import newspaper_letter
from array_string import is_rotation
from array_string import compress_string
from array_string import reverse_list
from array_string import remove_duplicates
from array_string import User
from array_string import sort_users


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

    def test_newspaper_letter(self):
        self.assertFalse(newspaper_letter('acb ', 'def'))
        self.assertTrue(newspaper_letter('nib', 'bin'))
        self.assertFalse(newspaper_letter('nib', 'Nbin'))
        self.assertFalse(newspaper_letter('nad', 'naad'))
        self.assertTrue(newspaper_letter('n ', 'n'))
        self.assertTrue(newspaper_letter('', ''))
        self.assertTrue(newspaper_letter('aaasd', 'aad'))

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

    def test_reverse_list(self):
        self.assertEqual(reverse_list(None), None)
        self.assertEqual(reverse_list(['']), [''])
        self.assertEqual(reverse_list(['f', 'o', 'o']),
                         ['o', 'o', 'f'])
        self.assertEqual(reverse_list(['f', 'o', 'o', ' ', 'b', 'a', 'r']),
                         ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        self.assertEqual(reverse_list(['A']), ['A'])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates(None), None)
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_duplicates([1, 1, 2, 3, 3]), [1, 2, 3])
        self.assertEqual(remove_duplicates([1, 2, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_duplicates([4, 3, 5, 4, 3]), [3, 4, 5])

    def test_sort_users(self):
        self.assertEqual(sort_users(None), None)
        self.assertEqual(sort_users([]), [])
        user_1 = User('sahana', 23)
        self.assertEqual(sort_users([user_1]), [user_1])
        user_2 = User('alex', 24)
        user_3 = User('oliver', 2)
        self.assertEqual(sort_users([user_1, user_2, user_3]),
                         [user_3, user_1, user_2])


if __name__ == '__main__':
    unittest.main()
