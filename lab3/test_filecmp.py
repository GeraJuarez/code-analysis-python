import unittest
import filecmp


class TestingFilecmp(unittest.TestCase):
    """The TestingFactorial class runs some unit tests
    for the filecmp.cmp function.
    """

    def test_same_file(self):
        """Test the comparison of a file with itself.
        """

        input1 = '1.txt'
        input2 = '1.txt'
        output = filecmp.cmp(input1, input2)

        self.assertTrue(output)

    def test_same_extension_same_content(self):
        """Test for True comparing equal files with different name.
        """

        input1 = '1.txt'
        input2 = '2.txt'
        output = filecmp.cmp(input1, input2)

        self.assertTrue(output)

    def test_diff_extension_same_content(self):
        """Test for True comparing equal files with different extension.
        """

        input1 = '2.txt'
        input2 = '2.csv'
        output = filecmp.cmp(input1, input2)

        self.assertTrue(output)

    def test_same_extension_diff_content(self):
        """Test for False comparing different files with same extension.
        """

        input1 = '1.txt'
        input2 = '3.txt'
        output = filecmp.cmp(input1, input2)

        self.assertFalse(output)

    def test_diff_extension_diff_content(self):
        """Test for False comparing different files with different extension.
        """

        input1 = '2.csv'
        input2 = '3.txt'
        output = filecmp.cmp(input1, input2)

        self.assertFalse(output)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
