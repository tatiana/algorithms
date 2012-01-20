import pickle
import random

MAX_SIZE = 15

def logn_shuffle(sorted_list):
    size = len(sorted_list)
    unsorted_list = []
    if size < 2:
        unsorted_list = sorted_list
    elif size == 2:
        unsorted_list = [sorted_list[1], sorted_list[0]]
    else:
        first_half = sorted_list[0:size/2]
        second_half = sorted_list[size/2:size+1]
        item_from_first = first_half[-1]
        item_from_second = second_half[0]
        first_half[-1] = item_from_second
        second_half[0] = item_from_first
        first_half = logn_shuffle(first_half)
        #second_half = logn_shuffle(second_half)
        unsorted_list = first_half + second_half
    return unsorted_list

def get_sorted_list(i):
    sorted_list = range(1, (1000 * 2 ** i) + 1)
    return sorted_list

def get_shuffled_list(i):
    list_ = get_sorted_list(i)
    random.shuffle(list_)
    return list_

def get_logn_shuffled_list(i):
    sorted_list = get_sorted_list(i)
    unsorted_list = logn_shuffle(sorted_list)
    return unsorted_list

def write_list_to_file(unsorted_list, filename):
    fp = open(filename, 'w')
    pickle.dump(unsorted_list, fp)
    fp.close()

if __name__ == '__main__':
    import time
    for i in xrange(1, MAX_SIZE+1):
        initial_time = time.time()
        sorted_list = get_sorted_list(i)
        sorted_time = time.time() - initial_time
        print "--- sorted list: ", sorted_time
        shuffled_list = get_shuffled_list(i)
        shuffled_time = time.time() - sorted_time
        write_list_to_file(shuffled_list, "sample/shuffled_list_%.2d.pkl" % i)
        print "--- shuffled list: ", shuffled_time
        logn_shuffled_list = get_logn_shuffled_list(i)
        logn_shuffled_time = time.time() - sorted_time
        write_list_to_file(logn_shuffled_list, "sample/logn_shuffled_list_%.2d.pkl" % i)
        print "--- lognshuffled list: ", logn_shuffled_time
        final_time = time.time()
        print "i: %d, time: %f" % (i, final_time - initial_time)

