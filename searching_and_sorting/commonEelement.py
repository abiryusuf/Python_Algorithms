arr_1 = [1, 3, 5, 6]
arr_2 = [3, 5, 6, 7]

def commonElement(a, b):
    num_1 = 0
    num_2 = 0

    res = []

    while num_1 < len(a) and num_2 < len(b):
        if a[num_1] == b[num_2]:
            res.append(a[num_1]) and res.append(b[num_2])
            num_1 += 1
            num_2 += 1
        elif a[num_1] < b[num_2]:
            num_1 += 1
        else:
            num_2 += 1
    return res
print(commonElement(arr_1, arr_2))