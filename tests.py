import unittest
from check_pwd import check_pwd


class TestCheckPwd (unittest.TestCase):

    def test_assert_false(self):
        """tests a valid min password length"""
        self.assertFalse(check_pwd())




if __name__ == '__main__':
    unittest.main()
