import unittest
from algorithms.utils import isprime, next_prime, remove_smallest


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

class IsPrimeTestCase(unittest.TestCase):

    def test_2_is_prime(self):
        assert isprime(2)

    def test_7_is_prime(self):
        assert isprime(7)

    def test_4_is_not_prime(self):
        assert not isprime(4)

    def test_44909_is_prime(self):
        assert isprime(44909)

    def test_50000_is_not_prime(self):
        assert not isprime(50000)


class NextPrimeTestCase(unittest.TestCase):

    def test_3_is_next_prime_of_2(self):
        assert next_prime(2) == 3

    def test_13_is_next_prime_of_11(self):
        assert next_prime(11) == 13

    def test_17_is_next_prime_of_15(self):
        assert next_prime(15) == 17

    def test_12611_is_nex_prime_of_12601(self):
        assert next_prime(12601) == 12611
