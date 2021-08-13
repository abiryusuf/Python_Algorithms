
arr_1 = [3, 4, 6, 7, 7]
def total(arr):
    res = 0
    arr1 = len(arr)
    for i in arr:
        res += i

    return res // arr1
print(total(arr_1))

def maxNum(arr):
    max = 0
    for i in arr:
        current = i
        if current > max:
            max = current
    return max
print(maxNum(arr_1))

arr_1 = [3, 4, 6, 7, 7]
def minNum(arr):
    min = arr[0]

    for i in range(1, len(arr)):
        current = arr[i]
        if current < min:
            min = current
    return min
print(minNum(arr_1))

def minMax(num):
    min = num[0]
    max = num[0]

    for i in range(1, len(num)):
        current = num[i]
        if current < min:
            min = current
        if current > max:
            max = current
    return min, max
print(minMax(arr_1))



