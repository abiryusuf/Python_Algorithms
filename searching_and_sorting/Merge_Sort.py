"""
Sometimes it may be necessary to take two sorted lists and merge
them to create a new sorted list.
"""
listA = [2, 10, 3, 5, 1]
listB = [12, 8, 4, 9, 11]

def mergeSort(list_A, list_B):
    # index
    a = 0
    b = 0
    # store new value
    newList = list()

    while a < len(list_A) and b < len(list_B):
        if list_A[a] < list_B[b]:
            newList.append(list_A[a])
            a += 1
        else:
            newList.append(list_B[b])
            b += 1

    while a < len(list_A):
        newList.append(list_A[a])
        a += 1
    while b < len(list_B):
        newList.append(list_B[b])
        b += 1
    return newList
#print(mergeSort([1, 4, 6], [4, 6, 7, 8]))
print(mergeSort(listA, listB))