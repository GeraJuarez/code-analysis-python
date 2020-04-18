import unittest
import csv
from DataSorter import DataSorter


class TestDataSorter(unittest.TestCase):
    """The TestDataSorter class runs some unit tests for the DataSorter class.
    """

    def is_sorted(self, arr):
        """Validates for a sorted array/list.

        Args:
            arr: the list to be validated.

        Returns:
            True if the given array is sorted.
        """

        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

    def test_merge_sort1(self):
        """Tests the mergesort algorithm with an list of integers.
        """

        ds = DataSorter()
        arr = [5, 2, 1, 3, 5]
        ds.execute_merge_sort(data=arr)
        self.assertTrue(self.is_sorted(arr))

    def test_merge_sort2(self):
        """Tests if the mergesort algorithm with an list of
        integers with an odd length.
        """

        ds = DataSorter()
        arr = [5, 3, 1]
        ds.execute_merge_sort(data=arr)
        self.assertTrue(self.is_sorted(arr))

    def test_merge_sort3(self):
        """Test that validates the use of the DataSorter list when
        a None value is given to the mergesort method of the class.
        """

        ds = DataSorter()
        arr = None
        ds.execute_merge_sort(data=arr)
        self.assertFalse(ds.data)

    def test_merge_sort4(self):
        """Test the correctness of the mergesort when given a list of strings.
        """

        ds = DataSorter()
        arr = ['z2', 'a', 'b', '123', '512']
        ds.execute_merge_sort(data=arr)
        self.assertTrue(self.is_sorted(arr))

    def test_load_file(self):
        """Test that a file is actually read and sorted by the class.
        """

        ds = DataSorter()
        ds.set_input_data('sample.csv')
        ds.execute_merge_sort()
        self.assertTrue(self.is_sorted(ds.data))

    def test_load_file_err1(self):
        """Test that IOError is raised with a non csv-file.
        """

        ds = DataSorter()
        with self.assertRaises(IOError):
            ds.set_input_data('sample.txt')

    def test_load_file_err2(self):
        """Test that TypeError is raised with an invalid path.
        """

        ds = DataSorter()
        with self.assertRaises(TypeError):
            ds.set_input_data(None)

    def test_save_file(self):
        """Test that the saved csv-file is sorted.
        """

        ds = DataSorter()
        ds.set_input_data('sample.csv')
        ds.execute_merge_sort()
        ds.set_output_data('out.csv')

        with open('out.csv', 'r') as fp:
            reader = csv.reader(fp, delimiter=',', skipinitialspace=True)
            data = next(reader)

        self.assertEqual(data, ds.data)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
