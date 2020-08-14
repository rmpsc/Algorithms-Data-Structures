# algorithms used in Lab1
# a = array
# key = random int in array


def linearSearch(a, key):
    n = len(a)
    for i in range(n):
        if key == a[i]:
            return True
    return False
# if false (worst case)
# line being ran is 2n+1

def binarySearch(a, key):
    left = 0
    right = len(a) - 1
    while left < right:
        mid = int((left + right) / 2)
        if key == a[mid]:
            return True
        if key <= a[mid]:
            right = mid - 1
        if key >= a[left]:
            left = mid + 1
    # each while run for worst case runs 6 lines
    return False
