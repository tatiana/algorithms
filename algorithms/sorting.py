from utils import split_list


def merge(left, right):
    # TODO: Needs testing
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
