import unittest
from check_pwd import check_pwd


class TestCheckPwd (unittest.TestCase):

    def test_assert_false(self):
        """tests takes a blank entry and should return false"""
        self.assertFalse(check_pwd(""))

    def test_short_length(self):
        """testing for a length less than the min"""
        self.assertFalse(check_pwd("Test.1"))

    def testing_valid_length(self):
        """testing for a valid length"""
        self.assertTrue(check_pwd("Test.length13"))

    def testing_long_length(self):
        """testing a length that is more than the length"""
        self.assertFalse(check_pwd("Test.lengthOverTwenty"))





if __name__ == '__main__':
    unittest.main()
