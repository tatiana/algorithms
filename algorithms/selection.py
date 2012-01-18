from algorithms.sorting import mergesort
from utils import remove_smallest


def kth_by_extreme(unsorted_list, k):
    for ith in xrange(k):
        kth, unsorted_list = remove_smallest(unsorted_list)
    return kth


def kth_by_sorting(unsorted_list, k):
    sorted_list = mergesort(unsorted_list)
    kth = sorted_list[k - 1]
    return kth
