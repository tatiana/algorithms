import random
import unittest
from algorithms.sorting import mergesort


class MergeSortTestCase(unittest.TestCase):

    def test_sort_single_item(self):
        "Sort by MergeSort: list=[4] returns [4]"
        shuffled = [4]
        expected = [4]
        received = mergesort(shuffled)
        self.assertEquals(expected, received)

    def test_sort_range_4(self):
        "Sort by MergeSort: list=[3, 2, 1, 0] returns [0, 1, 2, 3]"
        shuffled = [3, 2, 1, 0]
        expected = [0, 1, 2, 3]
        received = mergesort(shuffled)
        self.assertEquals(expected, received)

    def test_sort_range_50(self):
        "Sort by MergeSort: shuffled 50 items list"
        expected = range(50)
        shuffled = range(50)
        random.shuffle(shuffled)
        received = mergesort(shuffled)
        self.assertEquals(expected, received)
