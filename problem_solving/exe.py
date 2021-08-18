
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

def listDict(arr):
    res = {}
    for i, value in enumerate(arr):
        if i not in res:
            res[i] = value
    return res
print(listDict(arr))

name = "I am abir"
def countText(str):
    str = str.replace(" ", "")
    res = {}
    for i in str:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res
print(countText(name))
