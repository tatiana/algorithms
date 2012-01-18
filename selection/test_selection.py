import unittest
from selection import remove_smallest


class SelectionByExtremeTestCase(unittest.TestCase):

    def test_remove_smallest_0_range_1(self):
        original_list = [0]
        expected = (0, [])
        answer = remove_smallest(original_list)
        self.assertEquals(expected, answer)

    def test_remove_smallest_0_range_3(self):
        original_list = [0, 1, 2]
        expected = (0, [1, 2])
        answer = remove_smallest(original_list)
        self.assertEquals(expected, answer)

    def test_remove_smallest_1_raffled_range_1_to_6(self):
        original_list = [4, 1, 3, 2, 5]
        expected = (1, [4, 3, 2, 5])
        answer = remove_smallest(original_list)
        self.assertEquals(expected, answer)



if __name__ == '__main__':
    unittest.main()
