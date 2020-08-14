# Romel Pascua
# 017167304
# 2/22/2020
# CECS 328 LAB 1
import random
import timeit
from algo import *
import math

# array which is stored to be size n
a = []
b = []
linTime = 0
binTime = 0

# Part 1
n = int(input("input a positive integer for avg cases "))

# fills array with n random numbers from -1000 to 1000
for i in range(n):
    a.append(random.randint(-1000, 1000))
a.sort()
print(a)

# picks a random value in array and saves it to key
key = random.choice(a)
print("key equals " + str(key))

numTimes = 100
# avg linearSearch time
for i in range(numTimes):
    timeStart = timeit.default_timer()
    linearSearch(a, key)
    timeEnd = timeit.default_timer()
    linTime += (timeEnd - timeStart)
linFinal = linTime / numTimes

# avg binarySearch time
for i in range(numTimes):
    timeStart = timeit.default_timer()
    binarySearch(a, key)
    timeEnd = timeit.default_timer()
    binTime = binTime + (timeEnd - timeStart)
binFinal = binTime / numTimes

print("Linear Avg: " + '{0:.2g}'.format(linFinal))
print("Binary Avg: " + '{0:.2g}'.format(binFinal))

# Part B
n = int(input("input a positive integer for worst cases "))

# fills array with n random numbers from -1000 to 1000
for i in range(n):
    b.append(random.randint(-1000, 1000))

b.sort()
print(b)

worseCaseKey = 5000

timeStart = timeit.default_timer()
linearSearch(a, worseCaseKey)
timeEnd = timeit.default_timer()
linTime = (timeEnd - timeStart)
linTime = (linTime/((2*n) + 1))
# 2*n + 1 total num of lines
# this is time complexity (not exact)

timeStart = timeit.default_timer()
binarySearch(a, worseCaseKey)
timeEnd = timeit.default_timer()
binTime = (timeEnd - timeStart)
binTime = (binTime/math.log(n, 2))

tenPowerOf15 = 1000000000000000

print("One run (Linear) = " + '{0:.2g}'.format(linTime))
print("One run (Binary) = " + '{0:.2g}'.format(binTime))
print("Linear for 10^15 = " + '{0:.2g}'.format(linTime * tenPowerOf15))
print("Binary for 10^15 = " + '{0:.2g}'.format(binTime * tenPowerOf15))
