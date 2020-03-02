import unittest
from UserDirectoryManager import UserDirectoryManager as UDM

class TestingFilecmp(unittest.TestCase):
    def test_add_record(self):
        pass

    def test_add_record_null(self):
        pass

    def test_add_record_repeated_email(self):
        pass

    def test_del_record(self):
        pass

    def test_del_record_none(self):
        pass

    def test_del_record_non_existent(self):
        pass
    
    def test_search_email(self):
        pass

    def test_search_email_deleted(self):
        pass

    def test_search_email_non_existent(self):
        pass

    def test_search_age(self):
        pass

    def test_search_age_non_existent(self):
        pass

    def test_search_age_none(self):
        pass

    def test_search_age_deleted(self):
        pass

    def test_get_all_empty(self):
        pass
    
    def test_get_all_filled(self):
        pass

    def test_get_all_after_deletion(self):
        pass

if __name__ == "__main__":
    unittest.main()