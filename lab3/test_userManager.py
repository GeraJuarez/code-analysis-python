import unittest
from UserDirectoryManager import UserDirectoryManager as UDM


class TestingUserManager(unittest.TestCase):
    """The TestingUserManager class runs some unit tests
    for the UserDirectoryManager class.
    """

    def test_add_record(self):
        """Test the succesfull insertion of a User
        """

        udm = UDM()
        output = udm.add_record('name', 'g@g.com', 22, 'Somewhere')

        self.assertIsNotNone(output)

    def test_add_record_null(self):
        """Test the TypeError when inserting None values
        """

        udm = UDM()
        expected = TypeError

        with self.assertRaises(expected):
            udm.add_record(None, 'g@g.com', 22, 'Somewhere')

    def test_add_record_repeated_email(self):
        """Test for TypeError when inserting same emails
        """

        udm = UDM()
        expected = TypeError
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')

        with self.assertRaises(expected):
            udm.add_record('name2', 'g@g.com', 21, 'over there')

    def test_del_record(self):
        """Test the succesfull deletion of a User
        """

        udm = UDM()
        output = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        deleted = udm.delete_record_by_email('g@g.com')

        self.assertEqual(output, deleted)
        self.assertIsNone(udm.email_dir.get('g@g.com'))
        self.assertIsNone(udm.age_dir.get(22))

    def test_del_record_none(self):
        """Test for invalid email at deletion.
        """

        udm = UDM()
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        deleted = udm.delete_record_by_email(None)

        self.assertIsNone(deleted)

    def test_del_record_non_existent(self):
        """Test for deletion of non existent user.
        """

        udm = UDM()
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        deleted = udm.delete_record_by_email('g2@g.com')

        self.assertIsNone(deleted)

    def test_search_email(self):
        """Test the succesfull search of a User by email.
        """

        udm = UDM()
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        found = udm.search_by_email('g@g.com')

        self.assertIsNotNone(found)
        self.assertEqual('name', found.name)

    def test_search_email_deleted(self):
        """Test for None type after searching an User after its deletion.
        """

        udm = UDM()
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        udm.delete_record_by_email('g@g.com')
        found = udm.search_by_email('g@g.com')

        self.assertIsNone(found)

    def test_search_email_non_existent(self):
        """Test for None type when searching non existent User
        """

        udm = UDM()
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        udm.delete_record_by_email('g@g.com')
        found = udm.search_by_email('g2@g.com')

        self.assertIsNone(found)

    def test_search_email_other_type(self):
        """Test for None type for invalid email.
        """

        udm = UDM()
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        found = udm.search_by_email(22)

        self.assertIsNone(found)

    def test_search_age(self):
        """Test the succesfull search of User by age.
        """

        udm = UDM()
        created1 = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        created2 = udm.add_record('name2', 'g2@g.com', 22, 'Somewhere')
        found = udm.search_by_age(22)

        self.assertTrue(found)
        self.assertIn(created1, found)
        self.assertIn(created2, found)

    def test_search_age_non_existent(self):
        """Test for searching Users with ages that have not been inserted.
        """

        udm = UDM()
        created1 = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        created2 = udm.add_record('name2', 'g2@g.com', 22, 'Somewhere')
        found = udm.search_by_age(21)

        self.assertFalse(found)
        self.assertNotIn(created1, found)
        self.assertNotIn(created2, found)

    def test_search_age_none(self):
        """Test the search by age when using invalid age.
        """

        udm = UDM()
        created1 = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        found = udm.search_by_age(None)

        self.assertFalse(found)
        self.assertNotIn(created1, found)

    def test_search_age_deleted(self):
        """Test for empty list when searching by age after the users
        were deleted.
        """

        udm = UDM()
        created1 = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        created2 = udm.add_record('name2', 'g2@g.com', 22, 'Somewhere')
        udm.delete_record_by_email('g2@g.com')
        found = udm.search_by_age(22)

        self.assertTrue(found)
        self.assertIn(created1, found)
        self.assertNotIn(created2, found)

    def test_get_all_empty(self):
        """Test empty list when initializing the class.
        """

        udm = UDM()
        records = udm.get_all_records()

        self.assertFalse(records)

    def test_get_all_filled(self):
        """Test the count of added Users.
        """

        udm = UDM()
        created1 = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        created2 = udm.add_record('name2', 'g2@g.com', 23, 'over there')
        created3 = udm.add_record('name2', 'g3@g.com', 23, 'not Somewhere')
        records = udm.get_all_records()

        self.assertTrue(records)
        self.assertEqual(3, len(records))
        self.assertIn(created1, records)

    def test_get_all_after_deletion(self):
        """Test the count of added Users after deletion.
        """

        udm = UDM()
        created1 = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        created2 = udm.add_record('name2', 'g2@g.com', 23, 'over there')
        created3 = udm.add_record('name2', 'g3@g.com', 23, 'not Somewhere')
        udm.delete_record_by_email('g@g.com')
        records = udm.get_all_records()

        self.assertTrue(records)
        self.assertEqual(2, len(records))
        self.assertNotIn(created1, records)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
