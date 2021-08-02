import sys

arr = [64, 25, 12, 22, 11, 14]
arr_1 = len(arr)
for i in range(arr_1):
    min_idx = i
    # print(min_idx)
    for j in range(i + 1, arr_1):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print("Sorted array ")
for i in range(arr_1):
    print("%d" % arr[i])


x = sorted(arr)
print(x)

for i, value in enumerate(arr):
    print(i, value)
