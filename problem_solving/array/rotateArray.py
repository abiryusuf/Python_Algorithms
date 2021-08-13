
arr = [1, 2, 3, 4, 5, 6, 7]

def arrayRotate(arr, target, n):
    n = len(arr)

    temp = []
    i = 0
    while i < target:
        temp.append(arr[i])
        i += 1
    i = 0
    while target < n:
        arr[i] = arr[target]
        i += 1
        target += 1
    arr[:] = arr[: i] + temp
    return arr
print(arrayRotate(arr, 3, len(arr)))
