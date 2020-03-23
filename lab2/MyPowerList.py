class MyPowerList():
    """MyPowerList implements a list of any type that
    can read data from files.
    """

    def __init__(self):
        """Initializes an empty list."""
        self.power_list = []

    def __str__(self):  # pragma: no cover
        return str(self.power_list)

    def add_item(self, item):
        """Adds a new item into the list.

        Args:
            item: the value of any type to be added.
        """

        self.power_list.append(item)

    def remove_item_at(self, index):
        """Removes an item at the specified index.

        Args:
            index: the index of the desired item to remove from the list.

        Raises:
            IndexError
        """

        if index >= len(self.power_list):
            raise IndexError(
                'Index out of bounds, remember it is a 0-index list')

        del self.power_list[index]

    def read_from_txt_file(self, txt_file):
        """Load data from a file in the specified path.

        Args:
            txt_file: the path and filename of data to load

        Raises:
            IOError
        """

        if not txt_file.endswith('.txt'):
            raise IOError('File must be a txt file')

        with open(txt_file, "r") as fp:
            for line in fp:
                self.power_list.append(line.rstrip('\n'))
