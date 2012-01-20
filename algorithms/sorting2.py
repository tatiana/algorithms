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


def mergesort_r(list2, first, last):
    if first < last:
        sred = (first + last)/2
        mergesort_r(list2, first, sred)
        mergesort_r(list2, sred + 1, last)
        merge(list2, first, last, sred)

def mergesort(list2):
    mergesort_r(list2, 0, len(list2) -1)
    return list2

