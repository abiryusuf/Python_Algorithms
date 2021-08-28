arr = [1, 3, 5, 7]
print(arr[-1])
n = len(arr)
x = arr[n - 1]
print(x)

first = arr[0]
arr[0] = arr[n - 1]
arr[n - 1] = first
print(arr)
arr_1 = [1, 2, 3, 5]
y = arr_1[::-1]
print(y)

def reverse(num):
    n = len(num)
    res = []
    for i in range(n):
        n -= 1
        res.append(num[n])
    return res
print(reverse(arr_1))