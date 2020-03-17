import csv


class DataSorter(object):
    def __init__(self):
        self.data = []

    def set_input_data(self, file_path_name):
        if file_path_name is None:
            raise TypeError('File path must not be None')

        if not file_path_name.endswith('.csv'):
            raise IOError('File must be a csv file')

        with open(file_path_name, 'r') as fp:
            reader = csv.reader(fp, delimiter=',', skipinitialspace=True)
            for row in reader:
                self.data += row

    def set_output_data(self, file_path_name):
        with open(file_path_name, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(self.data)

    def execute_merge_sort(self, data=None):
        if data is None:
            data = self.data

        self.__merge_sort(data, 0, len(data))

    def __merge_sort(self, arr, idx_start, idx_end):
        if len(arr[idx_start:idx_end]) < 2:
            return

        if idx_start < idx_end:
            idx_mid = (idx_start + idx_end) // 2
            self.__merge_sort(arr, idx_start, idx_mid)
            self.__merge_sort(arr, idx_mid, idx_end)
            self.__merge(arr, idx_start, idx_mid, idx_end)

    def __merge(self, arr, idx_start, idx_mid, idx_end):
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
