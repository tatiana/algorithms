INFINITY = float('Inf')


def remove_smallest(unsorted_list):
    smaller = INFINITY
    for value in unsorted_list:
        if value < smaller:
            smaller = value
    unsorted_list.remove(smaller)
    return smaller, unsorted_list


def split_list(sorted_list, value):
    # TODO: Needs testing
    smaller = []
    larger = []
    for item in sorted_list:
        if item < value:
            smaller.append(item)
        else:
            larger.append(item)
    return smaller, larger


def grouper(values_list, n):
    " Split values_list into n-sized chunks"
    # TODO: Needs testing / rename
    for i in xrange(0, len(values_list), n):
        yield values_list[i: i + n]


def split_into_chunks(values_list, n):
    return list(grouper(values_list, n))


def get_kth(unsorted_list, k):
    unsorted_list.sort()
    sorted_list = unsorted_list
    return sorted_list[k - 1]


def get_median(unsorted_list):
    size = len(unsorted_list)
    median_index = (size / 2) + (size % 2)
    return get_kth(unsorted_list, median_index)


def pivot_list(unsorted_list, pivot):
    smaller = []
    larger = []
    for value in unsorted_list:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            larger.append(value)
    return smaller, larger
