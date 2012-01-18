import unittest
from selection import remove_smallest


class SelectionByExtremeTestCase(unittest.TestCase):

    def test_remove_smaller_1_range_1(self):
        original_list = range(1)  # [0]
        expected = []
        answer = remove_smallest(original_list)
        self.assertEquals(expected, answer)

if __name__ == '__main__':
    unittest.main()
