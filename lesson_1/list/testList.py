import unittest
from lesson_1.list.num3 import num3


class TestList (unittest.TestCase):
    def test_num3_first(self):
        my_list = [1, 3, 5, 2, 3, 8, 10, 9, 6, 5, 7, 9, 0]
        self.assertEqual(num3(my_list), [2, 3, 8, 10])

    def test_num3_second(self):
        self.assertEqual(num3([1, 2, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()