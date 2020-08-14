import random
from Quick_select import *

n = int(input("How many values would you like in your array? "))
arr = []

for i in range(n):
    arr.append(random.randint(-99, 99))
print(arr)
k = int(input("Would you like k to equal "))
while k > n:
    k = int(input("k must be smaller than " + str(n) + " "))

quick_select(arr, k)
max_k(arr, k)
