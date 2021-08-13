
# follow the order from smallest number
arr = [5, 3, 8, 6, 7, 2]

def selectionSort(arr):

    length = len(arr)

    for i in range(length):
        min_idx = i
        for j in range(i + 1, length):
            if arr[min_idx] > arr[j]:
                min_idx = j


