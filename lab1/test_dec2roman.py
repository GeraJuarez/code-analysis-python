import unittest
from decimal_to_roman import decimal_to_roman as d2r


class TestingDecimal2Roman(unittest.TestCase):
    """decimal_to_roman function unittest
    """

    def test_1(self):
        """Test converting a single digit decimal to a single roman symbol
        """

        expected = 'I'
        result = d2r(1)

        self.assertEqual(expected, result)

    def test_10(self):
        """Test converting a multiple digit decimal to a single roman symbol
        """

        expected = 'X'
        result = d2r(10)

        self.assertEqual(expected, result)

    def test_99(self):
        """Test converting a multiple digit decimal to a multiple roman symbol
        """

        expected = 'XCIX'
        result = d2r(99)

        self.assertEqual(expected, result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
