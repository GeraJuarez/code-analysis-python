import unittest
import math


class TestingFactorial(unittest.TestCase):
    def test_one(self):
        input_ = 1
        output = math.factorial(input_)
        expected = 1

        self.assertEqual(expected, output,
                         f'Result: {output}, expectd: {expected}')

    def test_zero(self):
        input_ = 0
        output = math.factorial(input_)
        expected = 1

        self.assertEqual(expected, output,
                         f'Result: {output}, expectd: {expected}')

    def test_10(self):
        input_ = 10
        output = math.factorial(input_)
        expected = 3628800

        self.assertEqual(expected, output,
                         f'Result: {output}, expectd: {expected}')

    def test_negative(self):
        input_ = -1
        expected = ValueError
        with self.assertRaises(expected):
            math.factorial(input_)

    def test_float_type(self):
        input_ = 1.2
        expected = ValueError
        with self.assertRaises(expected):
            math.factorial(input_)

    def test_str_type(self):
        expected = TypeError
        input_ = 'c'
        with self.assertRaises(expected):
            math.factorial(input_)

    def test_list_type(self):
        expected = TypeError
        input_ = []
        with self.assertRaises(expected):
            math.factorial(input_)

    def test_dict_type(self):
        expected = TypeError
        input_ = []
        with self.assertRaises(expected):
            math.factorial(input_)

    def test_none_type(self):
        expected = TypeError
        input_ = None
        with self.assertRaises(expected):
            math.factorial(input_)


if __name__ == "__main__":
    unittest.main()
