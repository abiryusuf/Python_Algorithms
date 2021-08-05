"""
Bubble Sort: Rearranges the value by iterating over the list multiple times, causing
larger values to bubble to the top or end of the list.

Main reasons is find the large value from end of the list
Bubble sort needs two loops

# # follow the order from biggest number
"""

arr = [12, 3, 6, 11, 5, 10]

def bubbleSort(arr):
    length = len(arr)

    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubbleSort(arr)

for i in range(len(arr)):
    print(arr[i])

