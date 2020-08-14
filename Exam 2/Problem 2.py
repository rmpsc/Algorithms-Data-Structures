from functions import *

# solution 1
'''
def merge_arrays(m):
    # finds # of arrays and size of each array
    k = len(m)
    n = len(m[0])
    merged_arr = []

    for i in range(k):
        for j in range(n):
            merged_arr.append(m[i][j])

    print("before = " + str(merged_arr))
    heap_sort(merged_arr)
    return merged_arr


sorted_arr = merge_arrays(matrix)
print("after = " + str(sorted_arr))
'''

# solution 2
matrix = [[8, 4, 2, 0],
          [20, 15, 5, 3],
          [10, 7, 6, 1]]

def mergef_arrays(m):
    # finds # of arrays and size of each array
    k = len(m)
    n = len(m[0])
    merged_arr = []
    max_heap = []

    count = 1
    # keeps going until matrix has no more elements
    # while not m.all():
    while count > 0:
        print(m)

        for i in range(k):
            if len(m[i]) != 0:
                max_heap.append(m[i][0])

        print("max heap = " + str(max_heap))
        build_MaxHeap(max_heap, len(max_heap))
        print("max heap = " + str(max_heap))

        # adding root to merged_arr
        merged_arr.append(max_heap[0])
        print("root = " + str(max_heap[0]))
        print("merged arr = " + str(merged_arr))

        # removing root from matrix and max_heap
        print(m)

        for i in range(k):
            if max_heap[0] in m[i]:
                m[i].remove(m[i][0])
        print(m)

        max_heap.clear()

        count = 0
        for i in range(k):
            if m[i]:
                count += 1
        print("count = " + str(count))
        print("\n")

    return merged_arr


def merge_arrays(m):
    # finds # of arrays and size of each array
    k = len(m)
    n = len(m[0])
    merged_arr = []
    max_heap = []

    count = 1
    while count > 0:
        for i in range(k):
            if len(m[i]) != 0:
                max_heap.append(m[i][0])
        build_MaxHeap(max_heap, len(max_heap))

        # adding root to merged_arr
        merged_arr.append(max_heap[0])

        # removing root from matrix
        for i in range(k):
            if max_heap[0] in m[i]:
                m[i].remove(m[i][0])
                break
        # clearing max heap
        max_heap.clear()

        # checks if matrix still holds values
        count = 0
        for i in range(k):
            if m[i]:
                count += 1

    return merged_arr


final_arr = merge_arrays(matrix)
print(final_arr)
