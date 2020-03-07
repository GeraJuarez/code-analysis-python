import unittest
from utils import *


class TestingUtils(unittest.TestCase):
    def test_mean(self):
        expected = 3
        result = mean([1, 2, 3, 4, 5])

        self.assertEqual(expected, result)

    def test_std_dev(self):
        expected = 1.5811388300841898
        result = std_dev([1, 2, 3, 4, 5])

        self.assertEqual(expected, result)

    def test_median(self):
        expected = 3
        result = median([1, 2, 3, 4, 5])

        self.assertEqual(expected, result)

    def test_quartil(self):
        expected = 3
        result = n_quartil([1, 2, 3, 4, 5], 2)

        self.assertEqual(expected, result)

    def test_quartil_err(self):
        self.assertRaises(Exception, n_quartil, [1, 2, 3, 4, 5], 5)

    def test_percentil(self):
        expected = 3
        result = n_percentil([1, 2, 3, 4, 5], 50)

        self.assertEqual(expected, result)

    def test_percentil2(self):
        expected = 3
        result = n_percentil([1, 2, 3, 3, 5, 6], 50)

        self.assertEqual(expected, result)

    def test_percentil_err1(self):
        self.assertRaises(Exception, n_percentil, [1, 2, 3, 4, 5], 100)

    def test_percentil_err2(self):
        self.assertRaises(Exception, n_percentil, [1, 2, 3, 4, 5], None)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
