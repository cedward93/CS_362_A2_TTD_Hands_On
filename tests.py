import unittest
from check_pwd import check_pwd


class TestCheckPwd (unittest.TestCase):

    def test_valid_min_length(self):
        """tests a valid password length"""
        self.assertTrue(check_pwd("12345678"))


if __name__ == '__main__':
    unittest.main()
