def heap_sort(a):
    n = len(a)

    build_MinHeap(a, n)

    # n-1 is the last leaf in the tree
    for i in range(n-1, 0, -1):
        # swaps the root with the last leaf
        swap(a, i, 0)
        min_heapify(a, i, 0)

def build_MaxHeap(a, n):
    for i in range(int(n/2 - 1), -1, -1):
        max_heapify(a, n, i)

def build_MinHeap(a, n):
    for i in range(int(n/2 - 1), -1, -1):
        min_heapify(a, n, i)

# i = index of the element
# n = size of the array
def max_heapify(a, n, i):
    big = i
    parent = (i - 1) / 2
    Lidx = (2 * i) + 1
    Ridx = (2 * i) + 2

    if Lidx < n and a[Lidx] > a[i]:
        big = Lidx

    # makes sure Ridx > Lidx before changing big
    if Ridx < n and a[Ridx] > a[i] and a[Ridx] > a[Lidx]:
        big = Ridx

    if big != i:
        # swaps big and i
        swap(a, i, big)

        max_heapify(a, n, big)

def min_heapify(a, n, i):
    little = i
    parent = (i - 1) / 2
    Lidx = (2 * i) + 1
    Ridx = (2 * i) + 2

    if Lidx < n and a[Lidx] < a[i]:
        little = Lidx

    # makes sure Ridx < Lidx before changing big
    if Ridx < n and a[Ridx] < a[i] and a[Ridx] < a[Lidx]:
        little = Ridx

    if little != i:
        # swaps big and i
        swap(a, i, little)

        min_heapify(a, n, little)

def swap(a, p1, p2):
    a[p1], a[p2] = a[p2], a[p1]