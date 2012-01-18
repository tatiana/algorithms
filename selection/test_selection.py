import unittest
from selection import remove_smallest, kth_by_extreme


class SelectionByExtremeTestCase(unittest.TestCase):

    def test_remove_smallest_range_1_return_0(self):
        original_list = [0]
        expected = (0, [])
        received = remove_smallest(original_list)
        self.assertEquals(expected, received)

    def test_remove_smallest_range_3_return_0(self):
        original_list = [0, 1, 2]
        expected = (0, [1, 2])
        received = remove_smallest(original_list)
        self.assertEquals(expected, received)

    def test_remove_smallest_raffled_range_1_to_6_return_1(self):
        original_list = [4, 1, 3, 2, 5]
        expected = (1, [4, 3, 2, 5])
        received = remove_smallest(original_list)
        self.assertEquals(expected, received)

    def test_kth_by_extreme_list_2_return_2(self):
        original_list = [2]
        expected = 2
        received = kth_by_extreme(original_list, 1)
        self.assertEquals(expected, received)

    def test_kth_by_extreme_raffled_range_1_10_return_3th_item(self):
        original_list = [3, 5, 8, 4, 2, 7, 6, 1, 9]
        expected = 3
        received = kth_by_extreme(original_list, 3)
        self.assertEquals(expected, received)

if __name__ == '__main__':
    unittest.main()
