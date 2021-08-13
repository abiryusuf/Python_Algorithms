"""
Sometimes it may be necessary to take two sorted lists and merge
them to create a new sorted list.
"""
list_A = [2, 10, 3, 5, 1, 2]
list_B = [12, 8, 4, 9, 11, 2, 2, 11, 10]

def mergeSortedList(ListA, ListB):
    ListA = sorted(ListA)
    ListB = sorted(ListB)
    a = 0
    b = 0
    newList = list()

    while a < len(ListA) and b < len(ListB):
        if ListA[a] < ListB[b]:
            newList.append(ListA[a])
            a += 1
        else:
            newList.append(ListB[b])
            b += 1
    # Add new item
    while a < len(ListA):
        newList.append(ListA[a])
        a += 1
    while b < len(ListB):
        newList.append(ListB[b])
        b += 1
    return newList
print(mergeSortedList(list_A, list_B))

# SET
def mergeUnique(list_1, list_2):
    x = 0
    y = 0

    newList = set()

    while x < len(list_1) and y < len(list_2):
        if list_1[x] < list_2[y]:
            newList.add(list_1[x])
            x += 1
        else:
            newList.add(list_2[y])
            y += 1
# add new item
    while x < len(list_1):
        newList.add(list_1[x])
        x += 1
    while y < len(list_1):
        newList.add(list_2[y])
        y += 1
    return newList
print(mergeUnique(list_A, list_B))


def duplicate(list):
    res = set()
    a = 0
    while a < len(list):
        res.add(list[a])
        a += 1
    return res
print(duplicate(list_B))


def dup(num):
    seen = set()
    new_list = []

    for item in num:
        if item not in seen:
            new_list.append(item)
            seen.add(item)
    return new_list
print(dup(list_B))

def totalSum(num):
    sum = 0

    for i in range(len(num)):
        sum += i
    return sum
print(totalSum(5))