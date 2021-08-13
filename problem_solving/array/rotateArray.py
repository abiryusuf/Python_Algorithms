
arr = [1, 2, 3, 4, 5, 6, 7]

def arrayRotate(arr, target):
    n = len(arr)

    temp = []
    i = 0
    while i < target:
        temp.append(arr[i])
        i += 1
    while target < n:
        arr[i] = arr[d]
    return temp
print(arrayRotate(arr, 3))