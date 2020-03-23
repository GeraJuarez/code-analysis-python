import unittest
import math


class TestingFactorial(unittest.TestCase):
    """The TestingFactorial class runs some unit tests
    for the math.factorial function.
    """

    def test_one(self):
        """Test the base case of 1.
        """

        input_ = 1
        output = math.factorial(input_)
        expected = 1

        self.assertEqual(expected, output,
                         f'Result: {output}, expectd: {expected}')

    def test_zero(self):
        """Test the base case of 0.
        """

        input_ = 0
        output = math.factorial(input_)
        expected = 1

        self.assertEqual(expected, output,
                         f'Result: {output}, expectd: {expected}')

    def test_10(self):
        """Test for input of 10.
        """

        input_ = 10
        output = math.factorial(input_)
        expected = 3628800

        self.assertEqual(expected, output,
                         f'Result: {output}, expectd: {expected}')

    def test_negative(self):
        """Test for negative number ValueError.
        """

        input_ = -1
        expected = ValueError
        with self.assertRaises(expected):
            math.factorial(input_)

    def test_float_type(self):
        """Test for invalid type float. ValueError.
        """

        input_ = 1.2
        expected = ValueError
        with self.assertRaises(expected):
            math.factorial(input_)

    def test_str_type(self):
        """Test for invalid type str. ValueError.
        """

        expected = TypeError
        input_ = 'c'
        with self.assertRaises(expected):
            math.factorial(input_)

    def test_list_type(self):
        """Test for invalid type list. ValueError.
        """

        expected = TypeError
        input_ = []
        with self.assertRaises(expected):
            math.factorial(input_)

    def test_dict_type(self):
        """Test for invalid type dict. ValueError.
        """

        expected = TypeError
        input_ = []
        with self.assertRaises(expected):
            math.factorial(input_)

    def test_none_type(self):
        """Test for invalid type None. ValueError.
        """

        expected = TypeError
        input_ = None
        with self.assertRaises(expected):
            math.factorial(input_)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
