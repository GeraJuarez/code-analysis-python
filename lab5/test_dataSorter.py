import unittest
import csv
from DataSorter import DataSorter


class TestDataSorter(unittest.TestCase):
    def is_sorted(self, arr):
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

    def test_merge_sort1(self):
        ds = DataSorter()
        arr = [5, 2, 1, 3, 5]
        ds.execute_merge_sort(data=arr)
        self.assertTrue(self.is_sorted(arr))

    def test_merge_sort2(self):
        ds = DataSorter()
        arr = [5, 3, 1]
        ds.execute_merge_sort(data=arr)
        self.assertTrue(self.is_sorted(arr))

    def test_merge_sort3(self):
        ds = DataSorter()
        arr = None
        ds.execute_merge_sort(data=arr)
        self.assertFalse(ds.data)

    def test_merge_sort3(self):
        ds = DataSorter()
        arr = ['z2', 'a', 'b', '123', '512']
        ds.execute_merge_sort(data=arr)
        self.assertTrue(self.is_sorted(arr))

    def test_load_file(self):
        ds = DataSorter()
        ds.set_input_data('sample.csv')
        ds.execute_merge_sort()
        self.assertTrue(self.is_sorted(ds.data))

    def test_load_file_err1(self):
        ds = DataSorter()
        with self.assertRaises(IOError):
            ds.set_input_data('sample.txt')

    def test_load_file_err2(self):
        ds = DataSorter()
        with self.assertRaises(TypeError):
            ds.set_input_data(None)

    def test_save_file(self):
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
