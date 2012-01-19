# Algorithms' implementations in Python

The aim of this project is to implement some algorithms I've studied in Python,
for fun. ;)

## selection

Algorithms for finding the kth smallest number in a list (the kth order statistic). This includes the cases of finding the minimum, maximum, and median elements.

* kth_by_extreme        O(kn)     # Searching smaller k times
* kth_by_sorting        O(nlogn)  # Using mergesort
* kth_by_mom            O(n)      # Median of medians
* kth_random_pivot      O(n)

## sorting

Algorithms for sorting - yep, I know Python's default sort method ;)

* mergesort                 O(nlogn)
