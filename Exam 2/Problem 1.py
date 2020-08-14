import math

# returns INDEX of smallest element
def smalggl_idx(a):
    left = 0
    right = len(a) - 1
    # checks if array is shifted
    # if not, return first value
    if a[left] < a[right]:
        return 0
    # while loop  runs bc we now know array if shifted
    while right - left != 1:
        print("array = " + str(a[left:right + 1]))
        print("right - left = " + str(right - left))
        # index of mid
        mid = math.floor(len(a[left:right + 1]) / 2)
        print("mid index = " + str(mid))
        print("mid = " + str(a[left + mid]))
        # mid would get the index from the original array
        # so I had to use left + mid to get the mid of the shortened array
        if a[left] > a[left + mid]:
            print(str(a[left]) + " is greater than " + str(a[left + mid]) + "\n")
            right = left + mid
        if a[left] < a[left + mid]:
            print(str(a[left]) + " is less than " + str(a[left + mid]) + "\n")
            left = left + mid
    print("final array" + str(a[left:right + 1]))
    return a.index(a[right])

def small_idx(a):
    left = 0
    right = len(a) - 1
    # checks if array if shifted
    if a[left] < a[right]:
        return 0
    # while loop  runs bc we now know array if shifted
    while right - left != 1:
        mid = math.floor(len(a[left:right + 1]) / 2)
        if a[left] > a[left + mid]:
            right = left + mid
        if a[left] < a[left + mid]:
            left = left + mid
    return a.index(a[right])


arr = [3, 4, 5, 6, 7, 1, 2]
print("index of smallest element = " + str(smalggl_idx(arr)))
