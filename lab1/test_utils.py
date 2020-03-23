import unittest
from utils import *


class TestingUtils(unittest.TestCase):
    """Unit tests for the statistics functions from utils.
    """

    def test_mean(self):
        """Test mean of [1, 2, 3, 4, 5]
        """

        expected = 3
        result = mean([1, 2, 3, 4, 5])

        self.assertEqual(expected, result)

    def test_std_dev(self):
        """Test standard deviation of [1, 2, 3, 4, 5]
        """

        expected = 1.5811388300841898
        result = std_dev([1, 2, 3, 4, 5])

        self.assertEqual(expected, result)

    def test_median(self):
        """Test median of [1, 2, 3, 4, 5]
        """

        expected = 3
        result = median([1, 2, 3, 4, 5])

        self.assertEqual(expected, result)

    def test_quartil(self):
        """Test mean 2th quartil same as median.
        """

        expected = 3
        result = n_quartil([1, 2, 3, 4, 5], 2)

        self.assertEqual(expected, result)

    def test_quartil_err(self):
        """Test TypeError with invalid quartil.
        """

        self.assertRaises(TypeError, n_quartil, [1, 2, 3, 4, 5], 5)

    def test_percentil(self):
        """Test mean 50th percentil same as median.
        """

        expected = 3
        result = n_percentil([1, 2, 3, 4, 5], 50)

        self.assertEqual(expected, result)

    def test_percentil2(self):
        """Test mean 50th percentil same as 2th quartil.
        """

        expected = n_quartil([1, 2, 3, 4, 5], 2)
        result = n_percentil([1, 2, 3, 3, 5, 6], 50)

        self.assertEqual(expected, result)

    def test_percentil_err1(self):
        """Test TypeError with invalid percentil.
        """

        self.assertRaises(TypeError, n_percentil, [1, 2, 3, 4, 5], 100)

    def test_percentil_err2(self):
        """Test TypeError with None type as percentil.
        """

        self.assertRaises(TypeError, n_percentil, [1, 2, 3, 4, 5], None)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
