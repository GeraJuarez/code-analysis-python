import unittest
from UserDirectoryManager import UserDirectoryManager as UDM


class TestingUserManager(unittest.TestCase):
    """UserDirectoryManager unit tests.
    """

    def test_add_record(self):
        """Test successfull User insertion.
        """

        udm = UDM()
        output = udm.create_record('name', 'g@g.com', 22, 'Somewhere')

        self.assertIsNotNone(output)

    def test_add_record_null(self):
        """Test error when using None type as name.
        """

        udm = UDM()
        expected = TypeError

        with self.assertRaises(expected):
            udm.create_record(None, 'g@g.com', 22, 'Somewhere')

    def test_search_email(self):
        """Test the succesfull search of a User by email.
        """

        udm = UDM()
        udm.create_record('name', 'somewhere', 22, 'g@g.com')
        found = udm.search_by_email('g@g.com')

        self.assertIsNotNone(found)
        self.assertEqual('name', found.name)

    def test_search_email_non_existent(self):
        """Test for None type when searching non existent User
        """

        udm = UDM()
        found = udm.search_by_email('g2@g.com')

        self.assertIsNone(found)

    def test_search_email_other_type(self):
        """Test for None type for invalid email.
        """

        udm = UDM()
        udm.create_record('name', 'g@g.com', 22, 'Somewhere')
        found = udm.search_by_email(22)

        self.assertIsNone(found)

    def test_save_file(self):
        """Test that the saved file has the same Users from the class.
        """

        udm = UDM()
        udm.create_record('name', 'somewhere', 22, 'g@g.com')
        udm.save_to_file()

        with open('users_out.txt', "r") as fp:
            line = fp.readline()
            values = [data.rstrip('\n') for data in line.split(',')]

        self.assertEqual('name', values[0])

    def test_load_file(self):
        """Test that the class reads all Usres from file.
        """

        udm = UDM()
        udm.load_from_file()
        self.assertEqual('name', udm.search_by_email('g@g.com').name)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
