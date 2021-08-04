"""
Sequential search the item from the list and loop will execute until find the target
and each element compared against the target value

if not found it will return -1

Linear search: finding the phone number by searching in phone
"""
arr = [2, 5, 3, 7, 9]
target = 3
def linearSearch(value, target):
    length = len(value)

    for i in range(0, length):
        if value[i] == target:
            return i
    return -1

x = linearSearch(arr, target)
if x == -1:
    print("Not found")
else:
    print("Item is found ", x)

