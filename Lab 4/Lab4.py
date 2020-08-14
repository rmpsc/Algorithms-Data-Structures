import random
import math
from Quick_select import *

# fills arr with random integers n times
n = int(input("How many values would you like in your array? "))
arr = []

for i in range(n):
    arr.append(random.randint(-99, 99))

k = int(input("How many closest values to the median would you like? "))
while k > n:
    k = int(input("k must be smaller than the array size! "))

# stores differences of median
diff = []

# ceil makes k equal middle number in array
# ex) 5 / 2 = 2.5 -> 3
median = median(arr, math.ceil(len(arr) / 2))

# populates array with the differences from the median
for i in arr:
    diff.append(i - median)

# removes one zero from diff array which would be the median
for i in diff:
    if i == 0:
        diff.remove(i)
        break

print("\nyour array: " + str(arr))
print("median = " + str(median))
print("diff array: " + str(diff))

# integers before the median is added back to them
sm_elements = quick_select(diff, k)

result = []

for i in sm_elements:
    result.append(i + median)

print("\nthe " + str(k) + " nearest elements to the median are " + str(result))
