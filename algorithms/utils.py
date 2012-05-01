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


def isprime(n):
    n *= 1.0
    if n % 2 == 0 and n != 2 or n % 3 == 0 and n != 3:
        return False
    for b in range(1, int((n ** 0.5 + 1) / 6.0 + 1)):
        if n % (6 * b - 1) == 0:
            return False
        if n % (6 * b + 1) == 0:
           return False
    return True


def next_prime(n):
    for number in xrange(n + 1, 2 * n):
        if isprime(number):
            return number
