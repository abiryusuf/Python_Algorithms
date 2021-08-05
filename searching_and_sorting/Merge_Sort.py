"""
Sometimes it may be necessary to take two sorted lists and merge
them to create a new sorted list.
"""
list_A = [2, 10, 3, 5, 1]
list_B = [12, 8, 4, 9, 11]

def mergeSort(list_A, list_B):
    # index
    a = 0
    b = 0
    # store new value
    newList = []

    while a < len(list_A) and b < len(list_B):
        if list_A[a] < list_B[b]:
            newList.append(list_A[a])
            a += 1
        else:
            newList.append(list_B[b])
            b += 1

    while a < len(list_A):
        newList.append(list_A[a])

    return newList
print(mergeSort(list_A, list_B))