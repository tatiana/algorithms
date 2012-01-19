import random
from algorithms.sorting import mergesort
from utils import remove_smallest, split_into_chunks, get_median, get_kth, split_list_by_pivot

CHUNK_SIZE = 5


def kth_by_extreme(unsorted_list, k):
    for ith in xrange(k):
        kth, unsorted_list = remove_smallest(unsorted_list)
    return kth


def kth_by_sorting(unsorted_list, k):
    sorted_list = mergesort(unsorted_list)
    kth = sorted_list[k - 1]
    return kth


def kth_by_mom(unsorted_list, k):
    if len(unsorted_list) <= CHUNK_SIZE:
        return get_kth(unsorted_list, k)

    chunks = split_into_chunks(unsorted_list, CHUNK_SIZE)

    medians_list = []

    for chunk in chunks:
        median_chunk = get_median(chunk)
        medians_list.append(median_chunk)

    size = len(medians_list)
    mom = kth_by_mom(medians_list, size / 2 + (size % 2))
    smaller, larger = split_list_by_pivot(unsorted_list, mom)
    values_before_mom = len(smaller)

    if values_before_mom == (k - 1):
        return mom
    elif values_before_mom > (k - 1):
        return kth_by_mom(smaller, k)
    else:
        return kth_by_mom(larger, k - values_before_mom - 1)


def kth_by_quickselect(unsorted_list, k):
    pivot = random.choice(unsorted_list)
    smaller, larger = split_list_by_pivot(unsorted_list, pivot)
    values_before_pivot = len(smaller)
    if values_before_pivot == k - 1:
        return pivot
    elif values_before_pivot > k - 1:
        return kth_by_quickselect(smaller, k)
    else:
        return kth_by_quickselect(larger, k - values_before_pivot - 1)
