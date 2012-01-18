import unittest
from algorithms.selection import kth_by_extreme, kth_by_sorting


class SelectionByExtremeTestCase(unittest.TestCase):

    def test_kth_by_extreme_list_2_return_2(self):
        "Selection by Extreme: list=[2] kth=1 returns 2"
        original_list = [2]
        kth = 1
        expected = 2
        received = kth_by_extreme(original_list, kth)
        self.assertEquals(expected, received)

    def test_kth_by_extreme_shuffled_range_1_10_return_3th_item(self):
        "Selection by Extreme: list=[3, 5, 8, 4, 2, 7, 6, 1, 9] kth=3 returns 3"
        original_list = [3, 5, 8, 4, 2, 7, 6, 1, 9]
        expected = 3
        received = kth_by_extreme(original_list, 3)
        self.assertEquals(expected, received)


class SelectionBySortingTestCase(unittest.TestCase):

    def test_kth_by_extreme_range_3_return_2th_item(self):
        "Selection by Sorting: list=[0, 1, 2] kth=2 returns 1"
        original_list = [0, 1, 2]
        kth = 2
        expected = 1
        received = kth_by_sorting(original_list, kth)
        self.assertEquals(expected, received)

    def test_kth_by_extreme_unsorted_list_of_6_and_return_4th_item(self):
        "Selection by Sorting: list=[5, 7, 10, 2, 6, 33] kth=4 returns 7"
        original_list = [5, 7, 10, 2, 6, 33]
        kth = 4
        expected = 7
        received = kth_by_sorting(original_list, kth)
        self.assertEquals(expected, received)

    def test_kth_by_extreme_shuffled_range_1_10_return_3th_item(self):
        "Selection by Sorting: list=[3, 5, 8, 4, 2, 7, 6, 1, 9] kth=3 returns 3"
        original_list = [3, 5, 8, 4, 2, 7, 6, 1, 9]
        kth = 3
        expected = 3
        received = kth_by_sorting(original_list, kth)
        self.assertEquals(expected, received)


if __name__ == '__main__':
    unittest.main()
