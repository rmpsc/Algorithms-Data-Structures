# returns k values closest to median
# k keeps the same value
def quick_select(a, k):
    # print("\narray " + str(a))
    pivot = a[len(a) - 1]
    # print("pivot = " + str(pivot))
    a = partition(a, pivot)
    # gets pivot index
    pivot_index = a.index(pivot)

    # if k equals the location of the pivot
    if k == pivot_index + 1:
        return a[0:pivot_index + 1]
    elif k < pivot_index + 1:
        return quick_select(a[0:pivot_index], k)
    elif k > pivot_index + 1:
        add = k - (pivot_index + 1)
        return quick_select(a[0:pivot_index + 1 + add], k)

    return 0


# returns array with pivot in the middle
# compares the absolute values in case negative numbers are in use
def partition(a, pivot):
    new_a = []
    for i in a:
        if abs(i) < abs(pivot):
            new_a.append(i)
    new_a.append(pivot)
    for i in a:
        if abs(i) > abs(pivot):
            new_a.append(i)
    a = new_a
    return a


# returns median of array without sorting
# find the middle element using quick_select
def median(a, k):
    pivot = a[len(a) - 1]

    # keeps pivot in the middle
    a = median_partition(a, pivot)

    # gets pivot index
    pivot_index = a.index(pivot)

    if k == pivot_index + 1:
        # print(str(a[pivot_index]))
        # print(int(a[pivot_index]))
        return int(a[pivot_index])
    elif k < pivot_index + 1:
        return median(a[0:pivot_index], k)
    elif k > pivot_index + 1:
        return median(a[pivot_index + 1:len(a)], k - (pivot_index + 1))

    return 0


# partition function that does not compare the absolute values
# used alongside the median function
def median_partition(a, pivot):
    new_a = []
    for i in a:
        if i < pivot:
            new_a.append(i)
    new_a.append(pivot)
    for i in a:
        if i > pivot:
            new_a.append(i)
    a = new_a
    return a
