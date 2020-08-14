# Romel Pascua
# 017167304
# 4/2/2020
# CECS 328 LAB 5
import random
import timeit
from Heaps import *

print("Part A")
# fills arr with random integers n times
n = int(input("How many values would you like in your array? "))
arr = []

for i in range(n):
    arr.append(random.randint(-99, 99))

print(arr)
heap_sort(arr)
print(arr)

print("\nAvg-running time of heap sort and selection sort for n=1000 and 100 repetitions")
print("\nComputing...")
heapTime = 0
selectionTime = 0
numTimes = 100
n = 1000
for i in range(numTimes):
    arr.clear()
    for j in range(n):
        arr.append(random.randint(-99, 99))
    timeStart = timeit.default_timer()
    heap_sort(arr)
    timeEnd = timeit.default_timer()
    heapTime += (timeEnd - timeStart)
heapFinal = heapTime / numTimes

for i in range(numTimes):
    arr.clear()
    for j in range(n):
        arr.append(random.randint(-99, 99))
    timeStart = timeit.default_timer()
    selection_sort(arr)
    timeEnd = timeit.default_timer()
    selectionTime += (timeEnd - timeStart)
selectionFinal = selectionTime / numTimes

print("Heap Sort Avg: " + '{0:.2g}'.format(heapFinal))
print("Selection Sort Avg: " + '{0:.2g}'.format(selectionFinal))

print("\nPart B")
n = 10
arr.clear()
for i in range(n):
    arr.append(random.randint(-99, 99))
print("Unsorted: " + str(arr))
heap_sort(arr)
print("Sorted: " + str(arr))

