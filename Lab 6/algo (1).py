import numpy as np

def MPSS(a, s, e):

    # base case
    if s == e:
        if a[s] > 0:
            return a[s]
        if a[s] < 0:
            return float('inf')

    # index of middle point
    m = (s + e) // 2

    # return min between the left, right, and mid
    MPSS_L = MPSS(a, s, m)
    MPSS_R = MPSS(a, m + 1, e)
    MPSS_M = Find_MPSS_M(a, s, e)
    return min(MPSS_L, MPSS_R, MPSS_M)


def Find_MPSS_M(a, s, e):
    m = (s + e) // 2
    MPSS_L = a[s:m]
    MPSS_R = a[m:e]
    SL = []
    SR = []

    # adds elements in MPSS_L (adds one to left every iteration)
    for i in range(len(MPSS_L)):
        SL.append(np.sum(MPSS_L[i:len(MPSS_L) + 1]))

    # adds elements in MPSS_R (adds one to right every iteration)
    for i in range(len(MPSS_R)):
        SR.append(np.sum(MPSS_R[0:i + 1]))
 
    SL.sort()
    SR.sort()
    SR.reverse()

    i = 0
    j = 0
    s_min = float('inf')

    while i < len(SL) and j < len(SR):
        s = SL[i] + SR[j]
        if s <= 0:
            i += 1
        elif s < s_min:
            s_min = s
            j += 1
        else:
            j += 1

    return s_min


