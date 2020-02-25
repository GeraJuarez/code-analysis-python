class MyPowerList():
    def __init__(self):
        self.power_list = []

    def __str__(self):
        return str(self.power_list)

    def add_item(self, item):
        self.power_list.append(item)

    def remove_item_at(self, index):
        if index >= len(self.power_list):
            raise Exception('Index out of bounds, remember it is a 0-index list')

        del self.power_list[index]

    def read_from_txt_file(self, txt_file):
        if not txt_file.endswith('.txt'):
            raise Exception('File mmust be a txt file')

        with open(txt_file, "r") as fp:
            for line in fp:
                self.power_list.append(line.rstrip('\n'))
