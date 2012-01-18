INFINITY = float('Inf')


def remove_smallest(unsorted_list):
    smaller = INFINITY
    for value in unsorted_list:
        if value < smaller:
            smaller = value
    unsorted_list.remove(smaller)
    return smaller, unsorted_list


def split_list(sorted_list, value):
    smaller = []
    larger = []
    for item in sorted_list:
        if item < value:
            smaller.append(item)
        else:
            larger.append(item)
    return smaller, larger
