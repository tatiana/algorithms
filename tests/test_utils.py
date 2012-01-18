import unittest
from algorithms.utils import remove_smallest


class RemoveSmallestTestCase(unittest.TestCase):

    def test_remove_smallest_range_1_return_0(self):
        "Utils - remove_smallest: [0] returns (0, [])"
        original_list = [0]
        expected = (0, [])
        received = remove_smallest(original_list)
        self.assertEquals(expected, received)

    def test_remove_smallest_range_3_return_0(self):
        "Utils - remove_smallest: [0, 1, 2] returns (0, [1, 2])"
        original_list = [0, 1, 2]
        expected = (0, [1, 2])
        received = remove_smallest(original_list)
        self.assertEquals(expected, received)

    def test_remove_smallest_shuffled_range_1_to_6_return_1(self):
        "Utils - remove_smallest: [4, 1, 3, 2, 5] returns (1, [4, 3, 2, 5])"
        original_list = [4, 1, 3, 2, 5]
        expected = (1, [4, 3, 2, 5])
        received = remove_smallest(original_list)
        self.assertEquals(expected, received)
