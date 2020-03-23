import unittest
from MyPowerList import MyPowerList as MPL


class TestingMyPowerList(unittest.TestCase):
    """MyPowerList unit tests.
    """

    def test_add_item_count(self):
        """Test number of additions corresponds to the list size.
        """

        mpl = MPL()
        mpl.add_item(1)

        expected = 1
        result = len(mpl.power_list)

        self.assertEqual(expected, result,
                         f'Result: {result}, expectd: {expected}')

        mpl.add_item(2)
        mpl.add_item(20)

        expected = 3
        result = len(mpl.power_list)
        self.assertEqual(expected, result,
                         f'Result: {result}, expectd: {expected}')

    def test_add_item_exists(self):
        """Test consistency of the list when adding the first element.
        """

        mpl = MPL()
        mpl.add_item([])

        expected = []
        result = mpl.power_list[0]
        self.assertEqual(expected, result,
                         f'Result: {result}, expectd: {expected}')

    def test_remove_item(self):
        """Test consistency of the list after removing an element.
        """

        mpl = MPL()
        mpl.add_item(1)
        mpl.add_item('string')
        mpl.add_item([1])

        mpl.remove_item_at(0)
        expected = 'string'
        result = mpl.power_list[0]
        self.assertEqual(expected, result,
                         f'Result: {result}, expectd: {expected}')

    def test_remove_item_bounds(self):
        """Test IndexError when removing an item.
        """

        mpl = MPL()
        mpl.add_item(1)

        self.assertRaises(IndexError, mpl.remove_item_at, 1)

    def test_read_from_file(self):
        """Test data from file is saved correctly into the list
        """

        mpl = MPL()
        mpl.read_from_txt_file('sample.txt')

        expected = '1'
        result = mpl.power_list[0]
        self.assertEqual(expected, result,
                         f'Result: {result}, expectd: {expected}')

    def test_read_from_file_error1(self):
        """Test IOError when reading non-txt files.
        """

        mpl = MPL()
        mpl.add_item(1)

        self.assertRaises(IOError, mpl.read_from_txt_file, 'sample.csv')

    def test_read_from_file_error2(self):
        """Test IOError when reading non-existent files
        """

        mpl = MPL()
        mpl.add_item(1)

        self.assertRaises(IOError, mpl.read_from_txt_file, 'sample2.txt')


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
