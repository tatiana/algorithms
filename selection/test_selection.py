import unittest
from selection import remove_smallest


class SelectionByExtremeTestCase(unittest.TestCase):

    def test_remove_smaller_1_range_1(self):
        original_list = [0]
        expected = []
        answer = remove_smallest(original_list)
        self.assertEquals(expected, answer)

    def test_remove_smaller_1_range_3(self):
        original_list = [0, 1, 2]
        expected = [1, 2]
        answer = remove_smallest(original_list)
        self.assertEquals(expected, answer)

    def test_remove_smaller_1_raffled_range_5(self):
        original_list = [4, 1, 3, 2, 0]
        expected = [4, 1, 3, 2]
        answer = remove_smallest(original_list)
        self.assertEquals(expected, answer)

if __name__ == '__main__':
    unittest.main()
