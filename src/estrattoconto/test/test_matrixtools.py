import unittest

from .. import matrixtools


class TestMatrixtools(unittest.TestCase):
    def test_merge_columns(self):
        it = [['a', 'b', 'c', 'd', 'e', 'f'],
              ['g', 'h', 'i', 'j', 'k', 'l'],
              ['m', 'n', 'o', 'p', 'q', 'r']]
        n = 3
        sep = '-'

        expected = [['a', 'b', 'c', 'd-e-f'],
                    ['g', 'h', 'i', 'j-k-l'],
                    ['m', 'n', 'o', 'p-q-r']]

        actual = matrixtools.merge_columns(it, n, sep)
        self.assertEqual(expected, list(actual))

    def test_merge_rows(self):
        it = [['a', 'b'], [None, 'c'], ['', 'd'], ['e', ''], ['f', 'g']]
        i = 0
        sep = '-'

        expected = [['a', 'b-c-d'], ['e', ''], ['f', 'g']]

        actual = matrixtools.merge_rows(it, i, sep)
        self.assertEqual(expected, list(actual))
