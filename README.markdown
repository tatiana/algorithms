# Algorithms' implementations in Python

The aim of this project is to implement some algorithms I've studied in Python,
just for fun. ;)

## selection

Algorithms for finding the kth smallest number in a list (the kth order statistic). This includes the cases of finding the minimum, maximum, and median elements.

* kth_by_extreme        O(kn)     # Select discarding smaller item k times
* kth_by_sorting        O(nlogn)  # Select kth smaller after sorting with mergesort
* kth_by_mom            O(n)      # Select kth smaller using the median of medians
* kth_by_quickselect    O(n)      # Select kth smaller using quick select

## sorting

Algorithms for sorting - yep, I know Python's default sort method ;)

* mergesort                 O(nlogn)
