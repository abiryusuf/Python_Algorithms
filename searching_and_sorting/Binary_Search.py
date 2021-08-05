"""
Main purpose the binary search is "don't need to execute the whole list to find the
target value, so it is save time
we can divided low and high and find the mid and make a condition with low and high

I can eliminate half the values in the list when the target value is not found at the
middle position

# # follow the order from biggest number
"""

arr = [1, 2, 3, 4, 5, 6, 7]

pos = -1
def binary(arr, target):
    low = 0
    last_item = len(arr) - 1

    while low < last_item:
        mid = (low + last_item) // 2
        if arr[mid] == target:
            return True
        if arr[mid] < target:
            low = mid
        else:
            last_item = mid
    return False
target = 12

x = binary(arr, target)

if x == -1:
    print("item is not found")
else:
    print("Found", x)




























