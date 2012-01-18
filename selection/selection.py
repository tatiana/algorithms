INFINITY = float('Inf')


def remove_smallest(unsorted_list):
    smaller = INFINITY
    for value in unsorted_list:
        if value < smaller:
            smaller = value
    unsorted_list.remove(smaller)
    return smaller, unsorted_list


def kth_by_extreme(unsorted_list, k):
    for ith in xrange(k):
        kth, unsorted_list = remove_smallest(unsorted_list)
    return kth
