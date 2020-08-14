import math

# returns absolute value of a square rooted number w/o the sqrt function
def square_root():
    # set a lower bound and higher bound to keep track of which integers the sqrt must be between
    num = abs(int(input("Enter a number and I'll find the sqrt of it! ")))
    lower_bound = 0
    higher_bound = num
    half = math.ceil((lower_bound + higher_bound) / 2)
    if half == num | half == 1:
        return num
    while half != num:
        if half**2 == num:
            return half
        elif (half - 1)**2 < num < half**2:
            return half
        elif half**2 > num:
            higher_bound = half
            # used math.ceil to avoid a float being returned
            half = math.ceil((lower_bound + higher_bound) / 2)
        elif half**2 < num:
            lower_bound = half
            half = math.ceil((lower_bound + higher_bound) / 2)


# takes arr and finds smallest missing number
def smallest_num(arr):
    n = len(arr)

    # makes sure m is larger than n
    m = int(input("Enter a value for m "))
    while m <= n:
        m = int(input("Value must be greater than size of array! "))

    left = 0
    right = n - 1

    # if first and last index match their value, there is no missing number
    if (left == arr[left]) and (right == arr[right]):
        return n

    # checks to see if middle value matches its index
    # if it does, remove value from right side
    # if it doesn't, remove value from left side
    while left <= right:

        # mid = half of arr size
        mid = int((left + right) / 2)
        print("mid is " + str(mid) + "\n")

        # first check if middle value is missing value
        # will always reach this return if first if statement is not true
        if (mid != arr[mid]) and (mid - 1 == arr[mid - 1]):
            return "missing is " + str(mid)

        # only keeps array up to mid value
        elif mid != arr[mid]:
            right = mid - 1

        # only keeps mid value and after
        else:
            left = mid + 1
    return 0
