
info = 'abir_yusuf_ny_usa'
# out put: {0: 'abir', 1: 'yusuf', 2: 'ny', 3: 'usa'}
# def convertDict(str):
#     y = "_"
#     x = str.split(y)
#     res = {}
#     for i, value in enumerate(x):
#         if i not in res:
#             res[i] = value
#     return res
#
# print(convertDict(info))

arr = [1, 2, 3, 4, 5]
#
# def listDict(arr):
#     res = {}
#     for i, value in enumerate(arr):
#         if i not in res:
#             res[i] = value
#     return res
# print(listDict(arr))
#
# name = "I am abir"
# def countText(str):
#     str = str.replace(" ", "")
#     res = {}
#     for i in str:
#         if i in res:
#             res[i] += 1
#         else:
#             res[i] = 1
#     return res
# print(countText(name))

arr_lst = [9,8,7,6]

def swap(arr):
    n = len(arr)

    temp = arr[0]
    arr[0] = arr[n - 1]
    arr[n - 1] = temp
    return arr
print(swap(arr))

def swap_a(arr_1):
    n = len(arr_1)
    temp = arr_1[0]
    arr_1[0] = arr_1[n - 1]
    arr_1[n - 1] = temp

    return arr_1

print(swap_a(arr_lst))

int_arr = [1, 2, 3, 4]

x = int_arr[::-1]
print(x)

def intArr(arr):
    n = len(arr)

    res = []
    for i in range(n):
        n -= 1
        res.append(arr[n])
    return res
print(intArr(int_arr))

