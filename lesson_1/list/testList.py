import unittest


class TestList (unittest.TestCase):
    def first_test_num3(self):
        my_list = [1, 3, 5, 2, 3, 8, 10, 9, 6, 5, 7, 9, 0]
        self.assertEqual(num3(my_list), [2, 3, 8, 10])
    def seconf_test_num3(self):
        self.assertEqual(num3([1, 2, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()