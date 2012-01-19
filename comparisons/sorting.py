# timing 8 different Python sorting algorithms with a list of integers
# each function is given the same list (fresh copy each time)
# tested with Python24       vegaseat      21jan2006
# tested with Python27   tati_alchueyr     19jan2012
# adapted from:
# http://www.daniweb.com/software-development/python/code/216689

import random  # for generating random numbers
import time    # for timing each sort function with time.clock()

DEBUG = False  # set True to check results of each sort

N = 1000     # number of elements in list
list1 = []   # list of integer elements

for i in range(0, N):
    list1.append(random.randint(0, N-1))

#print list1  # test

def print_timing(func):
    def wrapper(*arg):
        t1 = time.clock()
        res = func(*arg)
        t2 = time.clock()
        print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

# declare the @ decorator just above each sort function, invokes print_timing()
@print_timing
def adaptive_merge_sort(list2):
    """adaptive merge sort, built into Python since version 2.3"""
    list2.sort()

@print_timing
def bubble_sort(list2):
    #swap_test = False
    for i in range(0, len(list2) - 1):
        # as suggested by kubrick, makes sense
        swap_test = False
        for j in range(0, len(list2) - i - 1):
            if list2[j] > list2[j + 1]:
                list2[j], list2[j + 1] = list2[j + 1], list2[j]  # swap
            swap_test = True
        if swap_test == False:
            break

# selection sort
@print_timing
def selection_sort(list2):
    for i in range(0, len (list2)):
        min = i
        for j in range(i + 1, len(list2)):
            if list2[j] < list2[min]:
                min = j
        list2[i], list2[min] = list2[min], list2[i]  # swap

# insertion sort
@print_timing
def insertion_sort(list2):
    for i in range(1, len(list2)):
        save = list2[i]
        j = i
        while j > 0 and list2[j - 1] > save:
            list2[j] = list2[j - 1]
            j -= 1
        list2[j] = save

# quick sort
@print_timing
def quick_sort(list2):
    quick_sort_r(list2, 0, len(list2) - 1)

# quick_sort_r, recursive (used by quick_sort)
def quick_sort_r(list2 , first, last):
    if last > first:
        pivot = partition(list2, first, last)
        quick_sort_r(list2, first, pivot - 1)
        quick_sort_r(list2, pivot + 1, last)

# partition (used by quick_sort_r)
def partition(list2, first, last):
    sred = (first + last)/2
    if list2[first] > list2 [sred]:
        list2[first], list2[sred] = list2[sred], list2[first]  # swap
    if list2[first] > list2 [last]:
        list2[first], list2[last] = list2[last], list2[first]  # swap
    if list2[sred] > list2[last]:
        list2[sred], list2[last] = list2[last], list2[sred]    # swap
    list2 [sred], list2 [first] = list2[first], list2[sred]    # swap
    pivot = first
    i = first + 1
    j = last

    while True:
        while i <= last and list2[i] <= list2[pivot]:
            i += 1
        while j >= first and list2[j] > list2[pivot]:
            j -= 1
        if i >= j:
            break
        else:
            list2[i], list2[j] = list2[j], list2[i]  # swap
    list2[j], list2[pivot] = list2[pivot], list2[j]  # swap
    return j

# heap sort
@print_timing
def heap_sort(list2):
    first = 0
    last = len(list2) - 1
    create_heap(list2, first, last)
    for i in range(last, first, -1):
        list2[i], list2[first] = list2[first], list2[i]  # swap
        establish_heap_property (list2, first, i - 1)

# create heap (used by heap_sort)
def create_heap(list2, first, last):
    i = last/2
    while i >= first:
        establish_heap_property(list2, i, last)
        i -= 1

# establish heap property (used by create_heap)
def establish_heap_property(list2, first, last):
    while 2 * first + 1 <= last:
        k = 2 * first + 1
        if k < last and list2[k] < list2[k + 1]:
            k += 1
        if list2[first] >= list2[k]:
            break
        list2[first], list2[k] = list2[k], list2[first]  # swap
        first = k

# merge sort
@print_timing
def merge_sort(list2):
    merge_sort_r(list2, 0, len(list2) -1)

# merge sort recursive (used by merge_sort)
def merge_sort_r(list2, first, last):
    if first < last:
        sred = (first + last)/2
        merge_sort_r(list2, first, sred)
        merge_sort_r(list2, sred + 1, last)
        merge(list2, first, last, sred)

# merge (used by merge_sort_r)
def merge(list2, first, last, sred):
    helper_list = []
    i = first
    j = sred + 1
    while i <= sred and j <= last:
        if list2 [i] <= list2 [j]:
            helper_list.append(list2[i])
            i += 1
        else:
            helper_list.append(list2 [j])
            j += 1
    while i <= sred:
        helper_list.append(list2[i])
        i +=1
    while j <= last:
        helper_list.append(list2[j])
        j += 1
    for k in range(0, last - first + 1):
        list2[first + k] = helper_list [k]

# test sorted list by printing the first 10 elements
def print10(list2):
    for k in range(10):
        print list2[k],
    print

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

def merge_tati(left, right):
    # TODO: Needs testing
    result = []
    for item in left:
        smaller_items, right = split_list_by_pivot(right, item)
        result = result + smaller_items + [item]
    if right:
        result = result + right
    return result

@print_timing
def mergesort_tati(unsorted_list):
    return mergesort_tati_r(unsorted_list)

def mergesort_tati_r(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    else:
        middle = len(unsorted_list) / 2
        left_list = unsorted_list[:middle]
        left = mergesort_tati_r(left_list)
        right_list = unsorted_list[middle:]
        right = mergesort_tati_r(right_list)
        return merge_tati(left, right)

# run test if script is executed
if __name__ == "__main__" :
    print "timing 7 sorting algorithms with a list of 1000 integers:"
    # make a true copy of list1 each time
    list2 = list(list1)
    adaptive_merge_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    bubble_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    heap_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    insertion_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    merge_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    quick_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    selection_sort(list2)
    if DEBUG:
        print10(list2)

    list2 = list(list1)
    mergesort_tati(list2)


    # final test
    list2 = list(list1)
    if DEBUG:
        print "final test: ",
        print10(list2)

    #raw_input( "Press Enter to continue..." )

"""
typical results:
timing 7 sorting algorithms with a list of 1000 integers:
adaptive_merge_sort took 0.343ms
bubble_sort took 146.491ms
heap_sort took 7.405ms
insertion_sort took 70.918ms
merge_sort took 6.770ms
quick_sort took 4.501ms
selection_sort took 61.769ms
"""

