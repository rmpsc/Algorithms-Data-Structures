# Romel Pascua
# 017167304
# CECS 328 Lab 6

from algo import *

arr = [6, 2, -5, 6, -8, 3, 10, -2, 4, -1]
arr2 = [6, 2, -3, 1, -.9, 2]
mpss = MPSS(arr2, 0, len(arr2) - 1)
print("maximum positive sum = " + str(mpss))

'''
Time complexity
T(n) = Θ(nlog2 n) is for MSS. Each subarray has a size of n/2
The reason MPSS is T(n) = Θ(nlog2 n) is because we have the two subarrays (SL and SR)
In the worst case for our while loop in Find_MPSS_M, we will go thru both arrays, which is equal to n
This extra n that we must go thru is what changes the time complexity compared to MSS

How/why MPSS works
MPSS splits the array in half just like MSS and recursively calls itself to find MPSS_L and MPSS_R
The while loop in Find_MPSS_M starts with the least value from SL and the greatest from SR
if the sum of those two values are less than 0, we increment i since SL is sorted in ascending order
we do this because we want a positive value. if s < smin, that means we have found a sum that is less than
our current sum and we must replace it. We increment j in this case in hope to find an even smaller sum.
s > smin means that we have yet to find a smalller sum and must increment j to hope to so. Once one of the arrays
have been exhausted, we know smin is the smallest it can be which is what gets returned.
'''