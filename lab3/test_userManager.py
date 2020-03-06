import unittest
from UserDirectoryManager import UserDirectoryManager as UDM


class TestingFilecmp(unittest.TestCase):
    def test_add_record(self):
        udm = UDM()
        output = udm.add_record('name', 'g@g.com', 22, 'Somewhere')

        self.assertIsNotNone(output)

    def test_add_record_null(self):
        udm = UDM()
        expected = TypeError

        with self.assertRaises(expected):
            udm.add_record(None, 'g@g.com', 22, 'Somewhere')

    def test_add_record_repeated_email(self):
        udm = UDM()
        expected = TypeError
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')

        with self.assertRaises(expected):
            udm.add_record('name2', 'g@g.com', 21, 'over there')

    def test_del_record(self):
        udm = UDM()
        output = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        deleted = udm.delete_record_by_email('g@g.com')

        self.assertEqual(output, deleted)
        self.assertIsNone(udm.email_dir.get('g@g.com'))
        self.assertIsNone(udm.age_dir.get(22))

    def test_del_record_none(self):
        udm = UDM()
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        deleted = udm.delete_record_by_email(None)

        self.assertIsNone(deleted)

    def test_del_record_non_existent(self):
        udm = UDM()
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        deleted = udm.delete_record_by_email('g2@g.com')

        self.assertIsNone(deleted)

    def test_search_email(self):
        udm = UDM()
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        found = udm.search_by_email('g@g.com')

        self.assertIsNotNone(found)
        self.assertEqual('name', found.name)

    def test_search_email_deleted(self):
        udm = UDM()
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        udm.delete_record_by_email('g@g.com')
        found = udm.search_by_email('g@g.com')

        self.assertIsNone(found)

    def test_search_email_non_existent(self):
        udm = UDM()
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        udm.delete_record_by_email('g@g.com')
        found = udm.search_by_email('g2@g.com')

        self.assertIsNone(found)

    def test_search_email_other_type(self):
        udm = UDM()
        udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        found = udm.search_by_email(22)

        self.assertIsNone(found)

    def test_search_age(self):
        udm = UDM()
        created1 = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        created2 = udm.add_record('name2', 'g2@g.com', 22, 'Somewhere')
        found = udm.search_by_age(22)

        self.assertTrue(found)
        self.assertIn(created1, found)
        self.assertIn(created2, found)

    def test_search_age_non_existent(self):
        udm = UDM()
        created1 = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        created2 = udm.add_record('name2', 'g2@g.com', 22, 'Somewhere')
        found = udm.search_by_age(21)

        self.assertFalse(found)
        self.assertNotIn(created1, found)
        self.assertNotIn(created2, found)

    def test_search_age_none(self):
        udm = UDM()
        created1 = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        found = udm.search_by_age(None)

        self.assertFalse(found)
        self.assertNotIn(created1, found)

    def test_search_age_deleted(self):
        udm = UDM()
        created1 = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        created2 = udm.add_record('name2', 'g2@g.com', 22, 'Somewhere')
        udm.delete_record_by_email('g2@g.com')
        found = udm.search_by_age(22)

        self.assertTrue(found)
        self.assertIn(created1, found)
        self.assertNotIn(created2, found)

    def test_get_all_empty(self):
        udm = UDM()
        records = udm.get_all_records()

        self.assertFalse(records)

    def test_get_all_filled(self):
        udm = UDM()
        created1 = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        created2 = udm.add_record('name2', 'g2@g.com', 23, 'over there')
        created3 = udm.add_record('name2', 'g3@g.com', 23, 'not Somewhere')
        records = udm.get_all_records()

        self.assertTrue(records)
        self.assertEqual(3, len(records))
        self.assertIn(created1, records)

    def test_get_all_after_deletion(self):
        udm = UDM()
        created1 = udm.add_record('name', 'g@g.com', 22, 'Somewhere')
        created2 = udm.add_record('name2', 'g2@g.com', 23, 'over there')
        created3 = udm.add_record('name2', 'g3@g.com', 23, 'not Somewhere')
        udm.delete_record_by_email('g@g.com')
        records = udm.get_all_records()

        self.assertTrue(records)
        self.assertEqual(2, len(records))
        self.assertNotIn(created1, records)


if __name__ == "__main__":
    unittest.main()
