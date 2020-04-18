import csv
import logging
import logging.config

logging.config.fileConfig('logging.conf')
LOG = logging.getLogger(__name__)


class DataSorter(object):
    """The DataSorter class save csv files and sortes them.

    It can read a csv file and sort it at increasing order with
    the merge sort algorithm, the result can then be saved in another file.
    """

    def __init__(self):
        """The constructor. Initialize a list."""

        self.data = []

    def set_input_data(self, file_path_name):
        """Read the csv file in the specified path

        Args:
            file_path_name: The path of the csv file

        Raises:
            TypeError, IOError
        """

        LOG.info(f'Reading data from file: {file_path_name}')

        if file_path_name is None:
            LOG.error('Encountered empty file path')
            raise TypeError('File path must not be None')

        if not file_path_name.endswith('.csv'):
            LOG.error('Encountered non-csv file to read')
            raise IOError('File must be a csv file')

        with open(file_path_name, 'r') as fp:
            reader = csv.reader(fp, delimiter=',', skipinitialspace=True)
            for row in reader:
                self.data += row

    def set_output_data(self, file_path_name):
        """Write a csv file in the specified path with the saved data

        Args:
            file_path_name: The path of the csv file to be written

        Raises:
            IOError
        """

        LOG.info(f'Writing data to path: {file_path_name}')

        with open(file_path_name, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(self.data)

    def execute_merge_sort(self, data=None):
        """Apply the mergesort algorithm to the given list

        When data is None, it will sort the data/list saved in the
        instantiated class.

        Args:
            data: The list to be sorted. When None, it will use the
            list saved in this class.

        Raises:
            TypeError
        """

        LOG.info('Executing merge sort')

        if data is None:
            LOG.info('Using data from DataSorter object')
            data = self.data

        if type(data) is not list:
            LOG.error(f'Incorrect datatype used as argument" {type(data)}')
            raise TypeError('given data must be a list')

        self.__merge_sort(data, 0, len(data))

    def __merge_sort(self, arr, idx_start, idx_end):
        """The actual mergesort algorithm

        It splits the list by half until the base case arrives, that is
        when a list of 2 or three elements is reached. Then, it continues
        to the merge section.

        Args:
            arr: The list to be sorted
            idx_start: the first index of the array/list
            idx_end: the last index of the array/list
        """

        if len(arr[idx_start:idx_end]) < 2:
            return

        if idx_start < idx_end:
            idx_mid = (idx_start + idx_end) // 2
            self.__merge_sort(arr, idx_start, idx_mid)
            self.__merge_sort(arr, idx_mid, idx_end)
            self.__merge(arr, idx_start, idx_mid, idx_end)

    def __merge(self, arr, idx_start, idx_mid, idx_end):
        """The merge step of the mergesort algorithm

        It merges two sorted arrays into a single one.

        Args:
            arr: The list to be sorted
            idx_start: the first index of the array/list
            idx_mid: the middle index of the array/list
            idx_end: the last index of the array/list
        """

        temp = []
        iter_left = idx_start
        iter_right = idx_mid

        for _ in range(idx_end - idx_start):
            if iter_left == idx_mid:
                temp.append(arr[iter_right])
                iter_right += 1

            elif iter_right == idx_end:
                temp.append(arr[iter_left])
                iter_left += 1

            elif arr[iter_left] <= arr[iter_right]:
                temp.append(arr[iter_left])
                iter_left += 1

            else:
                temp.append(arr[iter_right])
                iter_right += 1

        for idx, val in enumerate(temp):
            arr[idx_start + idx] = val


if __name__ == "__main__":  # pragma: no cover
    sorter = DataSorter()
    sorter.set_input_data('lab5/sample.csv')
    sorter.execute_merge_sort()
    sorter.set_output_data('lab5/s.csv')
