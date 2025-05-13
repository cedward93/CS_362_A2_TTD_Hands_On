import unittest
from check_pwd import check_pwd

class TestCheckPwd (unittest.TestCase):

    def test_valid_length(self):
        self.assertTrue(check_pwd("12345678"))