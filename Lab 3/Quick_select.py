# returns value of kth smallest element
def quick_select(a, k):
    print("\narray " + str(a))
    pivot = a[len(a) - 1]
    print("pivot = " + str(pivot))
    print("k = " + str(k))
    a = partition(a, pivot)
    print("after partition" + str(a))
    # gets pivot index
    pivot_index = a.index(pivot)
    if k == pivot_index + 1:
        print("\nkth smallest element is " + str(a[pivot_index]))
    elif k < pivot_index + 1:
        print("k is < pivot index")
        quick_select(a[0:pivot_index], k)
    elif k > pivot_index + 1:
        print("k is > pivot index")
        quick_select(a[pivot_index + 1:len(a)], k - (pivot_index + 1))

# returns max k numbers
def max_k(a, k):
    # print("\narray " + str(a))
    pivot = a[len(a) - 1]
    # print("pivot = " + str(pivot))
    # print("k = " + str(k))
    a = partition(a, pivot)
    # gets pivot index
    pivot_index = a.index(pivot)
    # print("pivot index = " + str(pivot_index))
    if k == len(a):
        print("\nmax k numbers are " + str(a))
    elif k == len(a[pivot_index:len(a)]):
        print("\nmax k numbers are " + str(a[pivot_index:len(a)]))
    elif k < len(a[pivot_index:len(a)]):
        # print("k is < pivot till end")
        max_k(a[pivot_index + 1:len(a)], k)
    elif k > len(a[pivot_index:len(a)]):
        # print("k is > pivot till end")
        a.remove(min(a))
        max_k(a, k)

# returns array with pivot in the middle
def partition(a, pivot):
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
