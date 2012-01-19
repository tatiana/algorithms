INFINITY = float('Inf')


def remove_smallest(unsorted_list):
    smaller = INFINITY
    for value in unsorted_list:
        if value < smaller:
            smaller = value
    unsorted_list.remove(smaller)
    return smaller, unsorted_list


def split_nsized_chunks(values_list, n):
    # TODO: Needs testing
    "Split values_list into n-sized chunks"
    for i in xrange(0, len(values_list), n):
        yield values_list[i: i + n]


def split_into_chunks(values_list, n):
    return list(split_nsized_chunks(values_list, n))


def get_kth(unsorted_list, k):
    # TODO: Needs testing
    unsorted_list.sort()
    sorted_list = unsorted_list
    return sorted_list[k - 1]


def get_median(unsorted_list):
    # TODO: Needs testing
    size = len(unsorted_list)
    median_index = (size / 2) + (size % 2)
    return get_kth(unsorted_list, median_index)


def split_list_by_pivot(unsorted_list, pivot):
    # TODO: Needs testing
    smaller = []
    larger = []
    for value in unsorted_list:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            larger.append(value)
    return smaller, larger
