import unittest
import filecmp

class TestingFilecmp(unittest.TestCase):
    def test_same_file(self):
        input1 = '1.txt'
        input2 = '1.txt'
        output = filecmp.cmp(input1, input2)

        self.assertTrue(output)

    def test_same_extension_same_content(self):
        input1 = '1.txt'
        input2 = '2.txt'
        output = filecmp.cmp(input1, input2)

        self.assertTrue(output)

    def test_diff_extension_same_content(self):
        input1 = '2.txt'
        input2 = '2.csv'
        output = filecmp.cmp(input1, input2)

        self.assertTrue(output)

    def test_same_extension_diff_content(self):
        input1 = '1.txt'
        input2 = '3.txt'
        output = filecmp.cmp(input1, input2)

        self.assertFalse(output)

    def test_diff_extension_diff_content(self):
        input1 = '2.csv'
        input2 = '3.txt'
        output = filecmp.cmp(input1, input2)

        self.assertFalse(output)



if __name__ == "__main__":
    unittest.main()