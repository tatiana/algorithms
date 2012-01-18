import random
import unittest
from selection import remove_smallest, kth_by_extreme, kth_by_sorting, mergesort


class RemoveSmallestTestCase(unittest.TestCase):

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

    def test_remove_smallest_shuffled_range_1_to_6_return_1(self):
        original_list = [4, 1, 3, 2, 5]
        expected = (1, [4, 3, 2, 5])
        received = remove_smallest(original_list)
        self.assertEquals(expected, received)


class MergeSortTestCase(unittest.TestCase):

    def test_sort_single_item(self):
        shuffled = [4]
        expected = [4]
        received = mergesort(shuffled)
        self.assertEquals(expected, received)

    def test_sort_range_4(self):
        shuffled = [3, 2, 1, 0]
        expected = [0, 1, 2, 3]
        received = mergesort(shuffled)
        self.assertEquals(expected, received)

    def test_sort_range_50(self):
        expected = range(50)
        shuffled = range(50)
        random.shuffle(shuffled)
        received = mergesort(shuffled)
        self.assertEquals(expected, received)


class SelectionByExtremeTestCase(unittest.TestCase):

    def test_kth_by_extreme_list_2_return_2(self):
        original_list = [2]
        kth = 1
        expected = 2
        received = kth_by_extreme(original_list, kth)
        self.assertEquals(expected, received)

    def test_kth_by_extreme_shuffled_range_1_10_return_3th_item(self):
        original_list = [3, 5, 8, 4, 2, 7, 6, 1, 9]
        expected = 3
        received = kth_by_extreme(original_list, 3)
        self.assertEquals(expected, received)

class SelectionBySortingTestCase(unittest.TestCase):

    def test_kth_by_extreme_range_3_return_2th_item(self):
        original_list = [0, 1, 2]
        kth = 2
        expected = 1
        received = kth_by_sorting(original_list, kth)
        self.assertEquals(expected, received)

    def test_kth_by_extreme_unsorted_list_of_6_and_return_4th_item(self):
        original_list = [5, 7, 10, 2, 6, 33]
        kth = 4
        expected = 7
        received = kth_by_sorting(original_list, kth)
        self.assertEquals(expected, received)

    def test_kth_by_extreme_shuffled_range_1_10_return_3th_item(self):
        original_list = [3, 5, 8, 4, 2, 7, 6, 1, 9]
        expected = 3
        received = kth_by_sorting(original_list, 3)
        self.assertEquals(expected, received)




if __name__ == '__main__':
    unittest.main()
