
arr = [5, 3, 8, 6, 7, 2]

length = len(arr)

for i in range(length):
    # find the index number for each element
    min_idx = i
    # print(min_idx)
    for j in range(i + 1, length):
        if arr[j] < arr[min_idx]:
            min_idx = j
    # swap
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

for i in range(length):
    print(arr[i])

# for i, value in enumerate(arr):
#     print(i + 1, value)