"""
Sequential search the item from the list and loop will execute until find the target
and each element compared against the target value

if not found it will return -1

Linear search: finding the phone number by searching in phone
"""

def linearSearch(value, target):
    length = len(value)
    for i in range(0, length):
        if value[i] == target:
            return i
    return -1
arr = [3, 5, 6, 10, 13, 16]
tar = 10
x = linearSearch(arr, tar)
if x == -1:
    print("Not found")
else:
    print("Item is found ", x)

