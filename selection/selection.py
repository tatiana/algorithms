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

def merge(left, right):
    result = []
    for item in left:
        smaller_items, right = split_list(right, item)
        result = result + smaller_items + [item]
    if right:
        result = result + right
    return result


def mergesort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    else:
        middle = len(unsorted_list) / 2
        left_list = unsorted_list[:middle]
        left = mergesort(left_list)
        right_list = unsorted_list[middle:]
        right = mergesort(right_list)
        return merge(left, right)


def kth_by_extreme(unsorted_list, k):
    for ith in xrange(k):
        kth, unsorted_list = remove_smallest(unsorted_list)
    return kth


def kth_by_sorting(unsorted_list, k):
    sorted_list = mergesort(unsorted_list)
    kth = sorted_list[k-1]
    return kth
