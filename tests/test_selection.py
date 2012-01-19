import unittest
from algorithms.selection import kth_by_extreme, kth_by_sorting, kth_by_mom

# TODO: Try using unittest2 on this CommonTests class
# http://docs.python.org/library/unittest.html#load-tests-protocol
class CommonTests(object):

    def test_kth_list_2_return_2(self):
        original_list = [2]
        kth = 1
        expected = 2
        received = self.selection_func(original_list, kth)
        self.assertEquals(expected, received)

    def test_kth_range_3_return_2th_item(self):
        "Selection by Sorting: list=[0, 1, 2] kth=2 returns 1"
        original_list = [0, 1, 2]
        kth = 2
        expected = 1
        received = self.selection_func(original_list, kth)
        self.assertEquals(expected, received)

    def test_kth_shuffled_list_of_6_and_return_4th_item(self):
        original_list = [5, 7, 10, 2, 6, 33]
        kth = 4
        expected = 7
        received = self.selection_func(original_list, kth)
        self.assertEquals(expected, received)

    def test_kth_shuffled_range_1_10_return_3th_item(self):
        original_list = [3, 5, 8, 4, 2, 7, 6, 1, 9]
        kth = 3
        expected = 3
        received = self.selection_func(original_list, kth)
        self.assertEquals(expected, received)


class SelectionByExtremeTestCase(unittest.TestCase, CommonTests):

    def setUp(self):
        self.selection_func = kth_by_extreme


class SelectionBySortingTestCase(unittest.TestCase, CommonTests):

    def setUp(self):
        self.selection_func = kth_by_sorting


class SelectionByMOMTestCase(unittest.TestCase, CommonTests):

    def setUp(self):
        self.selection_func = kth_by_mom

    def test_kth_by_mom_range_3_return_2th_item(self):
        original_list = range(1, 16)
        kth = 8
        expected = 8
        received = kth_by_mom(original_list, kth)
        self.assertEquals(expected, received)


if __name__ == '__main__':
    unittest.main()
